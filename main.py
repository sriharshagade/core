from fastapi import FastAPI

app = FastAPI()

# define endpoint


@app.get("/")
def index():
    return {"data": "Blog List"}


@app.get("/blog/unpublished")
def unpublished():
    # data of all unpublished blogs
    return {"data": {"all unpublished blogs"}}


@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with id = id
    return {"data": {id}}


@app.get("/blog/{id}/comments")
def comments(id):
    # fetch comments of blog with id = id
    return {"data": {'1', '2'}}
