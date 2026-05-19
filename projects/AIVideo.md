---
layout: default
title: AI Video Production System
---

<a href="/projects" class="back-link"><span>&larr;</span> Back to Projects</a>

<div class="navigation-links">
  <a href="https://cdcastr0.github.io/">Home</a>
  <a href="https://cdcastr0.github.io/education">Education</a>
  <a href="https://cdcastr0.github.io/skills">Skills & Expertise</a>
  <a href="https://cdcastr0.github.io/experience">Experience</a>
  <a href="https://cdcastr0.github.io/projects">Projects</a>
</div>

# AI Video Production System

## Overview

A multi-agent AI pipeline for producing educational YouTube content about artificial intelligence. Rather than relying on a single generalist model, the system distributes the work across five specialized agents — each with a focused role, custom persona, and specific output format.

## Agent Architecture

| Agent | Role | Output |
|---|---|---|
| ResearcherBot | Gathers facts, stats, expert opinions on a topic | 3–6 sourced bullet points |
| WriterBot | Turns research into a complete 1,400+ word script | Full video script with hook/intro/body/CTA |
| EditorBot | Polishes tone, pacing, hook strength | Revised script |
| VisualBot | Suggests on-screen elements and B-roll | Timestamped visual cues |
| BrandingBot | Adds channel intro, outro, and CTAs | Final production-ready script |

## WriterBot Persona

The WriterBot is tuned to a specific voice: conversational yet sophisticated, narrative-driven, dryly humorous, and research-obsessed. The goal is content that treats viewers as intelligent but not experts — building genuine understanding rather than surface-level summaries.

Key techniques built into the system prompt:
- Lead with a counterintuitive hook in the first 10 seconds
- Build in "unexpected connections" between the AI topic and everyday experience
- Avoid jargon without explanation
- End with an actionable insight, not just a summary

## Why Multi-Agent?

A single LLM prompt attempting to research, write, edit, and brand simultaneously tends to produce mediocre work across all dimensions. Specialization — giving each agent a narrow, clear mandate — produces better output at each stage. It also makes the pipeline easier to debug: if the hook is weak, the problem is in WriterBot's prompt, not in a monolithic black box.

## Technology Stack

- **Orchestration:** DeepLearning.AI AI Playground (multi-agent mode)
- **Models:** OpenAI GPT family
- **Design pattern:** Role-based agent specialization with sequential handoffs

---

[GitHub Repository](https://github.com/CDCastr0/AIVideoProject) | [← Back to Projects](/projects)

<footer class="site-footer">
  <p>&copy; 2025 Christian Castro. All rights reserved.</p>
</footer>
