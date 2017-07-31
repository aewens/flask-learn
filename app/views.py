from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"nick": "aewens"}
    posts = [
        {
            "author": {"nick": "aewens"},
            "body": "Test post for testing the posts."
        },
        {
            "author": {"nick": "admin"},
            "body": "Posts can now be made, hurray!"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
