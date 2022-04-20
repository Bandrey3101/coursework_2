import json

POST_PATH = "data/data.json"
COMMENT_PATH = "data/comments.json"


# возвращает посты
def get_posts_all():
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_posts_by_user(poster_name):
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
        data = {}
        for i in posts:
            data[i['poster_name']] = i
        return poster_name


def get_post_by_pk(pk):
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
        for i in posts:
            if i['pk'] == pk:
                return i
    return {}


def get_post_by_name(name):
    user_posts = []
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
        for i in posts:
            if i['poster_name'] == name:
                user_posts.append(i)
    return user_posts



def find_post_by_tag(tag):
    user_posts = []
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
        for i in posts:
            if tag in i['content']:
                user_posts.append(i)
    return user_posts


def get_comments_by_post_id(post_id):
    post_comment = []

    with open(COMMENT_PATH, 'r', encoding='utf-8') as file:
        comments = json.load(file)
        for i in comments:
            if i['post_id'] == post_id:
                post_comment.append(i)
    return post_comment
