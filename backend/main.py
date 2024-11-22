from fastapi import FastAPI
import time
import math
import os
from datetime import datetime

app = FastAPI()
LOG_FILE = "/app/data/app.log"

# Ensure log directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

@app.get("/write/{data}")
async def write_data(data: str):
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp}: {data}\n")
    return {"message": f"Data written: {data}"}

@app.get("/read")
async def read_data():
    try:
        with open(LOG_FILE, "r") as f:
            return {"data": f.read()}
    except FileNotFoundError:
        return {"data": "No data found"}

@app.get("/compute")
async def compute():
    start_time = time.time()
    result = 0
    for i in range(1, 10000000):
        result += math.sin(i) * math.cos(i)
    end_time = time.time()
    execution_time = end_time - start_time
    return {"result": result, "execution_time": f"{execution_time:.2f} seconds"}

@app.get("/status")
async def status():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }