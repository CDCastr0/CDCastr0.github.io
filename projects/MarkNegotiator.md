---
layout: default
title: Mark — AI Storage Unit Negotiator
---

<a href="/projects" class="back-link"><span>&larr;</span> Back to Projects</a>

<div class="navigation-links">
  <a href="https://cdcastr0.github.io/">Home</a>
  <a href="https://cdcastr0.github.io/education">Education</a>
  <a href="https://cdcastr0.github.io/skills">Skills & Expertise</a>
  <a href="https://cdcastr0.github.io/experience">Experience</a>
  <a href="https://cdcastr0.github.io/projects">Projects</a>
</div>

# Mark — AI Storage Negotiator

## Overview

Mark is a conversational AI agent that negotiates monthly storage unit rental rates on behalf of storage facility businesses. Customers interact with Mark in a chat interface; he checks availability and pricing in real time, handles objections, applies appropriate discounts, and sends deal confirmation emails when an agreement is reached.

## How It Works

Mark is powered by Claude claude-opus-4-6 using Anthropic's tool_use API. Rather than hallucinating pricing, Mark calls structured functions mid-conversation:

| Tool | What it does |
|---|---|
| `check_availability` | Checks if a unit type/size is available |
| `get_current_price` | Retrieves the current monthly rate |
| `apply_discount` | Calculates and applies a negotiated discount |
| `send_confirmation` | Triggers a confirmation email via Resend |

When Mark decides to check a price, the model outputs a `tool_call` block. The server executes the function and returns real data. Mark continues the conversation with accurate, grounded information — no hallucinated prices.

## Technology Stack

| Category | Tools |
|---|---|
| Frontend | Next.js 14, TypeScript, React |
| UI | Tailwind CSS |
| AI | Claude claude-opus-4-6 (Anthropic tool_use API) |
| Database | Prisma 5, SQLite |
| Email | Resend |

## Conversation Design

Mark's persona is designed to be helpful, honest, and persuasive without being pushy. The system prompt gives him knowledge of typical objections (price too high, need more time, comparing competitors) and response strategies. Conversation history is persisted in Prisma so sessions can be resumed.

## Key Challenge

The core engineering challenge is keeping the AI grounded during negotiation. Without tool_use, a language model would make up pricing numbers. With tool_use, every pricing claim is backed by a live function call — the model is constrained to only state numbers it actually retrieved.

---

[← Back to Projects](/projects)

<footer class="site-footer">
  <p>&copy; 2025 Christian Castro. All rights reserved.</p>
</footer>
