from sqlalchemy import create_engine, text


# 引擎
engine = create_engine('postgresql://postgres:postgres@localhost:5432/BlogDb')


#-----------------------------------
# DDL
#-----------------------------------
engine.execute("DROP TABLE IF EXISTS users")
engine.execute("create table users(userid int4, username char(50))")


#-----------------------------------
# DML
#-----------------------------------
resultProxy = engine.execute(
    "insert into users (userid,username) values('1','tony')")
resultProxy = engine.execute(
    "insert into users (userid,username) values('2','peter')")
resultProxy = engine.execute(
    "insert into users (userid,username) values('3','jerry')")
# return rows affected by an UPDATE or DELETE statement
print("affected rows count    :     %s" % resultProxy.rowcount)


#-----------------------------------
# Query
#-----------------------------------
sql = text("select * from users where userid>:id")
resultProxy = engine.execute(sql, id=1)
for item in resultProxy.fetchall():
    print("%s    :     %s"
          % (item["userid"], item["username"])
          )


# 关闭
resultProxy.close()


# resultProxy.close(), resultProxy 用完之后, 需要close
#resultProxy.scalar(), 可以返回一个标量查询的值
# ResultProxy 类是对Cursor类的封装(在文件sqlalchemy\engine\base.py),
# ResultProxy 类有个属性cursor即对应着原来的cursor.
# ResultProxy 类有很多方法对应着Cursor类的方法, 另外有扩展了一些属性/方法.
# resultProxy.fetchall()
# resultProxy.fetchmany()
# resultProxy.fetchone()
# resultProxy.first()
# resultProxy.scalar()
# resultProxy.returns_rows  #True if this ResultProxy returns rows.
# resultProxy.rowcount  #return rows affected by an UPDATE or DELETE
# statement. It is not intended to provide the number of rows present from
# a SELECT.
