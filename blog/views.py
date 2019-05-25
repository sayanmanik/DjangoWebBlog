from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [

    {
        'author' : 'Sayan Manik',
        'title' : 'Blog post 1',
        'content' : 'First Post Content',
        'date_posted' : 'May 25, 2019'
    },

    {
        'author' : 'Corey MS',
        'title' : 'Blog post 2',
        'content' : 'Second Post Content',
        'date_posted' : 'May 25, 2019'
    },
]

def home(request):
    contexts = {
        'posts' : posts
    }
    return render(request,'blogs/home.html',contexts)

def about(request):
    return render(request,'blogs/about.html',{'title':'About'})