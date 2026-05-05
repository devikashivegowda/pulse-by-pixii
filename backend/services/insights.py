def generate_insights(results):
    insights = []
    keywords = []

    # Collect all reasons
    for model in results:
        for item in results[model]:
            keywords.append(item.get("reason", "").lower())

    combined = " ".join(keywords)

    # Basic pattern insights
    if "sleep" in combined:
        insights.append("Competitors highlight sleep benefits")

    if "doctor" in combined:
        insights.append("Authority signals like doctor recommendation are used")

    if "absorption" in combined:
        insights.append("High absorption is a key selling point")

    # Fallback insight
    if len(insights) == 0:
        insights.append("No strong differentiation found among competitors")

    return insights