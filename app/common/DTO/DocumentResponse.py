from pydantic import BaseModel
from .BaseResponse import BaseResponse
from typing import List


class DocumentResponse(BaseResponse):
    doc_text: List[str]

    def to_dict(self):
        return self.dict()
