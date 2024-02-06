from django.shortcuts import render, redirect
import datetime
from .models import Post, Author
from django.http import HttpResponse
from .forms import AddPost, AddPostModel

# Create your views here.

def posts(request):
    posts = Post.objects.all()

    return  render(request, 'posts.html', {"posts":posts})
      
def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        post = ""
    return render(request, 'post.html', {"post":post})

# def add_post(request):
#     if request.method == "POST":
#         form = AddPost(request.POST, request.FILES)

#         if form.is_valid():
#             post_entry = Post()
#             post_entry.author = Author.objects.all()[0]
#             post_entry.issued= datetime.datetime.now()
#             # cleaned_data - провалидированные данные
#             post_entry.title = form.cleaned_data['title']
#             post_entry.content = form.cleaned_data['content']
#             post_entry.post_type = form.cleaned_data['post_type']
#             post_entry.image = form.cleaned_data['image']

#             post_entry.save()

#             return redirect('post', post_entry.id)

#     else:
#         form = AddPost()
#     return render(request, 'add_post.html', {'form':form})

def add_post(request):
    if request.method == "POST":
        form = AddPostModel(request.POST, request.FILES)

        if form.is_valid():
            post_entry = form.save(commit=False)
            post_entry.author = Author.objects.get(email=request.user.email)
            post_entry.issued = datetime.datetime.now()
            #save_m2m – сохранение формы many to many (многие к многим) и в стр53 ее сохранение
            # form.save_m2m()
            # form.save()
            post_entry.save()

            return redirect('post', post_entry.id)
    else:
        form = AddPostModel()

    return render(request, 'add_post.html', {'form':form})