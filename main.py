import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="PDF Q&A with LangChain and FastAPI",
    description="Upload a PDF, generate questions, and get answers.",
    version="1.0.0",
)
@app.get("/")
async def root():
    return {"message": "Welcome to the PDF Q&A API."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)