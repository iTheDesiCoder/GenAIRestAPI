from fastapi.responses import JSONResponse


class GlobalExceptionHandler:
    @staticmethod
    async def exception_handler(request, exc):
        return JSONResponse(
            status_code=500,
            content={"message": str(exc)},
        )
