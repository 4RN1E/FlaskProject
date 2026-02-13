from flask import Flask, jsonify, request

app = Flask(__name__)

#Sample data (FIU campus locations with coordinates).
DATA = [
    {"id": 1, "campus": "MMC", "lat": 25.76, "lon": -80.36},
    {"id": 2, "campus": "BBC", "lat": 25.90, "lon": -80.13},
    {"id": 3, "campus": "DC",  "lat": 38.89, "lon": -77.01},
]

@app.route("/index")
def index():
    """
    Home page with API documentation
    Returns HTML with links to available endpoints
    """
    return """
        <h1>FIU CAMPUS API</h1>
        <h2>We give information on FIU campuses</h2>
        <p>Try these endpoints:</p>
        <ul>
            <li><a href="/api/health">/api/health</a></li>
            <li><a href="/api/items">/api/items</a></li>
            <li><a href="/api/item/1">/api/item/1</a></li>
        </ul>
    """

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/api/items")
def get_items():
    return jsonify(DATA), 200

@app.route("/api/item/<int:id>")
def get_item(id):
    for item in DATA:
        if item["id"] == id:
            return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

@app.route("/hello", methods=["GET", "POST"])
def hello():
    """
    Endpoint: /hello
    Methods: GET, POST

    GET: Returns a welcome message
    POST: Accepts JSON with 'name' field and returns personalized greeting
    """
    if request.method == "GET":
        return jsonify({
            "message": "Hello, World!",
            "status": "success"
        }), 200
    elif request.method == "POST":
        # Get JSON data from request body
        data = request.get_json()

        # Validate input
        if not data or 'name' not in data:
            return jsonify({"error": "Please provide 'name' in JSON body"}), 400

        # Return personalized greeting
        return jsonify({
            "message": f"Hello, {data['name']}!",
            "status": "success"
        }), 201

@app.route("/data", methods=["GET", "POST"])
def data():
    """
    Endpoint: /data
    Methods: GET, POST

    GET: Returns all campus data
    POST: Adds new campus to the dataset
    """
    if request.method == "GET":
        return jsonify({
            "status": "success",
            "count": len(DATA),
            "data": DATA
        }), 200
    elif request.method == "POST":
        # Get JSON data from request body
        new_item = request.get_json()

        # Validate input
        if not new_item:
            return jsonify({"error": "Invalid data"}), 400

        # Generate new ID (in production, database would handle this)
        new_id = max([item["id"] for item in DATA]) + 1
        new_item["id"] = new_id

        # Add to data store
        DATA.append(new_item)
        return jsonify({
            "status": "success",
            "data": new_item
        }), 201

if __name__ == "__main__":
    # Run Flask app in debug mode on port 5050
    # Debug mode enables auto-reload and detailed error messages
    # Only use debug=True in development, not production
    app.run(port = 5050, debug=True)
