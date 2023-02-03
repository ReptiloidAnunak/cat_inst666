import json, flask, logging
POST_PATH = "posts.json"

def load_posts_base(path=POST_PATH):
    try:
        with open(path, "r") as file:
                actual_base = json.load(file)
        return actual_base

    except FileNotFoundError:
        print("Файл posts.json отсутствует или не хочет превращаться в список")
        return None



def search_by_tag(word):
    posts_base = load_posts_base()
    word = str(word).strip().lower()
    relevant_posts_list = []
    for post in posts_base:
        if word in post["content"]:
            relevant_posts_list.append(post)
    return relevant_posts_list

def save_new_picture(picture):
    picture_name = picture.filename
    picture_savepath = f"uploads/images/{picture_name}"
    picture.save(picture_savepath)
    return picture_savepath

def format_post(picture_path, text):
    formatted_post = {"pic": picture_path, "content": text}
    return formatted_post


def save_renew_base(posts):
    with open ("posts.json", "w") as file:
        json.dump(posts, file, ensure_ascii=False)



def load_post_to_base(post):
    with open("posts.json", "r") as file:
        base = json.load(file)
        base.append(post)
        save_renew_base(base)
    return base

