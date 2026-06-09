# OfficeAI Call Center

**AI-powered virtual receptionist and call management platform.** OfficeAI Call Center handles inbound calls, routes them intelligently, provides real-time transcription and translation, and offers a full-featured dashboard for agents and supervisors.

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/your-org/officeai-call-center.git
cd officeai-call-center

# Copy environment file
cp .env.example .env

# Start with Docker
docker compose up -d

# Access the application
# Frontend: http://localhost:3000
# API:      http://localhost:8000/api/v1
# Docs:     http://localhost:8000/docs
```

---

## Architecture Overview

```
                    ┌─────────────────────────────────────────────────────┐
                    │                     Callers                         │
                    │              (PSTN / SIP / Web)                     │
                    └────────────────────┬────────────────────────────────┘
                                         │
                                         ▼
                    ┌─────────────────────────────────────────────────────┐
                    │                    Twilio                           │
                    │         (Voice / SIP / Media Streams)               │
                    └────────────────────┬────────────────────────────────┘
                                         │
                                         ▼
                    ┌──────────────────────────────────────────────────────┐
                    │                   Backend (FastAPI)                  │
                    │  ┌─────────┐  ┌──────────┐  ┌───────────────────┐  │
                    │  │  Auth   │  │  REST    │  │   WebSocket       │  │
                    │  │  Module │  │  API     │  │   Manager         │  │
                    │  └─────────┘  └──────────┘  └───────────────────┘  │
                    │  ┌─────────┐  ┌──────────┐  ┌───────────────────┐  │
                    │  │  Call   │  │  Ticket  │  │   AI Orchestrator │  │
                    │  │  Router │  │  Manager │  │                   │  │
                    │  └─────────┘  └──────────┘  └───────────────────┘  │
                    └──────────┬──────────────────────────────────────────┘
                               │
          ┌────────────────────┼────────────────────────────────────┐
          │                    │                                    │
          ▼                    ▼                                    ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────────┐
│   PostgreSQL     │  │      Redis       │  │        ChromaDB          │
│  - Calls         │  │  - Session       │  │  - Vector embeddings    │
│  - Users         │  │  - Queue         │  │  - Knowledge base       │
│  - Tickets       │  │  - Cache         │  │  - Semantic search      │
│  - Customers     │  │  - Rate Limits   │  │                          │
│  - Audit Logs    │  │                  │  │                          │
└──────────────────┘  └──────────────────┘  └──────────────────────────┘
                               │                    │
                               ▼                    ▼
          ┌──────────────────────────────────────────────────────────────┐
          │                    AI Services Layer                         │
          │  ┌────────────────┐  ┌──────────────┐  ┌────────────────┐  │
          │  │  Voice Agent   │  │  Transcriber  │  │   Sentiment    │  │
          │  │  (gpt-4o)      │  │  (Whisper)    │  │   Analysis     │  │
          │  └────────────────┘  └──────────────┘  └────────────────┘  │
          └──────────────────────────┬───────────────────────────────────┘
                                     │
                                     ▼
          ┌──────────────────────────────────────────────────────────────┐
          │                External AI APIs                              │
          │  ┌────────────────────┐      ┌──────────────────────────┐   │
          │  │   OpenAI API       │      │    ElevenLabs API        │   │
          │  │  - GPT-4o Realtime │      │  - Text-to-Speech        │   │
          │  │  - Whisper STT     │      │  - Voice Synthesis       │   │
          │  └────────────────────┘      └──────────────────────────┘   │
          └──────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────────────────┐
                    │              Frontend (Next.js)                     │
                    │  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
                    │  │Dashboard │  │  Agent   │  │  Admin Panel     │  │
                    │  │   View   │  │   Panel  │  │                  │  │
                    │  └──────────┘  └──────────┘  └──────────────────┘  │
                    │  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
                    │  │ Reports  │  │ Settings │  │  Live Monitor    │  │
                    │  └──────────┘  └──────────┘  └──────────────────┘  │
                    └─────────────────────────────────────────────────────┘
