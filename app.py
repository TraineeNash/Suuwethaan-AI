from google import genai
from flask import Flask,request,jsonify
from flask import send_from_directory
import os
from flask_cors import CORS
app = Flask(__name__)

CORS(app,resources={r"/*": {"origins": "*"}})
client = genai.Client(api_key="AQ.Ab8RN6I5C4yJMo9izH_L4PfiRkN3MaJT34kjHAuBOQohT5Pd8g")

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    if os.path.exists(path):
        return send_from_directory('.', path)
    return "Not found", 404

@app.route("/summary",methods=["POST"])
def summary():
    data = request.get_json()
    user_input = data.get("text")
    print("Received text:", user_input)
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=("Give a summary of this input:", user_input)
    )
    print("AI:", response.text)
    return jsonify({"summary": response.text})
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
