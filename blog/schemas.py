from pydantic import BaseModel

class Blog(BaseModel):
    # id: int
    title: str
    body: str

class ShowBlog(Blog):
    # class Config():
    #     orm_mode = True
    model_config = {"from_attributes": True}

# class ShowBlog(BaseModel):
#     title: str
#     class Config():
#         orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    
    model_config = {"from_attributes": True}