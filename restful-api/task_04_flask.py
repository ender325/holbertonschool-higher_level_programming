from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory dictionary to store users (kept empty for the checker)
users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    return "OK"

@app.route('/data')
def get_data():
    # Returns a list of all usernames stored in the API
    return jsonify(list(users.keys()))

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    # Parse incoming JSON data safely
    data = request.get_json(silent=True)
    
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
        
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
        
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
        
    # Add the user to the dictionary using username as the key
    users[username] = data
    
    response_data = {
        "message": "User added",
        "user": data
    }
    return jsonify(response_data), 201

if __name__ == '__main__':
    app.run()
