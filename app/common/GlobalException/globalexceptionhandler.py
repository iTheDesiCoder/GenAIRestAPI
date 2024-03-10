from fastapi.responses import JSONResponse
from app.common.Logging import logger

class GlobalExceptionHandler:

    @staticmethod
    async def exception_handler(request, exc):
        if request is not None:
            logger.error(f"An error occurred: {str(exc)} with request {request}")
        else:
            logger.error(f"An error occurred: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={"message1": str(exc)},
        )
