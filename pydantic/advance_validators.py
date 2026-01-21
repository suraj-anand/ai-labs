from pydantic import BaseModel, field_validator

class User(BaseModel):
    firstname: str
    lastname: str
    
    @field_validator('firstname', 'lastname')
    def all_lower(cls, v: str):
        for ch in v:
            if not ch.islower():
                raise ValueError("Not a lower")
        return v
                
        
    

# u0 = User(firstname="suraAj", lastname='a') # invalid
u1 = User(firstname="suraj", lastname='a')
print(u1.model_dump())