# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach


def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect("dbname=forum")
    conn = db.cursor()
    conn.execute("SELECT content, time FROM posts ORDER BY time DESC")
    return conn.fetchall()
    db.close()  # unreachable?


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    db = psycopg2.connect("dbname=forum")
    conn = db.cursor()
    content = bleach.clean(content)
    conn.execute("INSERT INTO posts VALUES (%s)", (content,))
    conn.execute("UPDATE posts SET content = 'cheese what!' WHERE content LIKE"
                 " '%spam%'")
    db.commit()
    db.close()
