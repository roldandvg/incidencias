from django.db import models
from django.contrib.auth.models import User, UserManager
from incidencias.apps.institucion.models import Trabajador

User.add_to_class('personal',models.ForeignKey(Trabajador, null=True))