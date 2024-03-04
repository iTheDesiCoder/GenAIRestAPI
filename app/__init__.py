# Desc: Main entry point for the application
import os
from fastapi import FastAPI
from app.globalexceptionhandler import GlobalExceptionHandler
from app.contoller import genai_router
from config import OPENAI_API_KEY


os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
app = FastAPI(debug=True)
app.exception_handler(Exception)(GlobalExceptionHandler.exception_handler)
app.include_router(genai_router)
