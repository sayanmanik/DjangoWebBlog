from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def home(request):
    contexts = {
        'posts' : Post.objects.all()
    }
    return render(request,'blogs/home.html',contexts)

def about(request):
    return render(request,'blogs/about.html',{'title':'About'})