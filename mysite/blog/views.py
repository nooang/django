from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpRequest
from .models import Post, Reply
from .forms import PostForm

# Create your views here.
def index(request:HttpRequest):
  post_list = Post.objects.order_by('-create_date')
  context = {'post_list': post_list}

  return render(request, "blog/post_list.html", context)

def detail(request:HttpRequest, post_id:int):
  # post = Post.objects.get(id=post_id)
  post = get_object_or_404(Post, pk=post_id)
  context = {"post": post}
  
  return render(request, "blog/post_detail.html", context)

def reply_create(request:HttpRequest, post_id:int):
  post = get_object_or_404(Post, pk=post_id)
  content = request.POST.get('content')
  now = timezone.now()
  reply = Reply(post=post, content=content, create_date=now, modify_date=now)
  reply.save()
  
  return redirect('blog:detail', post_id=post.id)

def post_create(request:HttpRequest):
  form = PostForm()
  context = {'form': form}
  return render(request, 'blog/post_form.html', context)