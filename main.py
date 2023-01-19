from fastapi import Depends, FastAPI,Response,status,HTTPException,APIRouter

app = FastAPI()

@app.get("/")
def getData():
    return {"message" : "hello world"}