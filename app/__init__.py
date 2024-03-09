# Desc: Main entry point for the application
from fastapi import FastAPI
from app.globalexceptionhandler import GlobalExceptionHandler
from app.contoller import genai_router


app = FastAPI(debug=True)
app.exception_handler(Exception)(GlobalExceptionHandler.exception_handler)
app.include_router(genai_router)



