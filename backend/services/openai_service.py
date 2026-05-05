import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def query_openai(query):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = f"""
        What are the best {query}?
        List top 5 products with reasons.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        return response.choices[0].message.content

    except Exception as e:
        print("OpenAI failed, using fallback:", e)

        # 🔁 Dynamic fallback (not static to one product)
        return f"""
        Top {query} products:
        Generic Brand A - popular choice
        Generic Brand B - good reviews
        Generic Brand C - affordable option
        """
    
