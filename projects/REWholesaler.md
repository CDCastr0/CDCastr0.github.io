---
layout: default
title: RE Wholesaler — Automated Real Estate Pipeline
---

<a href="/projects" class="back-link"><span>&larr;</span> Back to Projects</a>

<div class="navigation-links">
  <a href="https://cdcastr0.github.io/">Home</a>
  <a href="https://cdcastr0.github.io/education">Education</a>
  <a href="https://cdcastr0.github.io/skills">Skills & Expertise</a>
  <a href="https://cdcastr0.github.io/experience">Experience</a>
  <a href="https://cdcastr0.github.io/projects">Projects</a>
</div>

# RE Wholesaler — Automated Real Estate Pipeline

## Overview

A full-stack automated wholesaling pipeline targeting distressed properties across 7 Dallas–Fort Worth counties (Dallas, Tarrant, Collin, Denton, Rockwall, Kaufman, Ellis). The system runs continuously — scraping public records, enriching leads, running multi-channel outreach, generating purchase contracts, and pushing deals to institutional buyer platforms — without manual intervention.

Connected to a personal Mission Control dashboard for real-time pipeline visibility.

## Architecture

```
re_wholesaler/
├── database/     SQLAlchemy 2.0 async models + session management
├── scrapers/     Foreclosure, tax lien, probate, lis pendens + AVM
├── leads/        Ingestor (rapidfuzz dedup), distress scorer, offer calculator
├── outreach/     Enzo Dialer, Twilio SMS, SendGrid email, contact sequencer
├── contracts/    9 verbatim legal clauses, ReportLab PDF generator
├── buyers/       MaxDispo + InvestorLift API push clients
├── crm/          6-stage pipeline state machine + deadline alerts
├── briefs/       Daily brief generator (email + SMS + dashboard)
└── osint/        DCAD enrichment, code violations, absentee owner detection

cli/              Typer CLI (re-ws entrypoint, 15+ commands)
scheduler/        APScheduler — 11 automated daily jobs
tests/            pytest — contracts, leads, offer calculator
```

## Data Models

Seven SQLAlchemy 2.0 async ORM models, all UUID primary keys:

| Model | Purpose |
|---|---|
| Lead | Distressed property with distress_score, ARV, offer_price_low/high |
| Contact | Owner/agent/attorney with skip_trace_raw JSON |
| Deal | 6-stage pipeline with key dates (close, inspection, assignment) |
| OutreachLog | Every outreach attempt — channel, status, external ID |
| Document | Generated PDFs with SHA-256 integrity hash |
| Buyer | Cash buyer registry with platform + criteria JSON |
| PipelineEvent | Immutable audit log of every stage transition |

## Lead Scoring & Offer Calculation

The distress scorer assigns a numeric score based on: lien type severity, time since origination, absentee owner status, code violations, and probate/foreclosure status. The offer calculator applies the 70% rule (ARV × 0.70 − estimated repairs) modified by distress score to generate low/high offer bounds. Talking points for outreach scripts are generated from the same data.

## Outreach Automation

Multi-channel sequences: Enzo Dialer (voice), Twilio (SMS), SendGrid (email). The contact sequencer tracks every attempt in OutreachLog and enforces DNC compliance and channel rotation rules.

## Technology Stack

| Category | Tools |
|---|---|
| Backend | Python 3.12, FastAPI, Uvicorn |
| ORM | SQLAlchemy 2.0 async, Pydantic v2 |
| Database | SQLite (default) / PostgreSQL |
| Scheduling | APScheduler (11 jobs) |
| CLI | Typer |
| PDF Generation | ReportLab |
| Frontend | React + Vite |
| Testing | pytest |
| Skip Trace / AVM | xLeads API |
| Buyer Platforms | MaxDispo API, InvestorLift API |
| Outreach | Twilio SMS, SendGrid, Enzo Dialer |

---

[← Back to Projects](/projects)

<footer class="site-footer">
  <p>&copy; 2025 Christian Castro. All rights reserved.</p>
</footer>
