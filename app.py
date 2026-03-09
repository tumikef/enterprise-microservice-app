from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Enterprise DevOps Microservice is Running"}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/users")
def users():
    return {
        "users": [
            {"id":1,"name":"Alice"},
            {"id":2,"name":"Bob"}
        ]
    }
