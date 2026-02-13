from flask import Flask, jsonify, request

app = Flask(__name__)

DATA = [
    {"id": 1, "campus": "MMC", "lat": 25.76, "lon": -80.36},
    {"id": 2, "campus": "BBC", "lat": 25.90, "lon": -80.13},
    {"id": 3, "campus": "DC",  "lat": 38.89, "lon": -77.01},
]

@app.route("/index")
def index():
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
    if request.method == "GET":
        return jsonify({
            "message": "Hello, World!",
            "status": "success"
        }), 200
    elif request.method == "POST":
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({"error": "Please provide 'name' in JSON body"}), 400
        return jsonify({
            "message": f"Hello, {data['name']}!",
            "status": "success"
        }), 201

@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return jsonify({
            "status": "success",
            "count": len(DATA),
            "data": DATA
        }), 200
    elif request.method == "POST":
        new_item = request.get_json()
        if not new_item:
            return jsonify({"error": "Invalid data"}), 400
        new_id = max([item["id"] for item in DATA]) + 1
        new_item["id"] = new_id
        DATA.append(new_item)
        return jsonify({
            "status": "success",
            "data": new_item
        }), 201

if __name__ == "__main__":
    app.run(port = 5050, debug=True)
