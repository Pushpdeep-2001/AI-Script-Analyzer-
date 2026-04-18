from app.core.llm import call_llm

async def run_engagement_worker(script: str):
    """ Evaluates script engagement and viral potential. """

    prompt = f"""
        You are an Engagement Evaluator.

        Your task:
        1. Give an engagement score from 1 to 10.
        2. Identify 3–5 key factors influencing the score.

        Evaluation factors may include:
        - strength of opening hook
        - character conflict
        - emotional depth
        - tension or suspense
        - presence of a cliffhanger

        Constraints:
        - Score must be an integer between 1 and 10.
        - Factors must be short and specific.
        - Do not repeat the same idea.

        Return ONLY valid JSON:
        {{
            "score": 8,
            "factors": ["...", "..."]
        }}

        Script: {script}
        Use only the information explicitly present in the script. Do not assume or invent details.
        Output must be strictly valid JSON. Do not include markdown, backticks, or text outside JSON.
    """
    
    response = await call_llm(prompt)
    if isinstance(response, dict):
        return {
            "score": int(response.get("score", 5)),
            "factors": response.get("factors", [])
        }
    return {"score": 0, "factors": []}
