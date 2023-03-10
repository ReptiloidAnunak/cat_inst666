from flask import Flask, send_from_directory
from main.main_view import main_blueprint
from loader.loader_view import loader_blueprint


UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

app.run(debug=True)

