import uuid
from flask import Flask, request, jsonify
import requests
from torch.utils.tensorboard import SummaryWriter

# --- SDK Implementation ---
class SessionIQSDK:
    def __init__(self, api_base_url, api_key=None):
        self.api_base_url = api_base_url
        self.api_key = api_key
        self.session_token = None

    def authenticate(self, username, password):
        """Authenticate the user and store the session token."""
        auth_url = f"{self.api_base_url}/authenticate"
        response = requests.post(auth_url, json={"username": username, "password": password})
        if response.status_code == 200:
            self.session_token = response.json().get("session_token")
            print(f"Authenticated successfully. Session Token: {self.session_token}")
        else:
            print("Authentication failed.")
            return None

    def create_session(self, user_id, session_data):
        """Create a new session for the user."""
        if not self.session_token:
            raise Exception("User is not authenticated.")
        session_url = f"{self.api_base_url}/sessions"
        headers = {"Authorization": f"Bearer {self.session_token}"}
        response = requests.post(session_url, json={"user_id": user_id, "data": session_data}, headers=headers)
        if response.status_code == 201:
            print("Session created successfully.")
        else:
            print(f"Failed to create session. Error: {response.text}")

    def get_session(self, session_id):
        """Fetch session details using session_id."""
        if not self.session_token:
            raise Exception("User is not authenticated.")
        session_url = f"{self.api_base_url}/sessions/{session_id}"
        headers = {"Authorization": f"Bearer {self.session_token}"}
        response = requests.get(session_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch session. Error: {response.text}")
            return None

    def analyze_session(self, session_id):
        """Analyze session data and return insights."""
        if not self.session_token:
            raise Exception("User is not authenticated.")
        analysis_url = f"{self.api_base_url}/sessions/{session_id}/analyze"
        headers = {"Authorization": f"Bearer {self.session_token}"}
        response = requests.get(analysis_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to analyze session. Error: {response.text}")
            return None


# --- Cloud API Implementation ---
app = Flask(__name__)

# Mocked database
users_db = {}
sessions_db = {}

# TensorBoard writer initialization
writer = SummaryWriter(log_dir='./runs')


@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # Basic authentication logic (mocked for now)
    if username == "admin" and password == "password":
        session_token = str(uuid.uuid4())
        return jsonify({"session_token": session_token}), 200
    return jsonify({"message": "Invalid credentials"}), 400


@app.route('/sessions', methods=['POST'])
def create_session():
    data = request.get_json()
    user_id = data.get('user_id')
    session_data = data.get('data')
    session_id = str(uuid.uuid4())
    sessions_db[session_id] = {"user_id": user_id, "data": session_data}
    return jsonify({"session_id": session_id}), 201


@app.route('/sessions/<session_id>', methods=['GET'])
def get_session(session_id):
    session = sessions_db.get(session_id)
    if session:
        return jsonify(session), 200
    return jsonify({"message": "Session not found"}), 404


@app.route('/sessions/<session_id>', methods=['PUT'])
def edit_session(session_id):
    session = sessions_db.get(session_id)
    if session:
        data = request.get_json()
        session["data"] = data.get("data", session["data"])  # Edit session data
        return jsonify({"message": "Session updated successfully.", "session": session}), 200
    return jsonify({"message": "Session not found."}), 404


@app.route('/sessions/<session_id>', methods=['DELETE'])
def delete_session(session_id):
    if session_id in sessions_db:
        del sessions_db[session_id]
        return jsonify({"message": "Session deleted successfully."}), 200
    return jsonify({"message": "Session not found."}), 404


@app.route('/sessions/<session_id>/analyze', methods=['GET'])
def analyze_session(session_id):
    session = sessions_db.get(session_id)
    if session:
        # Enhanced analysis based on session data
        activity = session.get("data").get("activity", "unknown")
        user_id = session.get("user_id")
        
        analysis = {}
        
        if activity == "sports":
            analysis["insight"] = "User spent a lot of time on sports activity."
            analysis["duration"] = "1 hour 30 minutes"  # Mock data: Replace with actual logic
            analysis["frequent_activity"] = True  # Mock data: Replace with actual logic
        elif activity == "study":
            analysis["insight"] = "User spent a significant amount of time studying."
            analysis["duration"] = "2 hours"
            analysis["frequent_activity"] = False
        else:
            analysis["insight"] = "User engaged in an unknown activity."
            analysis["duration"] = "30 minutes"
            analysis["frequent_activity"] = False

        # Log insights to TensorBoard
        writer.add_scalar('session/insight', 1 if activity == 'sports' else 0, global_step=1)

        return jsonify(analysis), 200
    return jsonify({"message": "Session not found"}), 404


if __name__ == '__main__':
    print('Available routes:')
    for rule in app.url_map.iter_rules():
        print(f'{rule.endpoint}: {rule}')
    app.run(debug=True)

# In-memory "database" for users
users_db = {}

# Create User (POST /users)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = str(uuid.uuid4())  # Generate a unique user ID
    users_db[user_id] = data
    return jsonify({"user_id": user_id}), 201

# Get User (GET /users/{user_id})
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users_db.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404


# Example in-memory "database" for sessions
sessions_db = {}

# Analytics endpoint (GET /analytics)
@app.route('/analytics', methods=['GET'])
def analytics():
    total_sessions = len(sessions_db)
    avg_duration = sum(session['data'].get('duration', 0) for session in sessions_db.values()) / total_sessions if total_sessions > 0 else 0
    return jsonify({"total_sessions": total_sessions, "avg_duration": avg_duration}), 200


import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Log session creation
@app.route('/sessions', methods=['POST'])
def create_session():
    logging.info(f"Received request to create session: {request.json}")
    # Your existing logic for creating the session
    session_id = str(uuid.uuid4())  # Example session creation logic
    sessions_db[session_id] = request.json
    logging.info(f"Session created with ID: {session_id}")
    return jsonify({"session_id": session_id}), 201


# Store sessions in memory (for simplicity in this example)
sessions_db = {}

# Create Session (POST /sessions)
@app.route('/sessions', methods=['POST'])
def create_session():
    data = request.get_json()
    session_id = str(uuid.uuid4())  # Generate unique session ID
    sessions_db[session_id] = data  # Store session data
    logging.info(f"Session created with ID: {session_id}")
    return jsonify({"session_id": session_id}), 201


# Get Session (GET /sessions/{session_id})
@app.route('/sessions/<session_id>', methods=['GET'])
def get_session(session_id):
    session = sessions_db.get(session_id)
    if session:
        return jsonify(session), 200
    return jsonify({"message": "Session not found"}), 404

