from pydantic import BaseModel, computed_field

class User(BaseModel):
    username: str
    
    @computed_field
    # @property
    def email(self) -> str:
        return f"{self.username}@user.com"
    

u1 = User(username="suraj")
print(u1.model_dump())