"""
Application Configuration Management
"""

from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    PROJECT_NAME: str = "OfficeAI Call Center"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "production"
    LOG_LEVEL: str = "INFO"
    RATE_LIMIT: str = "100/minute"

    # Server
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/officeai"
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10
    DATABASE_POOL_RECYCLE: int = 3600

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_SOCKET_CONNECT_TIMEOUT: int = 5
    REDIS_SOCKET_KEEPALIVE: bool = True

    # Security
    SECRET_KEY: str = "change-this-to-a-random-secret-key-in-production"
    JWT_SECRET_KEY: str = "change-this-to-a-random-jwt-secret-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRES: int = 30
    JWT_REFRESH_TOKEN_EXPIRES: int = 7

    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]

    # Twilio
    TWILIO_ACCOUNT_SID: str = ""
    TWILIO_AUTH_TOKEN: str = ""
    TWILIO_PHONE_NUMBER: str = "+1234567890"
    TWILIO_SIP_DOMAIN: str = ""

    # OpenAI
    OPENAI_API_KEY: str = ""
    OPENAI_REALTIME_MODEL: str = "gpt-4o-realtime-preview"
    OPENAI_WHISPER_MODEL: str = "whisper-1"
    OPENAI_TEMPERATURE: float = 0.7
    OPENAI_MAX_TOKENS: int = 500

    # ElevenLabs
    ELEVENLABS_API_KEY: str = ""
    ELEVENLABS_VOICE_ID: str = "21m00Tcm4TlvDq8ikWAM"

    # Storage
    STORAGE_BACKEND: str = "local"
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_REGION: str = "us-east-1"
    S3_BUCKET: str = "officeai-recordings"
    STORAGE_PATH: str = "/app/media"

    # Vector Database
    VECTOR_DB_BACKEND: str = "chroma"
    CHROMA_HOST: str = "chromadb"
    CHROMA_PORT: int = 8000
    CHROMA_PERSIST_DIR: str = "/data/chroma"
    EMBEDDINGS_MODEL: str = "all-MiniLM-L6-v2"

    # AI Configuration
    NEPALI_SUPPORT_ENABLED: bool = True
    DEFAULT_LANGUAGE: str = "en"
    SUPPORTED_LANGUAGES: List[str] = ["en", "ne"]

    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"
    CELERY_TASK_TRACK_STARTED: bool = True
    CELERY_TASK_TIME_LIMIT: int = 300
    CELERY_TASK_SOFT_TIME_LIMIT: int = 250

    # Monitoring
    PROMETHEUS_ENABLED: bool = True
    PROMETHEUS_PORT: int = 9090
    LOG_FORMAT: str = "json"
    SENTRY_DSN: str = ""

    # Features
    ENABLE_CALL_RECORDING: bool = True
    ENABLE_TRANSCRIPTION: bool = True
    ENABLE_SENTIMENT_ANALYSIS: bool = True
    ENABLE_KNOWLEDGE_BASE: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()