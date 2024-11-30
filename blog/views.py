from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all().order_by('-date_posted')
    return render(request, 'blog/home.html', {'posts': posts})

def profile(request):
    return render(request, 'blog/profile.html')
def workshops(request):
    return render(request, 'blog/workshops.html')

def seminar(request):
    return render(request, 'blog/seminar.html')
def res(request):
    return render(request, 'blog/res.html')

def pub(request):
    return render(request, 'blog/pub.html')

def app(request):
    return render(request, 'blog/app.html')
def pro(request):
    return render(request, 'blog/pro.html')
