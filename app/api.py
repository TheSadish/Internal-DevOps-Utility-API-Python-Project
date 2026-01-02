from fastapi import FastAPI
from routers import metrics, bucket_info

app = FastAPI(   # FastAPI is a class
    title="DevOps internal utilities API",
    description="Internal API utilities for which I will adding metrics",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redocs"
) 

@app.get("/")  # Route definition
def hello():
    '''
    This is hello api - testing purpose for docs
    '''
    return {"message":"Hello Guys"}

app.include_router(metrics.router)  # Mounts the router object to FastAPI object
app.include_router(bucket_info.router, prefix="/aws") 