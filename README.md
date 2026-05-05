# Pulse by Pixii

**AI Shelf Score** — Know if ChatGPT and Gemini would recommend your Amazon product.

Built as a take-home project for Pixii.ai.

## What it does

Paste a shopper query (e.g. "best magnesium supplement for seniors") and your product name.
Pulse fires that query at GPT-4o and Gemini simultaneously, checks if your product appears
in their recommendations, scores your AI visibility, and tells you exactly who's winning instead.

## The problem it solves

Pixii makes listings look great. But if AI engines like ChatGPT aren't recommending your
product when shoppers ask, beautiful images don't matter. Pulse closes that gap.

## Tech stack

- **Backend**: Python + Flask
- **APIs**: OpenAI GPT-4o, Google Gemini 1.5 Flash
- **Frontend**: HTML, CSS, Vanilla JS
- **Deployment**: Railway

## How to run locally

### 1. Clone the repo
git clone https://github.com/devikashivegowda/pulse-by-pixii.git
cd pulse-by-pixii

### 2. Install dependencies
pip install -r requirements.txt

### 3. Add your API keys
Create a `.env` file in the root:
OPENAI_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here

### 4. Run
python main.py

Open http://localhost:5000

## APIs used
- OpenAI GPT-4o
- Google Gemini 1.5 Flash

## Built by
Devika S — Final year CS (Cybersecurity), CGPA 8.9