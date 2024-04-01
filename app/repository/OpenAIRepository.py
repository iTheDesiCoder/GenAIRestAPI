from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from app.config import OPENAI_API_KEY
from app.common.DTO import CompletionRequest
from app.common.DTO import CompletionResponse


class OpenAIRepository:
    def __init__(self):
        self.chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-4-turbo-preview")

    def get_openai_completion(self, completion_request: CompletionRequest, system_message: str) -> CompletionResponse:
        messages = [HumanMessage(content=completion_request.query + "\n\r " + completion_request.context),
                    SystemMessage(content=system_message)]
        chat_response = self.chat.invoke(messages)
        completion_response = CompletionResponse(status=True, completion_content=chat_response.content)
        return completion_response
