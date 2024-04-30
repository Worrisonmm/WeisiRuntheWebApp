from flask import Blueprint, render_template, current_app #, session

from app.models.music import Music

music_routes = Blueprint("music_routes", __name__)

@music_routes.route("/musics")
def musics():
    musics = Music.all()
    return render_template("musics.html", musics=musics)