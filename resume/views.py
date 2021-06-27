from django.shortcuts import render
from .models import Resume
from django.views.generic import CreateView
from django.http import HttpResponse


def home(request):
    resume_list = Resume.objects.all()
    return render(request, "resume/home.html", {"resume_list": resume_list})


class ResumeCreateView(CreateView):
    model = Resume
    fields = ['description']
    success_url = '/home'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super().form_valid(form)
        else:
            return HttpResponse(status=403)
