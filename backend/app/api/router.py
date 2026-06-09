"""
API Router - Combines all API endpoints
"""

from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/status", tags=["Status"])
async def api_status() -> dict:
    """Get API status."""
    return {"status": "operational"}