---
layout: default
title: LoanReady — DSCR Calculator SaaS
---

<a href="/projects" class="back-link"><span>&larr;</span> Back to Projects</a>

<div class="navigation-links">
  <a href="https://cdcastr0.github.io/">Home</a>
  <a href="https://cdcastr0.github.io/education">Education</a>
  <a href="https://cdcastr0.github.io/skills">Skills & Expertise</a>
  <a href="https://cdcastr0.github.io/experience">Experience</a>
  <a href="https://cdcastr0.github.io/projects">Projects</a>
</div>

# LoanReady — DSCR Calculator SaaS

## Overview

LoanReady helps real estate investors calculate their Debt Service Coverage Ratio (DSCR) before meeting with lenders. Users upload bank statements and rental profit & loss statements; Claude Haiku extracts all transactions from the documents, computes the DSCR, and generates a lender-ready PDF report — in minutes.

## What is DSCR?

DSCR = Net Operating Income ÷ Total Debt Service

Lenders use DSCR to assess whether a rental property generates enough income to cover its loan payments. A DSCR above 1.25 is typically required for DSCR loan approval. LoanReady lets investors know their number before they walk into a lender meeting.

## How It Works

1. User creates an account (Clerk authentication)
2. Uploads bank statement or rental P&L as PDF
3. Claude Haiku reads the document and extracts transactions (date, description, amount, category)
4. System computes: Gross Rental Income → Net Operating Income → DSCR ratio
5. Stripe payment unlocks the full lender-ready PDF report
6. Report includes transaction breakdown, ratio visualization, and anomaly flags

## Technology Stack

| Category | Tools |
|---|---|
| Frontend & Backend | Next.js 15, TypeScript, React 19 |
| UI | shadcn/ui, Tailwind v4 |
| ORM & Database | Prisma 5, SQLite |
| Authentication | Clerk |
| Payments | Stripe |
| AI / PDF Extraction | Claude Haiku (claude-haiku-4-5) |
| Deployment | Vercel |

## Data Model

- **User** — clerkId, email, linked to reports and subscription
- **Report** — status, docType, grossRentalIncome, totalExpenses, netIncome, totalDebt, dscrRatio, paid, stripePaymentId, flags
- **Transaction** — date, description, amount, type, category (child of Report)
- **Subscription** — stripeCustomerId, stripePriceId, status, currentPeriodEnd

## Key Design Decisions

**Claude Haiku for extraction:** Haiku is the fastest, most cost-efficient Claude model. PDF extraction is a structured task that doesn't require deep reasoning — Haiku reliably pulls tabular data in a single prompt at under $0.01 per report.

**Vision-based extraction:** Claude reads the PDF visually, so scanned bank statements (image PDFs) work without a separate OCR layer.

**Stripe gating:** The DSCR computation runs for free; the lender-ready PDF download is gated behind a Stripe payment. This lets users see their number before committing.

---

[← Back to Projects](/projects)

<footer class="site-footer">
  <p>&copy; 2025 Christian Castro. All rights reserved.</p>
</footer>
