from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configure a secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-in-production"

jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory user database
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# --- Basic Authentication Verification ---
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

# --- Basic Authentication Protected Route ---
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# --- Login Route for JWT Generation ---
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
        
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
        
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # Embed role inside the JWT token claims
        access_token = create_access_token(
            identity=username, 
            additional_claims={"role": user["role"]}
        )
        return jsonify({"access_token": access_token}), 200
        
    return jsonify({"error": "Bad username or password"}), 401

# --- JWT Protected Route ---
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# --- Role-based Protected Route (Admin Only) ---
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# --- Custom JWT Error Handlers (Ensuring 401 status code) ---
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
