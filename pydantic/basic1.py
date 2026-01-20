from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    age: int
    
data = {
    # "user": "suraj", # Errors out since user is not in User BaseModel
    "username": "suraj",
    "email": "suraj02anand@gmail.com",
    "age": 24
}
user1 = User(**data)
print(user1.username)
print(user1.email)

# way 2 of create
user2 = User(username="hey", email="hey@gmail.com", age=24)
print(user2)