```

---

## Features

| Feature | Description |
|---|---|
| **AI Receptionist** | GPT-4o-powered voice agent that handles calls, answers questions, and routes intelligently |
| **Real-time Transcription** | Live speech-to-text via OpenAI Whisper with interim results |
| **Multilingual Support** | English and Nepali with automatic language detection |
| **Sentiment Analysis** | Real-time customer sentiment tracking during calls |
| **Smart Call Routing** | IVR menus, skill-based routing, department queues |
| **Live Agent Dashboard** | Real-time call monitoring with WebSocket updates |
| **Ticketing System** | Integrated ticket management with SLA tracking |
| **Knowledge Base** | Vector search-powered FAQ and article retrieval |
| **Analytics & Reports** | Call metrics, agent performance, sentiment trends |
| **Role-Based Access** | Super admin, admin, supervisor, agent, receptionist roles |
| **Twilio Integration** | SIP trunking, media streams, IVR flows |
| **Recording & Voicemail** | Call recording storage and voicemail capabilities |

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.12+, FastAPI, SQLAlchemy 2.0, Pydantic v2 |
| **Frontend** | Next.js 14, React 18, TypeScript, Tailwind CSS, Radix UI |
| **Database** | PostgreSQL 16, Redis 7, pgvector, ChromaDB |
| **AI/ML** | OpenAI GPT-4o Realtime, Whisper, ElevenLabs TTS |
| **Telephony** | Twilio Voice, SIP, Media Streams |
| **Messaging** | WebSocket, SSE, Socket.IO |
| **Task Queue** | Celery with Redis broker |
| **Auth** | JWT (access + refresh tokens), bcrypt, RBAC |
| **Infrastructure** | Docker, Nginx, Prometheus |
| **Testing** | pytest, pytest-asyncio |

---

## Prerequisites

- **Python** 3.12+
- **Node.js** 18+
- **PostgreSQL** 16+
- **Redis** 7+
- **Docker** & Docker Compose (optional)
- **Twilio** account with voice-enabled phone number
- **OpenAI** API key
- **ElevenLabs** API key (optional, for TTS)

---

## Installation

### Docker (Recommended)

```bash
# Start all services
docker compose up -d

# View logs
docker compose logs -f

# Stop services
docker compose down
```

### Manual Installation

**Backend:**
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your settings
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
cp .env.example .env.local
# Edit .env.local with your settings
npm run dev
```

---

## Configuration

All configuration is managed via environment variables. See [docs/environment.md](docs/environment.md) for a complete reference.

Key variables:

```bash
# Database
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/officeai_call_center
REDIS_URL=redis://localhost:6379/0

# Auth
JWT_SECRET_KEY=your-secret-key-here

# Twilio
TWILIO_ACCOUNT_SID=your-account-sid
TWILIO_AUTH_TOKEN=your-auth-token
TWILIO_PHONE_NUMBER=+1234567890

# OpenAI
OPENAI_API_KEY=sk-your-key
```

---

## Usage Examples

### Make a Test Call

```bash
# From your phone, dial your Twilio number
# The AI receptionist will answer and route your call
```

### API Authentication

```bash
# Get access token
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "your-password"}'

# Use token for authenticated requests
curl http://localhost:8000/api/v1/calls \
  -H "Authorization: Bearer <access_token>"
```

### WebSocket Connection

```javascript
// Connect to real-time events
const ws = new WebSocket('ws://localhost:8000/ws?token=<access_token>');

ws.onmessage = (event) => {
  const msg = JSON.parse(event.data);
  console.log(msg.type, msg.data);
};
```

---

## API Documentation

Interactive API documentation is available when the backend is running:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

See [docs/api/overview.md](docs/api/overview.md) for the complete API reference.

---

## Project Structure

```
officeai-call-center/
├── backend/
│   ├── app/
│   │   ├── api/          # API route definitions
│   │   ├── core/         # Config, database, security
│   │   ├── middleware/    # Rate limiting, auth, logging
│   │   ├── models/       # SQLAlchemy ORM models
│   │   ├── schemas/      # Pydantic request/response schemas
│   │   └── utils/        # Constants, helpers, prompts
│   └── requirements.txt
├── frontend/
│   ├── app/              # Next.js pages and routes
│   ├── components/       # React components
│   └── package.json
├── ai-services/
│   ├── voice-agent/      # GPT-4o real-time voice agent
│   ├── transcriber/      # Whisper transcription service
│   └── sentiment/        # Sentiment analysis service
├── docker/               # Docker configurations
├── scripts/              # Utility scripts
├── data/                 # Uploads and recordings
└── docs/                 # Documentation
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Support

- **Documentation:** [docs/](docs/)
- **Issues:** [GitHub Issues](https://github.com/your-org/officeai-call-center/issues)
- **Email:** support@officeai.example.com

---

*Built with FastAPI, Next.js, OpenAI, and Twilio.*
