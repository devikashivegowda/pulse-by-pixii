def compute_visibility(product_name, results):
    score = {}

    for model in results:
        score[model] = {"found": False, "rank": None}

        for i, item in enumerate(results[model]):
            if product_name.lower() in item["name"].lower():
                score[model]["found"] = True
                score[model]["rank"] = i + 1

    return score