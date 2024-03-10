# Desc: Main entry point for the application
from fastapi import FastAPI
from app.common.GlobalException.globalexceptionhandler import GlobalExceptionHandler
from .contoller import genai_router


app = FastAPI()
app.exception_handler(Exception)(GlobalExceptionHandler.exception_handler)
app.include_router(genai_router)