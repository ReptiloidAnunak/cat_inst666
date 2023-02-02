from flask import request, render_template, Blueprint
from functions import save_new_picture, format_post, load_post_to_base, save_renew_base
import logging

loader_blueprint = Blueprint("loader_blueprint", __name__)
@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    return render_template("post_form.html")

@loader_blueprint.route("/post_upload", methods=["POST"])
def page_post_upload():
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    user_picture = request.files.get("picture")
    user_picture_extension = user_picture.filename.split('.')[-1]

    if not user_picture:
        return 'Ошибка загрузки'
    elif user_picture_extension not in ALLOWED_EXTENSIONS:
        return 'Файл - не изображение!'

    user_text = request.form.get("content")
    picture_path = save_new_picture(user_picture)

    post_to_load = format_post(picture_path, user_text)
    uploaded_posts = load_post_to_base(post_to_load)
    save_renew_base(uploaded_posts)
    return render_template("post_uploaded.html", user_text=user_text, picture_path=picture_path)