from django.shortcuts import render, redirect
from django.views import View
from post.models import Post, Comment
from post.utils import create_post, update_post
from post.forms import CreatePostForm, UpdatePostForm, CreateCommentForm


class HomeView(View):
    def get(self, request):
        posts = Post.objects.order_by('-created_at', 'title')
        return render(request, 'home.html', context={'posts': posts})


class DetailView(View):
    def get(self, request, post_title):
        post = Post.objects(title=f'{post_title}')
        post = post.get(title=f'{post_title}')
        form = CreateCommentForm()
        return render(request, 'detail.html', context={'post': post, 'form': form})

    def post(self, request, post_title):
        post = Post.objects(title=f'{post_title}')
        post = post.get(title=f'{post_title}')
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            coments = post.comments
            coments.append(Comment(name= cd.get('name'), content= cd.get('content')))
            post.comments = coments
            post.save()
            form = CreateCommentForm()
            return render(request, 'detail.html', context={'post': post, 'form': form})



class CreateView(View):
    def get(self, request):
        form = CreatePostForm()
        return render(request, 'create.html', context={'form': form})

    def post(self, request):
        form = CreatePostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_instance = create_post(cd=cd)
            if not post_instance:
                return redirect('create')
            post_instance.save()
        return redirect('home')


class UpdateView(View):
    def get(self, request, post_title):
        post = Post.objects(title=f'{post_title}')
        post = eval(post.to_json())
        post = post[0]
        print(post)
        if post.get('tags'):
            str_tags = ' '.join(post.get('tags'))
            post.update(tags=str_tags)
        if post.get('author'):
            str_author = ' '.join(post.get('author'))
            post.update(author=str_author)
        form = UpdatePostForm(data=post)
        print(post)
        return render(request, 'update.html', context={'form': form})

    def post(self, request, post_title):
        form = UpdatePostForm(request.POST)
        if form.is_valid():
            post = Post.objects(title=f'{post_title}')
            post = post.get(title=f'{post_title}')
            post_pk = post.pk
            cd = form.cleaned_data
            post_instance = update_post(cd=cd, post_pk=post_pk)
            if not post_instance:
                return redirect('update')
            else:
                post_instance.save()
                return redirect('home')


def delete(request, post_title):
    Post.objects(title=f'{post_title}').delete()
    return redirect('home')


# post = Post.objects(title='post2')
# post = eval(post.to_json())
# post = post[0]
# print(post.get('tags'))
# temp = {}
# post = Post.objects(title='post7')
# post = post.get(title='post7')
# print(post.pk)
