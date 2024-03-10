import pytest
from unittest.mock import Mock
from app.manager.GenAIManager import GenAIManager
from app.repository import GenAIRepository, OpenAIRepository
from app.common.DTO import CompletionRequest, CompletionResponse


def test_get_annuity_completion(mocker):
    # Arrange
    mock_openai_repo = mocker.patch.object(OpenAIRepository, 'get_openai_completion')
    mock_openai_repo.return_value = Mock(spec=CompletionResponse)
    mock_genai_repo = mocker.patch.object(GenAIRepository, 'get_embeddings_from_db')
    mock_completion_request = mocker.patch.object(CompletionRequest, '__init__', return_value=None)
    genAIManager = GenAIManager()

    # Act
    response = genAIManager.get_annuity_completion(mock_completion_request)

    # Assert
    assert isinstance(response, CompletionResponse)
    mock_openai_repo.assert_called_once()
    mock_genai_repo.assert_called_once()
