from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

# Load events data
def load_events():
    with open('data/events.json') as f:
        return json.load(f)

# Route: Main Page
@app.route('/')
def index():
    return render_template('index.html')

# Route: Fetch Events (for infinite scrolling)
@app.route('/api/events')
def get_events():
    page = int(request.args.get('page', 1))
    per_page = 5
    events = load_events()
    start = (page - 1) * per_page
    end = start + per_page
    return jsonify(events[start:end])

if __name__ == '__main__':
    app.run(debug=True)
