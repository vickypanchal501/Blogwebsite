from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render
from django.http import HttpResponse 
from blog.models import Post

# Create your views here.

def home_site(request,*args, **kwargs):
    
    return render(request, 'index.html')    

def BlogUs(request):
    # import pdb ; pdb.set_trace()
    postdata = Post.objects.filter(status="PUBLISHED")
    context_data = {
        "title": "Blog | Post Pages",
        "postdata": postdata
    }
    return render(request, 'blog.html', context_data)

def Posts(request):
    return render(request, 'post.html')