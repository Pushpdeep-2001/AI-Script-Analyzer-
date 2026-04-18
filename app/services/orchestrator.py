import asyncio
import logging
from typing import Dict, Any

from app.services.validator import validate_script
from app.services.context_builder import build_context
from app.services.logger import app_logger as logger
from app.models.schema import ScriptAnalysisResponse
from app.utils.helper import retry_async

# Import all workers
from app.workers.summary_worker import run_summary_worker
from app.workers.emotion_worker import run_emotion_worker
from app.workers.engagement_worker import run_engagement_worker
from app.workers.optimization_worker import run_optimization_worker
from app.workers.cliffhanger_worker import run_cliffhanger_worker

async def execute_workers(script: str) -> list:
    """ Executes all script analysis workers in parallel with retry logic. """
    logger.info(f"Running 5 workers parallely for script: {script[:50]}...")
    
    return await asyncio.gather(
        retry_async(lambda: run_summary_worker(script)),
        retry_async(lambda: run_emotion_worker(script)),
        retry_async(lambda: run_engagement_worker(script)),
        retry_async(lambda: run_optimization_worker(script)),
        retry_async(lambda: run_cliffhanger_worker(script)),
        return_exceptions=True
    )

def format_response(results: list) -> ScriptAnalysisResponse:
    """ 
    Formats raw results into the ScriptAnalysisResponse Pydantic model. 
    Handles potential errors in worker results.
    """
    clean_results = []
    for res in results:
        if isinstance(res, Exception):
            logger.error(f"Worker execution failed: {res}")
            clean_results.append(None)
        else:
            clean_results.append(res)

    return ScriptAnalysisResponse(
        summary=clean_results[0] or "N/A",
        emotions=clean_results[1] or {"dominant_emotions": [], "emotional_arc": "N/A"},
        engagement=clean_results[2] or {"score": 1, "factors": []},
        improvements=clean_results[3] or [],
        cliffhanger=clean_results[4]
    )

async def analyze_script(script: str) -> ScriptAnalysisResponse:
    """ Main orchestration function to validate and analyze a script. """
    try:
        # Validate the script
        validate_script(script)
        
        # Build context (we still use build_context if we need truncated script or extra info)
        context = build_context(script)
        processed_script = context.get('script', script)
        
        # Run workers
        raw_results = await execute_workers(processed_script)
        
        # Format results
        return format_response(raw_results)

    except ValueError as e:
        logger.warning(f"Validation Error: {e}")
        raise e
    except Exception as e:
        logger.error(f"Orchestration Critical Error: {e}", exc_info=True)
        raise e
