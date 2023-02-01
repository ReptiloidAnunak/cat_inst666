from flask import Flask, request, render_template, send_from_directory, Blueprint
from functions import load_posts_base, search_by_tag
import logging

main_blueprint = Blueprint("main_blueprint", __name__)
@main_blueprint.route("/")
def page_index():
    return render_template("index.html")


@main_blueprint.route("/search", methods=["GET"])
def page_tag():
    substring = request.values.get("s")
    posts = search_by_tag(substring)
    return render_template("post_list.html", posts=posts, substring=substring)