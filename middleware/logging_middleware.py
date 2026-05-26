# logging_middleware.py

import time
import logging
from fastapi import Request


logger = logging.getLogger(__name__)


async def logging_middleware(request: Request, call_next):

    start_time = time.time()

    logger.info(
        f"Incoming request: "
        f"{request.method} "
        f"{request.url.path}"
    )

    response = await call_next(request)

    process_time = round(
        time.time() - start_time,
        4
    )

    logger.info(
        f"Completed: "
        f"{request.method} "
        f"{request.url.path} "
        f"Status: {response.status_code} "
        f"Time: {process_time}s"
    )

    return response