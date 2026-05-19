---
layout: default
title: Dallas ZIP Code Demographics Dataset
---

<a href="/projects" class="back-link"><span>&larr;</span> Back to Projects</a>

<div class="navigation-links">
  <a href="https://cdcastr0.github.io/">Home</a>
  <a href="https://cdcastr0.github.io/education">Education</a>
  <a href="https://cdcastr0.github.io/skills">Skills & Expertise</a>
  <a href="https://cdcastr0.github.io/experience">Experience</a>
  <a href="https://cdcastr0.github.io/projects">Projects</a>
</div>

# Dallas ZIP Code Demographics Dataset

## Overview

A Python data engineering project that compiles American Community Survey (ACS) Census data from multiple tables into a single unified master dataset at the ZIP code level. Built to support Dallas real estate market analysis and neighborhood research.

## The Problem

The Census Bureau publishes ACS data as separate table downloads — one CSV per topic (income, housing, demographics, commuting, etc.), each with cryptic column codes and companion metadata files. Merging these into something usable requires understanding the data structure and building a repeatable pipeline.

## Solution

A Python script that:
1. Discovers all `*-Data.csv` files in the download directory using `glob`
2. For each table, reads the companion `*-Column-Metadata.csv` to map column codes to human-readable labels
3. Extracts ZIP code from the `GEO_ID` field (last 5 digits)
4. Renames columns using a `table_prefix: description (Estimate/Margin of Error)` format
5. Merges all tables on ZIP using `functools.reduce` — scalable to any number of tables

## Output

`Dallas_Master_Dataset.csv` — a single wide-format table with:
- One row per Dallas ZIP code
- Columns from all ACS tables, clearly labeled
- Separate Estimate and Margin of Error columns for statistical reliability assessment

## Technology Stack

| Category | Tools |
|---|---|
| Data Processing | Python, pandas |
| File Discovery | glob, os.path |
| Merge Pattern | functools.reduce |
| Data Source | U.S. Census Bureau ACS |

## Key Design Decisions

**Metadata-driven labeling:** Rather than hardcoding column names, the script reads Census metadata files at runtime. Adding a new ACS table to the analysis requires zero code changes — just drop the files in the directory.

**Estimate vs. MOE separation:** ACS estimates always come with margins of error at 90% confidence. Keeping these as distinct columns lets downstream users filter out unreliable estimates from small-population ZIP codes.

---

[GitHub Repository](https://github.com/CDCastr0/DallasDataset) | [← Back to Projects](/projects)

<footer class="site-footer">
  <p>&copy; 2025 Christian Castro. All rights reserved.</p>
</footer>
