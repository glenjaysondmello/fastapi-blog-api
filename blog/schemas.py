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