from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = {
        'post': Post.objects.all()
    }
    return render(request, 'blog/home.html', posts)