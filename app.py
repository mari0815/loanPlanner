from flask import Flask, request, jsonify
import json, os

app = Flask(__name__, static_folder="static", static_url_path="")
os.makedirs('/app/data', exist_ok=True)

DATA_FILE = "/app/data/plan.json"

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/api/plan", methods=["GET"])
def get_plan():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify({"exists": False}), 200

@app.route("/api/plan", methods=["PUT"])
def save_plan():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "no JSON body"}), 400
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return jsonify({"ok": True})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
