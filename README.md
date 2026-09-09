# Nexgile WealthAgent Portal

A responsive wealth-management portal demo built with **React**, an accompanying **Angular login/dashboard implementation**, and a **FastAPI** backend.

## What is included

- `frontend-react/` — primary UI for Vercel (recommended)
- `frontend-angular/` — Angular version of the same login and portal experience
- `backend/` — FastAPI API for Railway

The demo covers the requested portal concepts: role-aware sign-in, portfolio value and allocation, goals, tax opportunities, retirement-plan activity, notifications, documents, and advisor insights. It deliberately uses sample data and a demo authentication flow.

## Run locally

### API

```bash
cd backend
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### React website

```bash
cd frontend-react
npm install
npm run dev
```

Open the local URL shown by Vite. Sign in with any valid email and a password of at least 4 characters. `alex@nexgile.com` is prefilled.

### Angular version

```bash
cd frontend-angular
npm install
npm start
```

## Deploy in a few minutes

### Railway (backend)

1. Create a Railway project from this GitHub repository.
2. Set the service root directory to `backend`.
3. Railway reads `railway.toml` and starts the API automatically.
4. Copy the generated public URL (for example `https://your-api.up.railway.app`).

### Vercel (React frontend)

1. Import this repository into Vercel.
2. Set **Root Directory** to `frontend-react`.
3. Add environment variable `VITE_API_URL` with the Railway URL plus `/api`, for example `https://your-api.up.railway.app/api`.
4. Deploy. Vercel recognizes the included configuration.

For an Angular deployment instead, import the same repository with root directory `frontend-angular`; use the build command `npm run build` and output directory `dist/frontend-angular/browser`.

## Production note

Before using real client data, replace demo login with a proper identity provider, secure cookies/JWT handling, database storage, authorization controls, audit logging, encryption, and compliance review.
