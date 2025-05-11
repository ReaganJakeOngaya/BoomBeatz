from flask import Blueprint, request, jsonify
from .. import db
from ..models import User
from flask_jwt_extended import create_access_token

bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "User exists"}), 400
    user = User(email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Registered successfully"})

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if user and user.check_password(data["password"]):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

@bp.route("/logout", methods=["POST"])
def logout():
    # In a JWT-based system, logout is typically handled on the client side
    # Invalidate the token (this is a placeholder, actual implementation may vary)
    # You can use a blacklist or simply not store the token
    # JWT tokens are stateless, so you can't "logout" in the traditional sense
    return jsonify({"message": "Logged out successfully"})