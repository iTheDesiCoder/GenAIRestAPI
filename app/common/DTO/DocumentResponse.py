from pydantic import BaseModel
from .BaseResponse import BaseResponse


class DocumentResponse(BaseResponse):
    doc_text: str

    def to_dict(self):
        return self.dict()
