from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from .routers import clinics, bookings, users

# Create FastAPI app
app = FastAPI(
    title="CareEscapes API",
    description="API for dental tourism platform with booking capabilities",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(clinics.router)
app.include_router(bookings.router)
app.include_router(users.router)

@app.get("/")
async def root():
    # Verify database connection string is available
    db_conn = os.getenv("DB_CONNECTION_STRING", "Not configured")
    db_status = "Configured" if db_conn != "Not configured" else "Not configured"
    
    return {
        "message": "Welcome to the CareEscapes API",
        "database_status": db_status
    }

if __name__ == "__main__":
    uvicorn.run("api.db_server:app", host="0.0.0.0", port=8092, reload=True) 