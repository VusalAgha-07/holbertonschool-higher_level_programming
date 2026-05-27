#!/usr/bin/python3
"""
A simple Flask API to manage users.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store users in memory
users = {}


@app.route("/")
def home():
    """Root endpoint greeting."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the user object for a given username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user via a POST request."""
    # Check if the request body is valid JSON
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    # Validation checks
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check for duplicate username with status 409
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user to memory and return 201 status
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
