from django.shortcuts import render
from django.views import View
from .models import Gaim


# Create your views here.



class Gaims(View):
    def get(self, request):
        posts = Gaim.objects.all()
        return render(request, 'main/index.html', {'post': posts})