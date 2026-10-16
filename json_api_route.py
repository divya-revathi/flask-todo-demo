from flask import Flask , jsonify
import json

app = Flask(__name__)

# Path to backend file
DATA_FILE = "data.json"

@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return jsonify(data), 200
    except FileNotFoundError:
        # If file doesn't exist, return empty list
        return jsonify([]), 200
    except Exception as e:
        # Any other error (like bad JSON format)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)