# exception_handler.py

from fastapi import Request, status
from fastapi.responses import JSONResponse
from exceptions.custom_exceptions import ResourceNotFoundException


def resource_not_found_exception_handler(request: Request, exc: ResourceNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "success": False,
            "message": exc.message
        }
    )