import datetime

from bson import ObjectId

from mongo import *


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    content = StringField()
    detail = StringField()
    author = ListField(StringField(max_length=30))
    image_path = StringField(default="https://www.freeiconspng.com/uploads/no-image-icon-10.png")
    link_url = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {'allow_inheritance': True}


# post1 = Post(title='post3', author=['arta'], link_url='https://docs.mongoengine.com/')
# post1.content = 'you looks pretty cool.'
# post1.image_path = 'https://beginnersbook.com/wp-content/uploads/2017/09/MongoDB_Delete_Document.jpg'
# post1.tags = ['akberdb', 'mongoengine']
# post1.detail = 'detail : lhfw;fhreweghr;ghr;ewugh;rfgvjfshggewhg;rgho;qghr;egqurh;oghq;gurgheoghregh;oerhg'
# post1.comments = [Comment(name="akbar jun", content="django is cool")]
# post1.save()
# post = Post.objects(pk=ObjectId("61f4289c2e68145c190faf53"))
# post = post.get(pk=ObjectId("61f4289c2e68145c190faf53"))
# post.content = "new content"
# post.save()
# print(eval(post.to_json()).get('_id').get('$oid'))
# post = Post.objects(title='post7')
# post = post.get(title='post7')
# print(post.pk, type(post.pk))
# print(len(Post.objects(title='post8')))
# post2=Post.objects(pk=post.pk)
# post2=post2.get(pk=post.pk)
# print(post2.title)
