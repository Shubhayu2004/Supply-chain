from fastapi import FastAPI
from .routers import detection, results, inventory

app = FastAPI()

app.include_router(detection.router)
app.include_router(results.router)
app.include_router(inventory.router)

@app.get("/")
def read_root():
    return {"message": "Inventory Monitoring Backend is running!"} 