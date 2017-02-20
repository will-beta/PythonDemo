import datetime
from sqlalchemy import MetaData, create_engine, Table, Column, Integer, String, DateTime, JSON, ARRAY
from sqlalchemy.sql import select, delete

# 引擎
engine = create_engine('postgresql://postgres:postgres@localhost:5432/BlogDb')
# 元数据
metadata = MetaData(engine)
# 连接
conn = engine.connect()

# 表结构
posts = Table('Posts', metadata,
              Column('PostId', Integer, primary_key=True, autoincrement=True),
              Column('PostTitle', String(256), nullable=True),
              Column('Content', String(256), nullable=True),
              Column('CreatedAt', DateTime(timezone=True), nullable=False),
              Column('Tags', ARRAY(String), nullable=True),
              Column('Festivals', ARRAY(DateTime(timezone=True)), nullable=True),
              Column('PostType', Integer, nullable=False),
              Column('Author', JSON, nullable=False)
              )


# 创建数据表
metadata.drop_all()
metadata.create_all()


# C操作
for i in range(1, 10):
    now = datetime.datetime.now()
    sql = posts.insert().values(
        PostId=i,
        CreatedAt=now,
        PostTitle="title%d" % i,
        Content="#",
        Tags=["b", "c"],
        Festivals=[
            now + datetime.timedelta(days=-1), now + datetime.timedelta(days=-2), ],
        Author="{""Name"":""Li"",""Age"":23}",
        PostType=i,
    )
    conn.execute(sql)

# U操作
sql = posts.update().values(Content=posts.c.Content + "#").where(posts.c.PostId > 5)
conn.execute(sql)

# R操作
sql = posts.select()
for post in conn.execute(sql):
    print("%s    :     %s    :     %s    :     %s"
          % (post[posts.c.PostTitle], post[posts.c.CreatedAt], post[posts.c.Content], post[posts.c.Festivals])
          )


# D操作
sql = posts.delete().where(posts.c.PostId > 4)
conn.execute(sql)
