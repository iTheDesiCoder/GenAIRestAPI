from fastapi import APIRouter
from app.manager import GenAIManager
from app.common.DTO import CompletionRequest, CompletionResponse
from typing import List

genai_router = APIRouter()


class GenAIController:
    @genai_router.post("/get_annuity_completion", status_code=200, response_model=CompletionResponse)
    async def get_annuity_completion(completion_request: CompletionRequest) -> CompletionResponse:
        genai_manager = GenAIManager()
        completion_response = genai_manager.get_annuity_completion(completion_request)
        return completion_response
