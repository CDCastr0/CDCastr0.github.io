---
layout: default
title: Misinformation Matrix
---

<a href="/projects" class="back-link"><span>&larr;</span> Back to Projects</a>

<div class="navigation-links">
  <a href="https://cdcastr0.github.io/">Home</a>
  <a href="https://cdcastr0.github.io/education">Education</a>
  <a href="https://cdcastr0.github.io/skills">Skills & Expertise</a>
  <a href="https://cdcastr0.github.io/experience">Experience</a>
  <a href="https://cdcastr0.github.io/projects">Projects</a>
</div>

# Misinformation Matrix

*"The dumbing down of America is most evident in the slow decay of substantive content..."*  
— Carl Sagan, The Demon-Haunted World

## Overview

An interactive educational platform designed to make the spread of misinformation visible and emotionally resonant. The project combines network graph analysis with generative art to reach audiences that data alone can't move.

## Features

### Misinformation Network Map
An interactive network diagram where:
- **Nodes** represent social media accounts, disinformation websites, and influential figures
- **Node size** encodes influence level — larger nodes have wider reach
- **Link weight** represents misinformation sharing frequency between nodes
- **Node detail panels** show content type (conspiracy theories, pseudoscience, etc.) and sample shared posts

Clicking a node expands its connections and reveals sharing patterns, making the structural anatomy of a misinformation campaign tangible.

### Generative Art — "Knowledge to Darkness"
Built with p5.js, this piece evolves through three states in response to user interaction:
1. **Initial state:** A vivid cityscape — progress, knowledge, science
2. **Transformation:** Gradual distortion, desaturation, introduction of pseudoscience imagery
3. **Final state:** An abstract landscape of distorted forms and superstition symbols

Interacting with high-influence misinformation nodes in the network map accelerates the art piece's transformation — making the causal relationship visible.

### "Reality vs. Perception" Decision Tree
An interactive fact-checking guide that walks users through critical evaluation questions for any piece of information they encounter. Designed to be a practical tool, not just a visualization.

## Technology Stack

| Category | Tools |
|---|---|
| Generative Art | p5.js |
| Network Visualization | D3.js, force-directed graphs |
| Frontend | HTML5, CSS3, JavaScript |
| Audio Layer | Web Audio API |

## Design Philosophy

The dual-display approach (network map + generative art side-by-side) addresses two different audience responses to misinformation: the analytical (who responds to data and evidence) and the emotional (who responds to narrative and imagery). Cross-linking the two displays makes the abstract structural problem of misinformation personally felt.

**Target audience:** Students, young adults, educators, and researchers studying media literacy.

---

[GitHub Repository](https://github.com/CDCastr0/MisinformationMatrix) | [← Back to Projects](/projects)

<footer class="site-footer">
  <p>&copy; 2025 Christian Castro. All rights reserved.</p>
</footer>
