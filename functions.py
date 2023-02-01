import json, flask, logging
POST_PATH = "posts.json"

def load_posts_base(path=POST_PATH):
    with open(path, "r") as file:
        actual_base = json.load(file)
        return actual_base

def search_by_tag(word):
    posts_base = load_posts_base()
    word = str(word).strip().lower()
    relevant_posts_list = []
    for post in posts_base:
        if word in post["content"]:
            relevant_posts_list.append(post)
    return relevant_posts_list

