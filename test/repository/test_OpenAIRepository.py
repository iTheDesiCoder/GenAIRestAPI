import pytest
from unittest.mock import Mock
from app.repository.OpenAIRepository import OpenAIRepository
from app.common.DTO import CompletionRequest, CompletionResponse
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


def test_get_openai_completion(mocker):
    # Arrange
    mock_chat = mocker.patch.object(ChatOpenAI, 'invoke')
    mock_chat.return_value = Mock(content="Test content")
    mock_completion_request = mocker.patch.object(CompletionRequest, '__init__', return_value=None)
    mock_system_message = mocker.patch.object(SystemMessage, '__init__', return_value=None)
    openAIRepository = OpenAIRepository()

    # Act
    response = openAIRepository.get_openai_completion(mock_completion_request, mock_system_message)

    # Assert
    assert isinstance(response, CompletionResponse)
    assert response.completion_content == "Test content"
