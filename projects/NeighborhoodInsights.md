---
layout: default
title: Neighborhood Insights — Data Platform
---

<a href="/projects" class="back-link"><span>&larr;</span> Back to Projects</a>

<div class="navigation-links">
  <a href="https://cdcastr0.github.io/">Home</a>
  <a href="https://cdcastr0.github.io/education">Education</a>
  <a href="https://cdcastr0.github.io/skills">Skills & Expertise</a>
  <a href="https://cdcastr0.github.io/experience">Experience</a>
  <a href="https://cdcastr0.github.io/projects">Projects</a>
</div>

# Neighborhood Insights

## Overview

A content and data platform for real estate professionals and community researchers. The site publishes in-depth neighborhood analysis across Texas markets, with 43+ articles live. The platform also sells six digital data products via Gumroad and Neura Market.

## What It Does

- **Content hub:** Long-form neighborhood analysis covering demographics, pricing trends, school districts, and investment potential
- **Resources section:** Tools and guides for real estate market research
- **Digital products:** Six downloadable data products (neighborhood comparison tools, market analysis templates, data guides)
- **Gumroad integration:** Products sold via Gumroad API; inventory managed from the codebase

## Technology Stack

| Category | Tools |
|---|---|
| Framework | Next.js 15, React 19, TypeScript |
| Styling | Tailwind v4, custom design system |
| Animation | Framer Motion |
| UI Components | shadcn/ui |
| Commerce | Gumroad API |
| Deployment | Vercel (auto-deploy from GitHub) |

## Architecture Notes

Every route uses a two-file pattern: a server component `page.tsx` that handles data fetching, and a client component `[Name]ClientPage.tsx` marked `"use client"` that handles interactivity. This separates server and client concerns cleanly under Next.js App Router.

The design system uses Tailwind v4's CSS-first configuration — design tokens live in CSS custom properties rather than a JavaScript config file.

---

[GitHub Repository](https://github.com/CDCastr0/v0-neighborhood-insights) | [← Back to Projects](/projects)

<footer class="site-footer">
  <p>&copy; 2025 Christian Castro. All rights reserved.</p>
</footer>
