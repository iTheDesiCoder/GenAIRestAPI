from app.common.DTO import EmbeddingRequest
from app.common.Logging import logger
from app.common.HttpClient import http_client


class GenAIRepository:

    def get_embeddings_from_db(self):
        response = http_client.post("https://httpbin.org/get")
