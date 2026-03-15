def ask_ai(query, model="gpt-4"):
    prompt = f"请分析:{query}"
    rules = ["民法典", "刑法", "劳动法"]
    return prompt, rules
