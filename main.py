from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load env FIRST
load_dotenv()

# Import your existing services
from backend.services.openai_service import query_openai
from backend.services.gemini_service import query_gemini
from backend.services.parser import extract_products
from backend.services.scorer import compute_visibility
from backend.services.insights import generate_insights

app = Flask(__name__, static_folder="frontend")
CORS(app)

# -------- SERVE FRONTEND --------

@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("frontend", path)

# -------- BACKEND API --------

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    query = data.get("query")
    product_name = data.get("product_name")

    try:
        gpt_raw = query_openai(query)
    except Exception as e:
        print(f"OpenAI error: {e}")
        gpt_raw = ""

    try:
        gemini_raw = query_gemini(query)
    except:
        gemini_raw = ""

    gpt = extract_products(gpt_raw)
    gemini = extract_products(gemini_raw)

    results = {
        "gpt": gpt,
        "gemini": gemini
    }

    score = compute_visibility(product_name, results)
    insights = generate_insights(results)

    return jsonify({
        "results": results,
        "score": score,
        "insights": insights
    })
 

# -------- RUN --------

if __name__ == "__main__":
    app.run(debug=True)