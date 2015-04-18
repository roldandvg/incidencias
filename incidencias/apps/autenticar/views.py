# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core import urlresolvers
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.template.loader import get_template
from django.template.context import Context, RequestContext
from django.core.mail import send_mail

from datetime import datetime

from incidencias.apps.autenticar.forms import FormAcceso
from incidencias.apps.comun.constantes import INTENTOS_ACCESO, TIEMPO_SESION

import json
import time
import os
import smtplib


class UsuarioList(ListView):
    model = User
    paginate_by = 10

    def get_queryset(self):
        if len(self.args) > 0:
            return User.objects.filter(username__icontains=self.args[0])
        else:
            return User.objects.all()


class UsuarioCreate(CreateView):
    model = User
    fields = ["personal", "username", "password", "email", "is_superuser", "is_staff", "is_active"]
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        form.instance.set_password(form.instance.password)
        return super(UsuarioCreate, self).form_valid(form)


class UsuarioUpdate(UpdateView):
    model = User
    fields = ["personal", "username", "password", "email", "is_superuser", "is_staff", "is_active"]
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        form.instance.set_password(form.instance.password)
        return super(UsuarioUpdate, self).form_valid(form)


class UsuarioDelete(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')

def generar_pass():
    import string
    from random import seed, choice

    seed("%d%s" % (os.getpid(), time.ctime()))

    letras = string.letters
    numeros = string.digits
    newpass = ''.join(choice([choice(letras),choice(numeros)]) for x in range(10))

    return newpass


def inicio(request):
    form = FormAcceso()
    return render_to_response('base.html', {'form': form}, context_instance=RequestContext(request))


def acceso(request):
    now = datetime.now()

    contador = 0

    if request.method == "POST":
        if (request.POST['usuario']!="" or request.POST['passwd']!="" or (request.POST['usuario']=="" and request.POST['passwd']=="")) and not 'contador_acceso' in request.session:
            request.session['contador_acceso'] = "0"
        else:
            contador = int(request.session['contador_acceso']) + 1
            request.session['contador_acceso'] = str(contador)

        form = FormAcceso(data=request.POST, auto_id="%s")

        if form.is_valid():
            request.session['contador_acceso'] = "0"
            usuario = authenticate(username=str(request.POST['usuario']), password=str(request.POST['passwd']))
            login(request, usuario)
            usr = User.objects.get(username=str(request.POST['usuario']))
            usr.last_login = now
            usr.save()
            return HttpResponseRedirect(urlresolvers.reverse("incidencias.apps.autenticar.views.inicio"))
        else:
            if int(request.session['contador_acceso'])>(INTENTOS_ACCESO-1):
                del request.session['contador_acceso']
                if User.objects.filter(username=str(request.POST['usuario'])):
                    usr = User.objects.get(username=str(request.POST['usuario']))
                    usr.is_active=False
                    usr.save()
            return render_to_response('base.html', {'form': form}, context_instance=RequestContext(request))

def send_templated_mail(email, template, subject, vars={}):
    try:
        t = get_template(template)
        c = Context(vars)
        send_mail(subject, t.render(c), settings.EMAIL_FROM, [email], fail_silently=False)
        logging.info(u"correo enviado a %s usando la plantilla '%s'" % (email, template))
        return True
    except smtplib.SMTPException, e:
        logging.error(u"ocurrió un error al enviar el correo. Detalles del error %s" % e.message, exc_info=True)
        return False

def forgotpass(request):
    if not request.is_ajax():
        return HttpResponse(json.dumps({'resultado': False, 'msg': 'no se pudo enviar el correo'}))

    email = request.GET.get('email', None)
    user = User.objects.get(email=email)
    passwd = generar_pass()
    
    if user:
        try:
            enviado = send_templated_mail(email, "auth/resetpass.mail", 'Nueva Contraseña', {'passwd':passwd})
            user.set_password(passwd)
            user.save()
            return HttpResponse(json.dumps({'resultado': True}))
        except Exception, e:
            print e.message
            return HttpResponse(json.dumps({'resultado': False}))
    else:
        return HttpResponse(json.dumps({'resultado': False, 'msg': 'No se pudo enviar la nueva contraseña'}))

@login_required()
def salir(request):
    user = request.user
    if user.is_authenticated():
        logout(request)
    return HttpResponseRedirect(settings.LOGOUT_URL)