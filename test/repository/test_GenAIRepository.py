import pytest
from app.repository.GenAIRepository import GenAIRepository
from app.common.HttpClient import http_client


def test_get_embeddings_from_db(mocker):
    # Arrange
    expected_response = None
    mocker.patch.object(http_client, 'post', return_value=expected_response)
    genAIRepository = GenAIRepository()

    # Act
    response = genAIRepository.get_embeddings_from_db()

    # Assert
    http_client.post.assert_called_once_with("https://httpbin.org/get")
    assert response == expected_response
