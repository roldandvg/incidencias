from django import forms


# Este formulario debe hacerser en el template con tabs debido a lo extenso del mismo
class FormNovedad(forms.Form):
    fecha = forms.DateField()
    lugar = forms.CharField()
    motivo = forms.CharField()
    descripcion = forms.CharField()
    hora_salida = forms.TimeField()
    hora_llegada = forms.TimeField()
    hora_reporte = forms.TimeField()
    tipo_procedimiento = forms.ChoiceField()
    unidad = forms.ChoiceField()  # esto debe ser un formset
    comision = forms.ChoiceField()  # esto debe ser un formset
    # persona debe ser un formset con todos los datos del modelo persona
    # Falta por agregar muchísimos campos de otros modelos