import datetime

from mongo import *


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    content = StringField()
    detail = StringField()
    author = StringField()
    image_path = StringField()
    link_url = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {'allow_inheritance': True}


# post1 = Post(title='post3', author='akber', link_url='https://docs.mongoengine.com/')
# post1.content = 'you looks pretty cool.'
# post1.image_path = 'https://beginnersbook.com/wp-content/uploads/2017/09/MongoDB_Delete_Document.jpg'
# post1.tags = ['akberdb', 'mongoengine']
# post1.detail = 'detail : lhfw;fhreweghr;ghr;ewugh;rfgvjfshggewhg;rgho;qghr;egqurh;oghq;gurgheoghregh;oerhg'
# post1.save()
