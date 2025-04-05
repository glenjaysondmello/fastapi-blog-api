from pydantic import BaseModel
from typing import List
from typing import Optional 

class BlogBase(BaseModel):
    # id: int
    title: str
    body: str

class Blog(BlogBase):
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

class ShowUserWithBlogs(ShowUser):
    blogs: List["Blog"]
    


# class ShowBlog(Blog):
    # class Config():
    #     orm_mode = True
    # creator: ShowUser

class ShowBlog(Blog):
    creator: ShowUser

    model_config = {"from_attributes": True}
    

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
     email: Optional[str] = None



    