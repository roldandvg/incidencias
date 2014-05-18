# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class FormAcceso(forms.Form):
    usuario = forms.CharField(label="Usuario",
                              widget=forms.TextInput(attrs={"size": "15", "class": "small",
                                                            "placeholder": "Nombre de usuario"}))
    passwd = forms.CharField(label="Contraseña",
                             widget=forms.PasswordInput(attrs={"size": "15", "class":"small",
                                                               "placeholder": "contraseña de acceso"}))

    def clean_usuario(self):
        usuario = self.cleaned_data['usuario']

        if not User.objects.filter(username=usuario):
            raise forms.ValidationError("El usuario no existe")
        else:
            usr = User.objects.get(username=usuario)
            if not usr.is_active:
                raise forms.ValidationError("El usuario esta inactivo")

        return self.cleaned_data['usuario']

    def clean_passwd(self):
        usuario = self.data['usuario']
        passwd = self.cleaned_data['passwd']

        if User.objects.filter(username=usuario):
            usr = User.objects.get(username=usuario)
            if not usr.check_password(passwd):
                raise forms.ValidationError("La contraseña es incorrecta")

        return self.cleaned_data['passwd']