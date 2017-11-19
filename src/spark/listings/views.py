from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
# function based views

#def home(request):
#    return render(request, "template", {})

class HomeView(TemplateView):
    template_name = "special_non_profit.html"
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        #Aquí viene toda la lógica a mostrar en la página

        return context

class EventsView(TemplateView):
    template_name = "portfolio__boxed__3_columns.html"
    def get_context_data(self, *args, **kwargs):
        context = super(EventsView, self).get_context_data(*args, **kwargs)

        #Aquí viene toda la lógica a mostrar en la página

        return context


class BlogView(TemplateView):
    template_name = "blog__standard__left_sidebar.html"
    def get_context_data(self, *args, **kwargs):
        context = super(BlogView, self).get_context_data(*args, **kwargs)

        #Aquí viene toda la lógica a mostrar en la página

        return context
