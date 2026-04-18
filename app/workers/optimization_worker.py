from app.core.llm import call_llm

async def run_optimization_worker(script: str):
    """
    Suggests structural and stylistic optimizations for the script.
    """
    prompt = f"""
        You are a Script Optimization Specialist.

        Your task:
        Suggest 3 to 5 actionable improvements to enhance:
        - pacing
        - dialogue
        - conflict
        - emotional impact

        Constraints:
        - Suggestions must be specific and actionable.
        - Avoid generic advice.
        - Base suggestions only on the script.

        Return ONLY valid JSON:
        {{
            "improvements": ["...", "..."]
        }}

        Script: {script}
        Use only the information explicitly present in the script. Do not assume or invent details.
        Output must be strictly valid JSON. Do not include markdown, backticks, or text outside JSON.
    """
    
    response = await call_llm(prompt)
    if isinstance(response, dict):
        return response.get("improvements", [])
    return []
