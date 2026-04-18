from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AnalysisRequest(BaseModel):
    text: str

@router.post("/analyze")
async def analyze_script(request: AnalysisRequest):
    # This is a placeholder for the actual analysis logic
    input_text = request.text
    
    # Simple response for testing
    return {
        "status": "success",
        "message": "Script received successfully",
        "word_count": len(input_text.split()),
        "character_count": len(input_text),
        "preview": input_text[:100] + "..." if len(input_text) > 100 else input_text
    }
