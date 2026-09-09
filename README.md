# Nexgile WealthAgent Portal

A responsive wealth-management portal prototype for individual clients, advisors, plan sponsors, and operations teams. It uses **React**, an accompanying **Angular implementation**, and a **FastAPI** backend.

> **Prototype notice:** All financial information is sample data. Integrations, approvals, calculations, and workflows are simulated for demonstration; this is not a live financial system.

## What is included

- `frontend-react/` — primary UI for Vercel (recommended)
- `frontend-angular/` — Angular version of the same login and portal experience
- `backend/` — FastAPI API for Railway

The primary React portal includes role switching, portfolio/holdings, rebalancing proposals, tax/estate/philanthropy scenarios, retirement and participant education, documents, messaging, approval queues, data quality, audit/lineage, and mock integration status.

## Functional coverage

- **Individual dashboard:** net worth, asset allocation, performance, retirement and education goals, data freshness, and advisor-reviewed insights.
- **Portfolio workstation:** consolidated mock holdings, report generation, and a rebalancing approval flow.
- **Tax, estate & philanthropy:** tax-loss harvesting request, beneficiary review, and charitable giving scenario.
- **Retirement & participant experience:** readiness score, retirement scenarios, learning path, and sponsor-oriented plan metrics.
- **Documents & communication:** secure-document, document-search, download, and advisor-message demo actions.
- **Operations & compliance:** approval queue, data quality, audit/lineage, and connected-source status representation.

The sidebar role selector demonstrates client, advisor, plan sponsor, and operations/compliance views. It is a frontend demonstration, not real access control.

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
3. Set the start command to `uvicorn main:app --host 0.0.0.0 --port $PORT`.
4. Set health check path to `/health`, deploy, then generate the public domain on port `8080`.

### Vercel (React frontend)

1. Import this repository into Vercel.
2. Set **Root Directory** to `frontend-react`.
3. Use build command `vite build` and output directory `dist`.
4. Add environment variable `VITE_API_URL` with the Railway URL plus `/api`, for example `https://your-api.up.railway.app/api`.
5. Deploy. Pushes to `main` trigger redeployments.

For an Angular deployment instead, import the same repository with root directory `frontend-angular`; use the build command `npm run build` and output directory `dist/frontend-angular/browser`.

## Production note

Before using real client data, replace demo login with a proper identity provider, secure cookies/JWT handling, database storage, authorization controls, audit logging, encryption, and compliance review.
