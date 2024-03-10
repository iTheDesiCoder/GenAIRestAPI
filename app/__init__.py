from .main import app
from .common.Logging import logger
from .contoller import genai_router


app.include_router(genai_router)

# Expose main components at the package level (optional, depending on your preference)
#__all__ = ["app", "logger"]



