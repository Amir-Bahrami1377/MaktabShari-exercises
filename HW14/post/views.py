from django.shortcuts import render, redirect
from post.models import Post, Comment
from post.forms import CreatePostForm, UpdatePostForm


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
            print(cd)
            post = Post()
            if cd.get('title'):
                post.title = cd.get('title')
            if cd.get('content'):
                post.content = cd.get('content')
            if cd.get('detail'):
                post.detail = cd.get('detail')
            if cd.get('author'):
                author_list = cd.get('author').split()
                post.author = author_list
            if cd.get('image_path'):
                post.image_path = cd.get('image_path')
            if cd.get('link_url'):
                post.link_url = cd.get('link_url')
            if cd.get('tags'):
                tag_list = cd.get('tags').split()
                post.tags = tag_list
            post.save()
        return redirect('home')
    else:
        form = CreatePostForm()
    return render(request, 'create.html', context={'form': form})


def update(request, post_title):
    post1 = Post.objects(title=f'{post_title}')
    post1 = eval(post1.to_json())
    post1 = post1[0]
    if post1.get('tags'):
        str_tags = ' '.join(post1.get('tags'))
        post1.update(tags=str_tags)
    if post1.get('author'):
        str_author = ' '.join(post1.get('author'))
        post1.update(author=str_author)

    if request.method == 'POST':
        Post.objects(title=f'{post_title}').delete()
        form = UpdatePostForm(request.POST)
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
                author_list = cd.get('author').split()
                post.author = author_list
            if cd.get('image_path'):
                post.image_path = cd.get('image_path')
            if cd.get('link_url'):
                post.link_url = cd.get('link_url')
            if cd.get('tags'):
                tag_list = cd.get('tags').split()
                post.tags = tag_list
            post.save()
        return redirect('home')

    else:
        form = UpdatePostForm(data=post1)
    return render(request, 'update.html', context={'form': form})


# post = Post.objects(title='post2')
# post = eval(post.to_json())
# post = post[0]
# print(post.get('tags'))
# temp = {}
