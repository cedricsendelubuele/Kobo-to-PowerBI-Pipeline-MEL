# Kobo → Python → SQL → Power BI (MEL) — NFI Distributions (Goma, DRC)

**EN (quick summary)**: End-to-end MEL reporting pipeline for NFI distributions in DRC: Kobo API extraction, Python cleaning + data quality checks (DQA), risk/fraud flags, SQL marts, and Power BI dashboards for MEL, operations and donor reporting. Uses synthetic data only.

**FR** : Ce projet simule un cas très courant en ONG à l’Est RDC : les données Kobo existent, mais le reporting est manuel, tardif et fragile. Je propose une chaîne complète et réaliste pour passer à un reporting fiable et rapide : extraction API Kobo, nettoyage Python, contrôles qualité (DQA), détection d’anomalies/fraude, structuration SQL, et tableaux de bord Power BI adaptés aux besoins MEL, opérations et bailleurs.

---

## Business context
- Location: Goma (North Kivu) + territories
- Activity: NFI distributions to displaced households
- Constraints: intermittent connectivity, dispersed teams, donor reporting pressure, data quality issues

See `docs/00_story_and_context.md`

---

## What this solves
- Replace manual CSV exports and Excel cleaning
- Reduce reporting delay from weeks to near-real-time
- Standardize KPIs and definitions (indicator reference sheets)
- Add Data Quality as a first-class reporting component
- Flag potential duplicates/fraud patterns for follow-up

---

## Architecture (high level)
KoboToolbox -> Kobo API -> Python (clean + DQA + risk flags) -> SQL marts -> Power BI dashboards

See `docs/01_architecture.md`

---

## Quick start (demo with synthetic data)
1) Start Postgres:
```bash
docker compose up -d
