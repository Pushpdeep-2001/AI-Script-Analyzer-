from pydantic import BaseModel, Field
from typing import List, Optional

class SummaryResponse(BaseModel):
    summary: str

class EmotionResponse(BaseModel):
    dominant_emotions: List[str]
    emotional_arc: str

class EngagementResponse(BaseModel):
    score: int = Field(..., ge=1, le=10)
    factors: List[str]

class OptimizationResponse(BaseModel):
    improvements: List[str]

class CliffhangerResponse(BaseModel):
    moment: str
    reason: str

class ScriptAnalysisResponse(BaseModel):
    summary: str
    emotions: EmotionResponse
    engagement: EngagementResponse
    improvements: List[str]
    cliffhanger: Optional[CliffhangerResponse] = None

class ScriptRequest(BaseModel):
    script: str
