import pytest
from unittest.mock import Mock
from fastapi.testclient import TestClient
from app.contoller.GenAIController import genai_router
from app.manager.GenAIManager import GenAIManager
from app.common.DTO import CompletionRequest, CompletionResponse


def test_get_annuity_completion(mocker):
    # Arrange
    mock_manager = mocker.patch.object(GenAIManager, 'get_annuity_completion')
    mock_manager.return_value = Mock(spec=CompletionResponse)
    client = TestClient(genai_router)

    # Create a dictionary that represents the data you want to send in the request
    # Make sure this matches the structure and data types of the CompletionRequest object
    request_data = {
        "query": "value1",
        "context": "value2",
        # Add more fields as needed
    }

    # Act
    response = client.post("/get_annuity_completion", json=request_data)

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    mock_manager.assert_called_once()
