from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from view.QueryApi import query

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(query)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
