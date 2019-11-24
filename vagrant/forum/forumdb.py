# "Database code" for the DB Forum.

import datetime
import psycopg2

# POSTS = [("This is the first post.", datetime.datetime.now())]


def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect("dbname=forum")
    conn = db.cursor()
    conn.execute("SELECT content, time FROM posts ORDER BY time DESC")
    db.close()
    return conn.fetchall()


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    # POSTS.append((content, datetime.datetime.now()))
    db = psycopg2.connect("dbname=forum")
    conn = db.cursor()
    conn.execute("INSERT INTO posts VALUES ('%s')", content)
    db.commit()
    count = conn.rowcount
    print(count, "Record inserted successfully into forum posts table")
    db.close()

