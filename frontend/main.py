from fastapi import FastAPI, HTTPException
import httpx
import os

app = FastAPI()
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:3402")

async def proxy_request(path: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{BACKEND_URL}{path}")
            return response.json()
        except httpx.RequestError:
            raise HTTPException(status_code=503, detail="Backend service unavailable")

@app.get("/write/{data}")
async def write_data(data: str):
    return await proxy_request(f"/write/{data}")

@app.get("/read")
async def read_data():
    return await proxy_request("/read")

@app.get("/compute")
async def compute():
    return await proxy_request("/compute")

@app.get("/status")
async def status():
    return await proxy_request("/status")