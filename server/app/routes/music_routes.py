from flask import Blueprint

bp = Blueprint("music", __name__, url_prefix="/api/music")

@bp.route("/", methods=["GET"])
def list_music():
    return {"message": "Music route is working"}
