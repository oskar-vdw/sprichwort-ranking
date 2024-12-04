# Sprichwort Ranking

A full-stack application for ranking German proverbs ("Sprichwörter") using an ELO rating system.

## Stack
- Frontend: Vue 3 + TypeScript + Vite
- Backend: Flask + SQLAlchemy
- Database: PostgreSQL
- Containerized with Docker

## Quick Start

```bash
# Clone repository
git clone https://github.com/oskarvdw/sprichwort-ranking.git

```

Frontend runs on port 5173, backend on port 5000.

```bash
# Backend
cd sprichwort-ranking-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run

# Frontend
cd sprichwort-ranking-frontend
npm install
npm run dev
```

The database has to be set up independently.


## License
MIT