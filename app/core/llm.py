import os
import json
from groq import AsyncGroq
from app.config import settings
from app.services.logger import app_logger as logger

class LLMService:
    """Class to handle interactions with the Groq LLM API."""
    
    def __init__(self):
        self.client = AsyncGroq(
            api_key=settings.GROQ_API_KEY,
        )
        self.model = settings.MODEL
        self.temperature=0.3
        self.system_prompt = "You are an expert script analyst. Focus only on events explicitly present. Maintain consistency across analysis. You must return strictly valid JSON. Do not include any explanation outside JSON. Base your analysis only on the provided script. Do not hallucinate missing details."

    async def get_response(self, prompt: str) -> str:
        """
        Calls the LLM asynchronously with a system and user prompt.
        """
        try:
            chat_completion = await self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model,
                temperature=self.temperature,
                response_format={"type": "json_object"} if "JSON" in prompt else None
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            logger.error(f"LLM Call Error: {str(e)}")
            return json.dumps({"error": str(e)})

# Create a singleton instance
llm_client = LLMService()

# Export call_llm directly for convenience
async def call_llm(prompt: str):
    response_text = await llm_client.get_response(prompt)
    try:
        # Try to parse as JSON if possible
        return json.loads(response_text)
    except json.JSONDecodeError:
        return response_text
