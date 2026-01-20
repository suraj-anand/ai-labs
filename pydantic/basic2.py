from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    age: int
    is_active: bool
    
    
class DUser(BaseModel):
    username: str
    email: str
    age: int
    is_active: bool = False # Default value



data = {
    "username": "suraj",
    "email": "suraj02anand@gmail.com",
    "age": 24,
    # "is_active": 1, # treats as true
    "is_active": True,
}


# Field required [type=missing, input_value={'username': 'suraj', 'em...d@gmail.com', 'age': 24}, input_type=dict]
# data = {
#     "username": "suraj",
#     "email": "suraj02anand@gmail.com",
#     "age": 24,
    # "is_active": 101 # Input should be a valid boolean, unable to interpret input [type=bool_parsing, input_value=101, input_type=int]
# }
user1 = User(**data)


data1 = {
    "username": "suraj",
    "email": "suraj02anand@gmail.com",
    "age": 24,
}
user2 = DUser(**data1)


print(user1)
print(user2)