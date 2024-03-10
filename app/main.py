# Desc: Main entry point for the application
from fastapi import FastAPI
from .common.GlobalException.globalexceptionhandler import GlobalExceptionHandler

app = FastAPI()
app.exception_handler(Exception)(GlobalExceptionHandler.exception_handler)
