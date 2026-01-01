# Internal-DevOps-Utility-API-Python-Project
Creating a python project for demonstrating utilities of a webpage


# Asynchronous
- tasks executing independently without waiting for each other, improving efficiency by running background processes

Synchronous Call

@app.get("/data")
def get_data():
    result = slow_db_call()  # 2 seconds
    return result

Asynchronous Call

@app.get("/data")
async def get_data():
    result = await slow_db_call()
    return results

# FastAPI defines the application
# Uvicorn runs the application
- Uvicorn is the ASGI server that loads the FastAPI app object and handles incoming HTTP requests.

# ASGI - ASGI is a standard that defines how a Python web app talks to a web server.
- ASGI is a standard that defines how a Python web app talks to a web server, enabling asynchronous operations.


Services should be kept aside because if they are decorated then 
- You can’t reuse logic easily
- You can’t test it without FastAPI
- You can’t call it from another service
- You can’t run it as a background job