from fastapi import APIRouter, HTTPException, Request
from app.services.orchestrator import analyze_script as run_analysis
from app.models.schema import ScriptRequest, ScriptAnalysisResponse
from app.services.logger import app_logger as logger
import time

router = APIRouter()

@router.post("/analyze", response_model=ScriptAnalysisResponse)
async def analyze_script(request: ScriptRequest, raw_request: Request):
    start_time = time.time()
    
    logger.info(f"POST /analyze started - Payload length: {len(request.script)}")
    
    try:
        results = await run_analysis(request.script)
        
        duration = time.time() - start_time
        logger.info(f"POST /analyze success - Duration: {duration:.2f}s")
        return results
        
    except ValueError as e:
        logger.warning(f"POST /analyze validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
        
    except Exception as e:
        logger.error(f"POST /analyze terminal error: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500, 
            detail="An internal error occurred while analyzing the script. Please try again later."
        )
