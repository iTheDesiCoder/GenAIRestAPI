from fastapi import APIRouter, Depends
from app.manager import GenAIManager
from app.common.DTO import CompletionRequest, CompletionResponse,DocumentRequest, DocumentResponse
from app.common.Logging import logger

genai_router = APIRouter()


class GenAIController:

    @genai_router.post("/get_annuity_completion", status_code=200, response_model=CompletionResponse)
    async def get_annuity_completion(completion_request: CompletionRequest) -> CompletionResponse:
        logger.debug(f"Request received for get_annuity_completion: {completion_request}")
        logger.info(f"Testing INFO log")
        genai_manager = GenAIManager()
        completion_response = genai_manager.get_annuity_completion(completion_request)
        logger.debug(f"Response for get_annuity_completion: {completion_response}")
        return completion_response

    @genai_router.post("/get_annuity_assistant", status_code=200, response_model=CompletionResponse)
    async def get_annuity_completion(completion_request: CompletionRequest) -> CompletionResponse:
        logger.debug(f"Request received for get_annuity_assistant: {completion_request}")
        logger.info(f"Testing INFO log")
        genai_manager = GenAIManager()
        completion_response = genai_manager.get_annuity_assistant(completion_request)
        logger.debug(f"Response for get_annuity_assistant: {completion_response}")
        return completion_response

    @genai_router.post("/process_doc", status_code=200, response_model=DocumentResponse)
    async def process_doc(doc_request: DocumentRequest) -> DocumentResponse:
        logger.debug(f"Request received for get_annuity_completion: {doc_request}")
        genai_manager = GenAIManager()
        doc_response = genai_manager.process_doc(doc_request)
        logger.debug(f"Response for get_annuity_completion: {doc_response}")
        return doc_response