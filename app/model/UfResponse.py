from pydantic import BaseModel  

# I define a Pydantic model for the JSON response
class UfResponse(BaseModel):  
    date: str
    uf_value: str  
