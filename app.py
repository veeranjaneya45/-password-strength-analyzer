from flask import Flask, render_template, request, jsonify, session
import re
import random
import string
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = "thiranex_secure_key_2026"

def analyze_password(password):
    score = 0
    feedback = []
    details = {}

    # Length check
    details['length'] = len(password)
    if len(password) >= 12:
        score += 2
        details['length_ok'] = True
    elif len(password) >= 8:
        score += 1
        details['length_ok'] = True
    else:
        details['length_ok'] = False
        feedback.append("Use at least 8 characters (12+ recommended)")

    # Uppercase
    details['has_upper'] = bool(re.search(r'[A-Z]', password))
    if details['has_upper']:
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z)")

    # Lowercase
    details['has_lower'] = bool(re.search(r'[a-z]', password))
    if details['has_lower']:
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z)")

    # Numbers
    details['has_number'] = bool(re.search(r'[0-9]', password))
    if details['has_number']:
        score += 1
    else:
        feedback.append("Add at least one number (0-9)")

    # Symbols
    details['has_symbol'] = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    if details['has_symbol']:
        score += 2
    else:
        feedback.append("Add special characters like @, #, $, !")

    # Common passwords
    common = ["password", "123456", "password123", "admin", "qwerty", "letmein"]
    if password.lower() in common:
        score = 0
        feedback = ["This is one of the most common passwords ever! Change it immediately."]

    return score, feedback, details

def get_strength(score):
    if score <= 1:
        return {"label": "Weak", "color": "#ef4444", "percent": 15}
    elif score <= 3:
        return {"label": "Moderate", "color": "#f97316", "percent": 45}
    elif score <= 5:
        return {"label": "Strong", "color": "#eab308", "percent": 75}
    else:
        return {"label": "Very Strong", "color": "#22c55e", "percent": 100}

def generate_password(length=14):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    while True:
        pwd = ''.join(random.choice(chars) for _ in range(length))
        score, _, _ = analyze_password(pwd)
        if score >= 6:
            return pwd

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    password = data.get('password', '')

    if not password:
        return jsonify({'error': 'No password provided'}), 400

    score, feedback, details = analyze_password(password)
    strength = get_strength(score)

    result = {
        'score': score,
        'max_score': 7,
        'strength': strength,
        'feedback': feedback,
        'details': details,
        'timestamp': datetime.now().strftime("%d %b %Y, %I:%M %p")
    }

    # Save to session history
    if 'history' not in session:
        session['history'] = []

    history_entry = {
        'masked': '*' * len(password),
        'length': len(password),
        'strength': strength['label'],
        'color': strength['color'],
        'score': score,
        'timestamp': result['timestamp']
    }

    session['history'] = [history_entry] + session['history'][:9]  # Keep last 10
    session.modified = True

    return jsonify(result)

@app.route('/generate', methods=['GET'])
def generate():
    password = generate_password()
    score, _, _ = analyze_password(password)
    strength = get_strength(score)
    return jsonify({'password': password, 'strength': strength})

@app.route('/history', methods=['GET'])
def history():
    return jsonify(session.get('history', []))

@app.route('/clear-history', methods=['POST'])
def clear_history():
    session['history'] = []
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)