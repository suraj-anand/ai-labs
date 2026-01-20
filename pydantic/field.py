from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., min_length=5)
    age: int = Field(..., ge=18)
    
# u1 = User(name="hey", age=18) # invalid name
# u2 = User(name="hey123", age=-1) # invalid age
u3 = User(name="hey123", age=18) # valid