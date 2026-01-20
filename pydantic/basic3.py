from pydantic import BaseModel
from typing import List, Union, Optional

class User(BaseModel):
    username: str

class Post(BaseModel):
    id: Union[str, int]
    liked_by: Optional[List[User]] = None
    
userH = User(username="H")
# post1 = Post(id=1, liked_by=[userH]) # valid
post2 = Post(id="two", liked_by=[userH]) # valid
post3 = Post(id=3) # valid
# post4 = Post(id=True, liked_by=[userH]) # invalid
print(post2)