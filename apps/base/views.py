from django.shortcuts import render
from apps.base.models import Boys, Girls
# Create your views here.

def setting(request):
    boy = Boys.objects.all()
    girl = Girls.objects.all()
    return render (request, 'index.html', locals())