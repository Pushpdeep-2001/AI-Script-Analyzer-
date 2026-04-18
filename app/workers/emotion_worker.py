from app.core.llm import call_llm

async def run_emotion_worker(script: str):
    """ Analyzes the emotional tone and arc of the script. """

    prompt = f"""
        You are an Emotional Intelligence Analyst.

        Your task:
        1. Identify 2–5 dominant emotions in the script.
        2. Describe how the emotional tone evolves from beginning to end.

        Constraints:
        - Emotions must be single words (e.g., "sadness", "tension", "anger").
        - Emotional arc should be a short progression (e.g., "confusion → tension → relief").
        - Ensure the emotional arc reflects the dominant emotions listed.
        - Consider both explicit and implicit emotions (e.g., guilt, fear, internal conflict).
        - Base only on the script.

        Return ONLY valid JSON:
        {{
            "dominant_emotions": ["emotion1", "emotion2"],
            "emotional_arc": "Brief description of how emotions change through the script. emotional arc reflects the dominant emotions listed"
        }}

        Script: {script}
        Use only the information explicitly present in the script. Do not assume or invent details.
        Output must be strictly valid JSON. Do not include markdown, backticks, or text outside JSON.
    """
    
    response = await call_llm(prompt)
    if isinstance(response, dict):
        return {
            "dominant_emotions": response.get("dominant_emotions", []),
            "emotional_arc": response.get("emotional_arc", "Neutral")
        }
    return {"dominant_emotions": [], "emotional_arc": "Analysis failed"}
