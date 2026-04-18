from app.core.llm import call_llm

async def run_summary_worker(script: str):
    """
    Generates a concise summary of the script.
    """
    prompt = f"""
        You are a Story Summarizer.

        Your task:
        - Summarize the script in 3 to 4 lines only.
        - Capture the core plot, main characters, and key conflict.
        - Capture not just events, but also the underlying tone or tension of the story.
        - Do not add interpretation beyond what is present.

        Constraints:
        - Keep it concise and clear.
        - No extra commentary.

        Return ONLY valid JSON:
        {{
            "summary": "..."
        }}

        Script:{script}
        Use only the information explicitly present in the script. Do not assume or invent details.
        Output must be strictly valid JSON. Do not include markdown, backticks, or text outside JSON.
    """
    
    response = await call_llm(prompt)
    if isinstance(response, dict):
        return response.get("summary", "")
    return ""