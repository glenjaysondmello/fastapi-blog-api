from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data": {"data" : "hey"}}

@app.get('/about')
def about():
    return {"data": "about"}