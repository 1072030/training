import sys
import asyncio
import signal


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=80, workers=1)