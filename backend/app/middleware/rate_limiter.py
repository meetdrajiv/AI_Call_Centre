"""Middleware for Rate Limiting"""

import logging

from fastapi import Request, HTTPException

logger = logging.getLogger(__name__)


class RateLimiterMiddleware:
    """Rate limiter middleware."""

    def __init__(self, app):
        self.app = app
        self.request_counts = {}

    async def __call__(self, request: Request, call_next):
        """Rate limiter middleware."""
        client_ip = request.client.host if request.client else "unknown"
        
        # Simple in-memory rate limiting (replace with Redis in production)
        if client_ip not in self.request_counts:
            self.request_counts[client_ip] = 0
        
        self.request_counts[client_ip] += 1
        
        if self.request_counts[client_ip] > 100:  # 100 requests per minute
            logger.warning(f"Rate limit exceeded for {client_ip}")
            raise HTTPException(status_code=429, detail="Too many requests")
        
        response = await call_next(request)
        response.headers["X-RateLimit-Limit"] = "100"
        response.headers["X-RateLimit-Remaining"] = str(100 - self.request_counts[client_ip])
        
        return response
