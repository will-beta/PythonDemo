#!/usr/bin/python
import psycopg2

conn = psycopg2.connect(host="localhost",database="BlogDb", user="postgres", password="postgres")
try:
    cur = conn.cursor()
    cur.callproc('get_posts_by_type', (0,))
    #cur.execute("SELECT * FROM get_posts_by_type( %s,); ",(0,))
    while True:
        row = cur.fetchone()
        if row is None:break

        print(row[1])
    cur.close()
finally:
    conn.close()

