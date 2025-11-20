from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Function to read data from the JSON file
def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

# Function to save updated data back to the JSON file
def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

# Load the main HTML page
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Create a new passenger (POST)
# -----------------------------
@app.route("/passengers", methods=["POST"])
def add_passenger():
    data = load_data()
    new_passenger = request.json

    # Create a unique ID using timestamp
    new_passenger["id"] = int(__import__("time").time())

    data.append(new_passenger)
    save_data(data)

    return jsonify({
        "message": "Passenger added",
        "passenger": new_passenger
    })


# -----------------------------
# Read all passengers (GET)
# -----------------------------
@app.route("/passengers", methods=["GET"])
def get_passengers():
    data = load_data()
    return jsonify(data)


# -----------------------------
# Update passenger details (PUT)
# -----------------------------
@app.route("/passengers/<int:pid>", methods=["PUT"])
def update_passenger(pid):
    data = load_data()

    # Find passenger by ID
    passenger = next((p for p in data if p["id"] == pid), None)

    if passenger is None:
        return jsonify({"message": "Passenger not found"}), 404

    # Update only the fields sent from the frontend
    updated_data = request.json
    for key, value in updated_data.items():
        passenger[key] = value

    save_data(data)

    return jsonify({
        "message": "Passenger updated",
        "passenger": passenger
    })


# -----------------------------
# Delete passenger (DELETE)
# -----------------------------
@app.route("/passengers/<int:pid>", methods=["DELETE"])
def delete_passenger(pid):
    data = load_data()

    # Remove the passenger with matching ID
    new_data = [p for p in data if p["id"] != pid]

    if len(new_data) == len(data):
        return jsonify({"message": "Passenger not found"}), 404

    save_data(new_data)

    return jsonify({"message": "Passenger deleted"})


# Run the Flask server
if __name__ == "__main__":
    app.run(debug=False)
