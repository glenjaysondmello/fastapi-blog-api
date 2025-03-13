from pydantic import BaseModel

class Blog(BaseModel):
    # id: int
    title: str
    body: str

class ShowBlog(Blog):
    class Config():
        orm_mode = True

# class ShowBlog(BaseModel):
#     title: str
#     class Config():
#         orm_mode = True