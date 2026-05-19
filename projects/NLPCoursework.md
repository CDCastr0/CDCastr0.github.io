---
layout: default
title: NLP Coursework — Natural Language Processing
---

<a href="/projects" class="back-link"><span>&larr;</span> Back to Projects</a>

<div class="navigation-links">
  <a href="https://cdcastr0.github.io/">Home</a>
  <a href="https://cdcastr0.github.io/education">Education</a>
  <a href="https://cdcastr0.github.io/skills">Skills & Expertise</a>
  <a href="https://cdcastr0.github.io/experience">Experience</a>
  <a href="https://cdcastr0.github.io/projects">Projects</a>
</div>

# NLP Coursework

**SMU MSDS — Natural Language Processing**

## Overview

Eight progressive homework assignments covering foundational and applied NLP techniques. Dataset sources include Project Gutenberg classic literature and 150 live-scraped IMDb movie reviews across three genres.

## Assignments

### HW1 — Lexical Diversity Analysis
Implemented a lexical diversity scoring function (unique words / total words) and applied it to Project Gutenberg texts at different grade levels. Compared vocabulary richness across elementary, middle school, and college-level texts using matplotlib visualizations.

### HW2–4 — Core NLP Fundamentals
Tokenization with NLTK word_tokenize, stopword filtering, frequency distributions, and n-gram analysis. Built text cleaning pipelines that remove punctuation and normalize case before analysis.

### HW5 — Web Scraping + POS Tagging
Scraped 150 IMDb reviews across three genres (Baby Driver, Fast & Furious, third genre) using BeautifulSoup and requests. Applied NLTK POS tagging and RegexpParser to extract noun phrases and identify genre-specific vocabulary patterns.

### HW6 — Text Similarity with TF-IDF
Collected 24 Amazon book titles (machine learning category) and search engine queries. Vectorized with TfidfVectorizer and CountVectorizer, then computed pairwise cosine similarity to find the most semantically similar documents.

### HW7 — Named Entity Recognition & Normalization
Applied NLTK named entity chunking, compared PorterStemmer vs. WordNetLemmatizer on the same corpus, and evaluated how each normalization strategy affects downstream similarity scores.

### HW8 — Sentiment Analysis with VADER
Used VADER (Valence Aware Dictionary and sEntiment Reasoner) to score all 150 IMDb reviews. Aggregated compound sentiment scores by movie and genre with pandas, visualized distributions with matplotlib and seaborn.

## Technology Stack

| Category | Tools |
|---|---|
| Core NLP | NLTK, VADER, RegexpParser |
| Vectorization | TfidfVectorizer, CountVectorizer |
| Data | pandas, numpy |
| Web Scraping | BeautifulSoup, requests |
| Visualization | matplotlib, seaborn |
| Similarity | scikit-learn (cosine_similarity) |

## Key Takeaways

- TF-IDF outperforms raw frequency counts for document similarity when corpus size varies significantly
- VADER performs well on informal, short review text; less reliable on formal academic prose
- POS tagging reveals genre-specific language patterns (action films: more motion verbs; documentaries: more nominalization)
- Lexical diversity is a fast, interpretable baseline metric for text complexity

---

[GitHub Repository](https://github.com/CDCastr0/NLP_Coursework) | [← Back to Projects](/projects)

<footer class="site-footer">
  <p>&copy; 2025 Christian Castro. All rights reserved.</p>
</footer>
