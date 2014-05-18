from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core import urlresolvers
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings

from datetime import datetime

from incidencias.apps.autenticar.forms import FormAcceso


class UsuarioList(ListView):
    model = User


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


class UsuarioDelete(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')


def inicio(request):
    form = FormAcceso()
    return render_to_response('base.html', {'form': form}, context_instance=RequestContext(request))


def acceso(request):
    now = datetime.now()

    if request.method == "POST":
        form = FormAcceso(data=request.POST, auto_id="%s")

        if form.is_valid():
            usuario = authenticate(username=str(request.POST['usuario']), password=str(request.POST['passwd']))
            login(request, usuario)
            usr = User.objects.get(username=str(request.POST['usuario']))
            usr.last_login = now
            usr.save()
            return HttpResponseRedirect(urlresolvers.reverse("incidencias.apps.autenticar.views.inicio"))
        else:
            return render_to_response('base.html', {'form': form}, context_instance=RequestContext(request))

@login_required()
def salir(request):
    user = request.user
    if user.is_authenticated():
        logout(request)
    return HttpResponseRedirect(settings.LOGOUT_URL)