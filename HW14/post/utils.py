from bson import ObjectId

from post.models import Post


def create_post(cd):
    post = Post()
    if cd.get('title'):
        if len(Post.objects(title=cd.get('title'))) != 0:
            return False
        else:
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
    return post


def update_post(cd, post_pk:ObjectId):
    post = Post.objects(pk=post_pk)
    post = post.get(pk=post_pk)
    if cd.get('title'):
        if len(Post.objects(title=cd.get('title'))) != 0:
            return False
        else:
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
    return post
