from django.views.generic import TemplateView
from cadastros.models import Atividade


class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atividade'] = Atividade.objects.all()
        return context

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

