from pydantic import BaseModel


class DocumentRequest(BaseModel):
    base64_pdf: str

    def to_dict(self):
        return self.dict()
