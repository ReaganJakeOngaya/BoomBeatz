from flask import Blueprint

bp = Blueprint("playlist", __name__, url_prefix="/api/playlists")

@bp.route("/", methods=["GET"])
def get_playlists():
    return {"message": "Playlist route is working"}
