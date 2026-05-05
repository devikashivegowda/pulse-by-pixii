from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
from services.openai_service import query_openai
from services.gemini_service import query_gemini
from services.parser import extract_products
from services.scorer import compute_visibility
from services.insights import generate_insights

import os



app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    query = data.get("query")
    product_name = data.get("product_name")

    gpt = extract_products(query_openai(query))
    gemini = extract_products(query_gemini(query))

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

if __name__ == "__main__":
    app.run(debug=True)