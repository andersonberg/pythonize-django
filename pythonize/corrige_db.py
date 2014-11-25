import sqlite3

conn = sqlite3.connect("dev.db")
with conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = "SELECT id,short_url,slug FROM blog_blogpost "
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        print row
        #new_url = str('http://pythonize.org/blog/%s/' % str(row["slug"]))
        #uId = str(row["id"])
        #sql_cor = "UPDATE blog_blogpost SET short_url=? WHERE id=?", (new_url, uId)
        #cursor.execute("UPDATE blog_blogpost SET short_url=? WHERE id=?", (new_url, uId))
        #conn.commit()
