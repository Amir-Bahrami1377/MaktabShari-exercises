from django.shortcuts import render, redirect
from post.models import Post, Comment
from .forms import CreatePostForm


def home(request):
    posts = Post.objects
    return render(request, 'home.html', context={'posts': posts})


def detail(request, post_title):
    post = Post.objects(title=f'{post_title}')
    return render(request, 'detail.html', context={'post': post[0]})


# for post in Post.objects(title='post2'):
#     print(post.content)
def delete(request, post_title):
    Post.objects(title=f'{post_title}').delete()
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post = Post()
            if cd.get('title'):
                post.title = cd.get('title')
            if cd.get('content'):
                post.content = cd.get('content')
            if cd.get('detail'):
                post.detail = cd.get('detail')
            if cd.get('author'):
                post.author = cd.get('author')
            if cd.get('image_path'):
                post.image_path = cd.get('image_path')
            if cd.get('link_url'):
                post.link_url = cd.get('link_url')
            if cd.get('tags'):
                tag_list = cd.get('tags').split()
                post.tags = tag_list
            post.save()
            print('object added')
        return redirect('home')
    else:
        form = CreatePostForm()
    return render(request, 'create.html', context={'form': form})