from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from todo import todo_router
import uvicorn
app=FastAPI()
origins=["http://18.209.142.96:5501", "http://18.209.142.96"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/")
async def welcom() -> dict:
    return{
        "msg" :"hello world??????"
    }
app.include_router(todo_router)
if __name__ == '__main__':
    uvicorn.run("main:app",host="0.0.0.0",port=8000, reload=True)