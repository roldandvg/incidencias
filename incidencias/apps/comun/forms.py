# -*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea, Select
from incidencias.apps.comun.models import Persona

class PersonaForm(ModelForm):
    class Meta:
        model = Persona