from incidencias.apps.comun.models import Zona
from model_report.report import reports, ReportAdmin

class AnyModelReport(ReportAdmin):
    title = ('AnyModel Report Name')
    model = Zona
    fields = [
        'nombre',
    ]
    list_order_by = ('nombre',)
    type = 'report'

reports.register('prueba', AnyModelReport)
