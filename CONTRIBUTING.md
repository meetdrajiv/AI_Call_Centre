# Contributing to OfficeAI Call Center

Thank you for your interest in contributing! This document outlines the contribution process.

## Code of Conduct

By participating, you agree to maintain a respectful and inclusive environment.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/officeai-call-center.git`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Install dependencies (see [README.md](README.md))
5. Make your changes
6. Run tests: `pytest`
7. Submit a pull request

## Branch Strategy

| Branch | Purpose |
|---|---|
| `main` | Production-ready code |
| `develop` | Integration branch for features |
| `feature/*` | New features (branch from `develop`) |
| `fix/*` | Bug fixes (branch from `develop`) |
| `hotfix/*` | Urgent production fixes (branch from `main`) |
| `release/*` | Release preparation |

Branch naming convention: `type/short-description` (e.g., `feature/multilingual-ivr`, `fix/call-routing-bug`).

## Pull Request Process

1. Ensure all tests pass and linting is clean
2. Update documentation if your changes affect public APIs or behavior
3. Include a clear description of the change and its motivation
4. Reference any related issues using `Closes #123` syntax
5. Request review from at least one maintainer
6. Squash commits before merging (use rebase strategy)

### PR Checklist

- [ ] Code follows project style and conventions
- [ ] Tests added/updated for all changes
- [ ] Documentation updated (if applicable)
- [ ] All existing tests pass
- [ ] Lint check passes (`ruff check .`)
- [ ] Type check passes (`mypy .`)
- [ ] No new warnings or errors
- [ ] Commit messages follow convention

## Commit Message Format

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

| Type | Usage |
|---|---|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `style` | Formatting, whitespace (no logic change) |
| `refactor` | Code restructuring |
| `perf` | Performance improvement |
| `test` | Adding or updating tests |
| `chore` | Build, CI, dependencies |
| `ci` | CI configuration changes |

### Examples

```
feat(calls): add warm transfer between agents

Implement warm transfer with consult-call-bridge flow.
Includes hold music for the original caller during consultation.

Closes #142
```

```
fix(twilio): handle missing call SID on stream disconnect

Prevents KeyError when Twilio WebSocket stream drops
before the call SID is available.

Fixes #89
```

```
docs(api): document WebSocket event payloads
```

## Code Style

### Python (Backend)

- Follow **PEP 8** conventions
- Use **type hints** for all function signatures
- Use **f-strings** for string formatting
- Sort imports with `isort`:
  ```
  isort .
  ```
- Lint with `ruff`:
  ```
  ruff check .
  ruff format . --check
  ```
- Type-check with `mypy`:
  ```
  mypy .
  ```
- Maximum line length: **100 characters**
- Use **async def** for all route handlers and database operations
- Use **Pydantic v2** models for request/response validation
- Use **SQLAlchemy 2.0 style** queries (no legacy query API)

### TypeScript/JavaScript (Frontend)

- Use **TypeScript** strict mode
- Use **ESLint** and **Prettier** as configured in the project
- Use **functional components** with hooks (no class components)
- Use **Tailwind CSS** for styling (avoid inline styles)
- Use **Zustand** for global state management
- Use **TanStack Query** for server state

### General

- Write descriptive variable and function names
- Keep functions small and focused (single responsibility)
- Avoid commented-out code
- Write tests for new functionality
- Update API documentation when changing endpoints

## Testing

### Backend Tests

```bash
cd backend
pytest                          # All tests
pytest -v                       # Verbose
pytest --cov=app                # With coverage
pytest -k "test_calls"          # Specific tests
pytest -x --pdb                 # Stop on first failure, drop into debugger
```

### Frontend Tests

```bash
cd frontend
npm run test                    # All tests
npm run test:watch              # Watch mode
npm run test:coverage           # With coverage
```

### Test Requirements

- All new features must include tests
- Bug fixes must include a regression test
- Aim for **80%+ code coverage**
- Tests must not depend on external services (mock Twilio, OpenAI, etc.)
- Use `pytest-asyncio` for async test support
- Name test files as `test_<module>.py`

## Project Structure Guidelines

- Keep API routes in `backend/app/api/v1/` organized by resource
- Add new models to `backend/app/models/`
- Add new schemas to `backend/app/schemas/`
- Business logic belongs in services, not in route handlers
- Configuration belongs in `backend/app/core/config.py`
- Constants and enums belong in `backend/app/utils/constants.py`

## Security

- Never commit API keys, tokens, or secrets
- Use environment variables for all configuration
- Always validate and sanitize user input
- Use parameterized queries (SQLAlchemy handles this)
- Report security vulnerabilities privately (see [SECURITY.md](docs/security/security-guide.md))

## Documentation

- Keep README.md up to date
- Document all public API endpoints with request/response schemas
- Update the environment variable reference when adding new config
- Add inline comments only for complex logic (not obvious code)
- Documentation lives in `docs/` as Markdown files

## Getting Help

If you need help, open a GitHub Discussion or ask in issues. For urgent matters, contact the maintainers directly.
