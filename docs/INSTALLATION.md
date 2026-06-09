# Installation & Setup Guide

## Prerequisites

- Python 3.12+
- Node.js 20+
- PostgreSQL 15+
- Redis 7+
- Docker & Docker Compose (optional)

## Quick Start with Docker

### 1. Clone Repository
```bash
git clone https://github.com/meetdrajiv/AI_Call_Centre.git
cd AI_Call_Centre
```

### 2. Create Environment File
```bash
cp .env.example .env
# Edit .env with your settings (see Configuration below)
```

### 3. Start Services
```bash
docker-compose up -d
```

### 4. Access Application
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/api/v1/docs
- Redis: localhost:6379
- PostgreSQL: localhost:5432

## Manual Installation

### Backend Setup

```bash
cd backend

# Create virtual environment
python3.12 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example ../.env

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Copy environment file
cp .env.example .env.local

# Start development server
npm run dev
```

Access the application at http://localhost:3000

## Configuration

### Essential Environment Variables

```bash
# Application
PROJECT_NAME=OfficeAI Call Center
VERSION=1.0.0
DEBUG=false
ENVIRONMENT=production

# Database (CHANGE DEFAULT CREDENTIALS!)
DATABASE_URL=postgresql+asyncpg://postgres:CHANGE_ME@localhost:5432/officeai
REDIS_URL=redis://localhost:6379/0

# Security (GENERATE NEW SECRETS!)
SECRET_KEY=<generate-with-secrets.token_urlsafe(32)>
JWT_SECRET_KEY=<generate-with-secrets.token_hex(32)>

# Twilio
TWILIO_ACCOUNT_SID=<your-account-sid>
TWILIO_AUTH_TOKEN=<your-auth-token>
TWILIO_PHONE_NUMBER=+1234567890

# OpenAI
OPENAI_API_KEY=sk-<your-api-key>

# ElevenLabs (Optional)
ELEVENLABS_API_KEY=<your-api-key>

# Frontend
NEXT_PUBLIC_API_URL=https://yourdomain.com/api
NEXT_PUBLIC_WS_URL=wss://yourdomain.com/ws
```

See [docs/SECURITY.md](./SECURITY.md) for security recommendations.

## Common Tasks

### Database Operations
```bash
# Run migrations
make migrate

# Create auto-migration
make migrate-auto msg="Add new table"

# Seed database
make seed

# Open database shell
make shell-db
```

### Testing
```bash
# Run all tests
make test

# Run with coverage
make test-coverage

# Run frontend tests
make test-frontend
```

### Linting & Formatting
```bash
# Check code quality
make lint

# Fix linting issues
make lint-fix

# Type checking
make typecheck
```

### Docker Management
```bash
# Build images
make build

# Start services
make up

# Stop services
make down

# View logs
make logs
make logs svc=backend
```

## Troubleshooting

### Database Connection Error
```bash
# Check PostgreSQL is running
docker-compose ps postgres

# Check connection string in .env
# Format: postgresql+asyncpg://user:password@host:port/database
```

### Redis Connection Error
```bash
# Check Redis is running
docker-compose ps redis

# Test connection
redis-cli ping
```

### Port Already in Use
```bash
# Change ports in docker-compose.yml
# Or kill existing process
# Linux/Mac: lsof -i :8000
# Windows: netstat -ano | findstr :8000
```

### Module Import Errors
```bash
# Ensure backend directory is in Python path
export PYTHONPATH="${PYTHONPATH}:/path/to/backend"

# Or reinstall dependencies
pip install -r requirements.txt
```

## Next Steps

1. Configure API keys (Twilio, OpenAI, ElevenLabs)
2. Set up SSL certificates
3. Configure domain name
4. Deploy to production (see docs/DEPLOYMENT.md)
5. Enable monitoring and logging
6. Set up backup strategy

## Support

- Issues: https://github.com/meetdrajiv/AI_Call_Centre/issues
- Documentation: https://github.com/meetdrajiv/AI_Call_Centre/tree/develop/docs
- Security: See [docs/SECURITY.md](./SECURITY.md)
