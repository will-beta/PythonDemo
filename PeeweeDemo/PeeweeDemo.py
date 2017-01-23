from peewee import *
from playhouse.postgres_ext import *
import datetime

db = PostgresqlExtDatabase(host="localhost",port="32802",database="BlogDb", user="postgres", password="postgres")

class BaseExtModel(Model):
    class Meta:
        database = db

class Post(BaseExtModel):
    PostId = IntegerField(primary_key=True)
    PostTitle = CharField(null=True)
    Content = CharField(null=True)
    CreatedAt = DateTimeTZField(null=False)
    Tags = ArrayField(CharField,null=True)
    Festivals = ArrayField(DateTimeTZField,null=True)
    PostType = IntegerField(null=False)
    Author = JSONField(null=False)
    class Meta:
        db_table = 'Posts'



db.connect()

if not Post.table_exists():
    db.create_tables([Post])



#C操作
for i in range(1,10):
    now = datetime.datetime.now()
    post = Post.create(PostId = i,
                CreatedAt = now,
                PostTitle = "title%d" % i,
                Content = "#",
                Tags = ["b", "c"],
                Festivals = [now + datetime.timedelta(days=-1), now + datetime.timedelta(days=-2),],
                Author = "{""Name"":""Li"",""Age"":23}",
                PostType = i,)
    post.save()


#U操作
for post in Post.select().where(Post.PostId > 5):
    post.Content+="#"
    post.save()


#R操作
for post in Post.select():
    print("%s    :     %s    :     %s    :     %s" % (post.PostTitle,post.CreatedAt,post.Content,post.Festivals))


#D操作
Post.delete().where(Post.PostId > 4).execute()
