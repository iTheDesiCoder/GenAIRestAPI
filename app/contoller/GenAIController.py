from fastapi import APIRouter, Depends
from app.manager import GenAIManager
from app.common.DTO import CompletionRequest, CompletionResponse
from app.common.Logging import logger

genai_router = APIRouter()


class GenAIController:

    @genai_router.post("/get_annuity_completion", status_code=200, response_model=CompletionResponse)
    async def get_annuity_completion(completion_request: CompletionRequest) -> CompletionResponse:
        logger.debug(f"Request received for get_annuity_completion: {completion_request}")
        genai_manager = GenAIManager()
        completion_response = genai_manager.get_annuity_completion(completion_request)
        logger.debug(f"Response for get_annuity_completion: {completion_response}")
        return completion_response
