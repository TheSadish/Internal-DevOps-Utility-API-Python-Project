from fastapi import FastAPI

app = FastAPI() # FastAPI is a class

@app.get("/")  # Route definition
def hello():
    return {"message":"Hello Guys"}

