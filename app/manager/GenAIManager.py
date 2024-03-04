from app.repository import GenAIRepository, OpenAIRepository
from app.common.DTO import CompletionRequest, EmbeddingRequest
from app.common.DTO import CompletionResponse


class GenAIManager:
    def get_annuity_completion(self, completion_request: CompletionRequest) -> CompletionResponse:
        system_message: str = "You are a helpful Annuity sales assistant who is always available to answer questions about the Annuity to Financial Advisor. You are knowledgeable about the annuity and can explain fees, expense, benfits and funds detail to financial advisor."
        openai_repository = OpenAIRepository()
        completion_response = openai_repository.get_openai_completion(completion_request, system_message)
        return completion_response
