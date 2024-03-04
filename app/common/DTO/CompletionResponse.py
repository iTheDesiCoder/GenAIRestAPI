from pydantic import BaseModel


class CompletionResponse(BaseModel):
    completion_content: str

    def to_dict(self):
        return self.dict()
