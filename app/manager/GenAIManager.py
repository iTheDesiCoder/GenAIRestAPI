from app.repository import GenAIRepository, OpenAIRepository
from app.common.DTO import CompletionRequest, CompletionResponse, DocumentRequest, DocumentResponse
import base64
import io
from PyPDF2 import PdfFileReader, PdfReader


class GenAIManager:
    def get_annuity_completion(self, completion_request: CompletionRequest) -> CompletionResponse:
        system_message: str = "You are a helpful Annuity sales assistant who is always available to answer questions about the Annuity to Financial Advisor. You are knowledgeable about the annuity and can explain fees, expense, benfits and funds detail to financial advisor."
        openai_repository = OpenAIRepository()
        completion_response = openai_repository.get_openai_completion(completion_request, system_message)
        return completion_response

    def get_annuity_assistant(self, completion_request: CompletionRequest) -> CompletionResponse:
        openai_repository = OpenAIRepository()
        completion_response = openai_repository.get_openai_assistant(completion_request)
        return completion_response

    def process_doc(self, doc_request: DocumentRequest) -> DocumentResponse:
        # Decode the base64 string
        decoded_pdf = base64.b64decode(doc_request.base64_pdf)

        # Convert the decoded string to a BytesIO object
        pdf_io = io.BytesIO(decoded_pdf)

        # Use PyPDF2 to read the PDF
        pdf_reader = PdfReader(pdf_io)

        # Extract the text from the PDF
        pages_text = [page.extract_text() for page in pdf_reader.pages]

        response = DocumentResponse(status=True, doc_text=pages_text)
        return response
