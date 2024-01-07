from pydantic import BaseModel, Field, HttpUrl

class Image(BaseModel):
    url : HttpUrl = Field(title="URL of Image")
    name : str = Field(title="Name of the Image", min_length=5, max_length=20)
    
class Item(BaseModel):
    name : str = Field(description="Name of Item", min_length=5, max_length=50)
    description : str | None = Field(default=None,description="Description of the Item", max_length=300)
    price : float = Field(gt=0, description="Price of the Item")
    tax : float | None = Field(default=None, ge=0, description="Applied Tax for the Item")
    image : Image | None = None