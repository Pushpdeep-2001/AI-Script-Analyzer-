from app.core.llm import call_llm

async def run_cliffhanger_worker(script: str):
    """ Identifies or suggests potential cliffhanger moments in the script. """
    
    prompt = f"""
        You are a Suspense and Cliffhanger Analyst.

        Your task:
        1. Identify the most suspenseful or impactful moment in the script.
        2. Explain why it works.

        Constraints:
        - If no clear cliffhanger exists, choose the most emotionally intense moment.
        - Keep explanation concise (1–2 lines).
        - Do not invent events not present in the script.
        - If no meaningful cliffhanger exists, explicitly state that the script lacks a strong suspenseful moment.

        Return ONLY valid JSON:
        {{
            "moment": "Description of the ending moment",
            "reason": "Why this works as a cliffhanger"
        }}

        Script: {script}
        Use only the information explicitly present in the script. Do not assume or invent details. 
        Output must be strictly valid JSON. Do not include markdown, backticks, or text outside JSON.
    """
    
    response = await call_llm(prompt)
    if isinstance(response, dict):
        return {
            "moment": response.get("moment", "N/A"),
            "reason": response.get("reason", "N/A")
        }
    return {"moment": "N/A", "reason": "N/A"}
