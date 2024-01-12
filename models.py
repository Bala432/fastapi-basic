from pydantic import BaseModel, Field

class Blog(BaseModel):
    title = Field(str, min_length=5, max_length=50)
    body  = Field(str, min_length=30, max_length=300)