from app.repository import GenAIRepository, OpenAIRepository
from app.common.DTO import CompletionRequest, CompletionResponse, DocumentRequest, DocumentResponse
import base64
import io
from PyPDF2 import PdfFileReader, PdfReader
from app.common.DTO import Document

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
        documents = []
        for document in doc_request.documents:
            # Decode the base64 string
            decoded_pdf = base64.b64decode(document.base64_pdf)

            # Convert the decoded string to a BytesIO object
            pdf_io = io.BytesIO(decoded_pdf)

            # Use PyPDF2 to read the PDF
            pdf_reader = PdfReader(pdf_io)

            # Extract the text from each page of the PDF and store it in a list
            pages_text = [page.extract_text() for page in pdf_reader.pages]

            # Create a Document object and append it to the documents list
            documents.append(Document(name=document.name, doc_text=pages_text))

        response = DocumentResponse(status=True, documents=documents)
        return response
