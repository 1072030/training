import logging
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.core import conn
from app.route import (
    health,
    auth
)
app = FastAPI(title="Foxlink API Backend", version="0.0.1")
origins = [
    "http://localhost",
    "http://localhost:8086"
]
#add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex="http(?:s)?://(?:.+\.)?foxlink\.com\.tw(?::\d+)?",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
logger = logging.getLogger("uvicorn")
logger.propagate = False
#add router
app.include_router(health.router)
app.include_router(auth.router)

@app.on_event("startup")
async def startup():
    # connect to databases
    while True:
        try:
            await asyncio.gather(*[
                # api_db.connect(),
            ])
        except Exception as e:
            logger.error(f"Start up error: {e}")
            logger.error(f"Waiting for 5 seconds to restart")
            await asyncio.sleep(5)
        else:
            logger.info("Server startup complete")
            break
@app.on_event("shutdown")
async def shutdown():
    # disconnect databases
    while True:
        try:
            await asyncio.gather(*[
                
            ])
        except Exception as e:
            logger.error(f"Start up error: {e}")
            logger.error(f"Waiting for 5 seconds to restart")
            await asyncio.sleep(5)
        else:
            logger.info("Server shutdown complete.")
            break