from langchain.agents import AgentExecutor
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from langchain.agents.openai_assistant.base import OpenAIAssistantFinish, OpenAIAssistantAction
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from app.common.DTO import CompletionRequest
from app.common.DTO import CompletionResponse
from app.common.Logging import logger
from app.config import OPENAI_API_KEY, ASSISTANT_ID
from langchain_core.agents import AgentFinish


class OpenAIRepository:
    def __init__(self):
        self.chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-4-turbo-preview")

    def get_openai_completion(self, completion_request: CompletionRequest, system_message: str) -> CompletionResponse:
        messages = [HumanMessage(content=completion_request.query + "\n\r " + completion_request.context),
                    SystemMessage(content=system_message)]
        chat_response = self.chat.invoke(messages)
        completion_response = CompletionResponse(status=True, completion_content=chat_response.content)
        return completion_response

    def get_openai_assistant(self, completion_request: CompletionRequest) -> CompletionResponse:
        interpreter_assistant = OpenAIAssistantRunnable(assistant_id=ASSISTANT_ID, as_agent=True)
        assistant_response = interpreter_assistant.invoke({"content": completion_request.query})
        logger.debug(f"assistant_response: {assistant_response}")
        if isinstance(assistant_response, OpenAIAssistantFinish):
            completion_response = CompletionResponse(status=True,
                                                     completion_content=assistant_response.return_values["output"])
        else:
            completion_response = CompletionResponse(status=False, completion_content="Error in response")
        return completion_response
