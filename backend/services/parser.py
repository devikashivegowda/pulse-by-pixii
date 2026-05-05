import re

def extract_products(data):
    if isinstance(data, list):
        return data

    return []