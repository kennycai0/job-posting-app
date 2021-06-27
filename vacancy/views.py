from django.shortcuts import render
from .models import Vacancy
from django.views.generic import CreateView
from django.http import HttpResponse


def home(request):
    vacancy_list = Vacancy.objects.all()
    return render(request, "vacancy/home.html", {"vacancy_list": vacancy_list})


class VacancyCreateView(CreateView):
    model = Vacancy
    fields = ['description']
    success_url = '/home'

    def form_valid(self, form):
        if self.request.user.is_staff and self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super().form_valid(form)
        else:
            return HttpResponse(status=403)
