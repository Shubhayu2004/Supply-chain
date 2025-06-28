from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import detection, results, inventory
import os

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files for serving result images
results_dir = os.path.join(os.path.dirname(__file__), '../results')
if os.path.exists(results_dir):
    app.mount("/results", StaticFiles(directory=results_dir), name="results")

app.include_router(detection.router)
app.include_router(results.router)
app.include_router(inventory.router)

@app.get("/")
def read_root():
    return {"message": "Inventory Monitoring Backend is running!"} 