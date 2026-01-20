from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int
    
    # Custom validator for the field name
    @field_validator("name")
    def name_validator(cls, val):
        if val not in ("suraj"):
            raise ValueError("Invalid User")
        return val
    
# u1 = User(name="hey123", age=18) # invalid name
u2 = User(name="suraj", age=18) # valid name