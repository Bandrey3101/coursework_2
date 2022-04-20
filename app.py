from flask import Flask, render_template, request, jsonify
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, \
    get_post_by_name, find_post_by_tag



app = Flask(__name__)


@app.route("/")
def index():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route("/posts/<int:pk>/")
def post_view(pk):
    post = get_post_by_pk(pk)

    comments = get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments)


@app.route("/search/")
def search():
    search_by = request.args['s']
    posts = find_post_by_tag(search_by)
    return render_template('index.html', search_by=search_by, posts=posts)


@app.route("/users/<username>/")
def user_posts(username):
    users_posts = get_post_by_name(username)
    print(users_posts)
    return render_template('index.html', posts=users_posts)


@app.route("/api/")
def api_index():
    posts = get_posts_all()
    return jsonify(posts)


@app.route("/api/<int:post_id>")
def api_id(post_id):
    posts = get_post_by_pk(post_id)
    return jsonify(posts)

if __name__ == "__main__":
    app.run()
