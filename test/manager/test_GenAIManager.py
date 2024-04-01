import pytest
from unittest.mock import Mock
from app.manager.GenAIManager import GenAIManager
from app.repository import GenAIRepository, OpenAIRepository
from app.common.DTO import CompletionRequest, CompletionResponse,DocumentRequest, DocumentResponse
import base64

def test_get_annuity_completion(mocker):
    # Arrange
    mock_openai_repo = mocker.patch.object(OpenAIRepository, 'get_openai_completion')
    mock_openai_repo.return_value = Mock(spec=CompletionResponse)
    mock_completion_request = mocker.patch.object(CompletionRequest, '__init__', return_value=None)
    genAIManager = GenAIManager()

    # Act
    response = genAIManager.get_annuity_completion(mock_completion_request)

    # Assert
    assert isinstance(response, CompletionResponse)
    mock_openai_repo.assert_called_once()

    def test_process_doc(self, mocker):
        # Arrange
        mock_pdf_reader = mocker.patch('PyPDF2.PdfReader')
        mock_pdf_reader.return_value.pages = [{'extract_text': lambda: 'Test text'}]
        doc_request = DocumentRequest(base64_pdf=base64.b64encode(b'Test pdf').decode('utf-8'))

        # Act
        response = self.genai_manager.process_doc(doc_request)

        # Assert
        assert isinstance(response, DocumentResponse)
        assert response.doc_text == 'Test text'