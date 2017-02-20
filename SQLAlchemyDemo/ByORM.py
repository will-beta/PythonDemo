import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime, JSON, ARRAY


# 生成一个SqlORM基类
Base = declarative_base()


class Post(Base):
    # 表名为hosts
    __tablename__ = 'Posts'

    # 表结构
    PostId = Column(Integer, primary_key=True, autoincrement=True)
    PostTitle = Column(String(256), nullable=True)
    Content = Column(String(256), nullable=True)
    CreatedAt = Column(DateTime(timezone=True), nullable=False)
    Tags = Column(ARRAY(String), nullable=True)
    Festivals = Column(ARRAY(DateTime(timezone=True)), nullable=True)
    PostType = Column(Integer, nullable=False)
    Author = Column(JSON, nullable=False)


# 引擎
engine = create_engine('postgresql://postgres:postgres@localhost:5432/BlogDb')
# 创建数据表，如果数据表存在，则忽视
Base.metadata.create_all(engine)




# 创建与数据库的会话
DbSession = sessionmaker(bind=engine)
session = DbSession()


# C操作
for i in range(1, 10):
    now = datetime.datetime.now()
    post = Post(
        PostId=i,
        CreatedAt=now,
        PostTitle="title%d" % i,
        Content="#",
        Tags=["b", "c"],
        Festivals=[now + datetime.timedelta(days=-1), now + datetime.timedelta(days=-2), ],
        Author="{""Name"":""Li"",""Age"":23}",
        PostType=i,
    )
    session.add(post)
session.commit()

# U操作
for post in session.query(Post).filter(Post.PostId > 5):
    post.Content += "#"
session.commit()

# R操作
for post in session.query(Post).filter():
    print("%s    :     %s    :     %s    :     %s"
          % (post.PostTitle, post.CreatedAt, post.Content, post.Festivals)
         )

# D操作
session.query(Post).filter(Post.PostId > 4).delete()
session.commit()

