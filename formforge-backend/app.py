from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/session/latest')
def latest_session():
    return jsonify({
        "playerName": "John Doe",
        "sessionDate": "2025-05-29"
    })

@app.route('/api/charts/latest')
def latest_charts():
    return jsonify({
        "speed": [5, 7, 6],
        "accuracy": [80, 90, 85]
    })

@app.route('/api/cards/latest')
def latest_cards():
    return jsonify({
        "strength": "Good upper body strength",
        "flexibility": "Needs improvement in hamstrings"
    })

if __name__ == '__main__':
    app.run(port=5001, debug=True)
