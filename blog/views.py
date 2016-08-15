from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    Rasoa=Post.objects.all()
    return render(request, 'blog/post_list.html', {"Posts": Rasoa})
