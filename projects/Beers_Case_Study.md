---
layout: default
title: Beer Case Study
---

<a href="/" class="back-link"><span>&larr;</span> Back to Home</a>

# Beer Case Study

## Overview

In this data analysis project, I worked with a partner to analyze beer market data to provide strategic insights for Budweiser. The goal was to understand brewing patterns, consumer preferences, and identify market opportunities through detailed examination of ABV (Alcohol By Volume) and IBU (International Bitterness Units) metrics across different states and beer styles.

## Challenge

Budweiser wanted to gain competitive insights about the craft beer market to identify:
- Regional preferences and patterns in beer characteristics
- Relationships between beer bitterness and alcohol content
- Market positioning opportunities based on data analysis
- Distinguishing factors between IPAs and other Ale styles

## Approach

Our analysis included:

1. **Data Cleaning and Preparation**: We addressed missing values in the dataset, particularly in the ABV and IBU columns. We implemented two different imputation methods:
   - Median imputation for IBU values where ABV was present
   - Linear regression-based imputation by leveraging the correlation between ABV and IBU

2. **Geographic Analysis**: We mapped the brewery distribution across states and calculated median ABV and IBU values for each state to identify regional preferences. Colorado stood out with 47 breweries, while some states like DC and West Virginia had only one.

3. **Statistical Analysis**: We examined the relationship between alcohol content and bitterness through correlation tests and visualization techniques including scatter plots, histograms, and density heat maps.

4. **Machine Learning**: We employed K-Nearest Neighbors (KNN) classification to distinguish between IPAs and other Ales based on their ABV and IBU characteristics, running 1,000 iterations with different random seeds to ensure robust results.

## Key Findings

### Regional Patterns

- Colorado had the highest number of breweries (47)
- West Virginia showed the highest median IBU (bitterness) levels at approximately 58 IBU
- DC and Kentucky featured beers with the highest median alcohol content at 6.2% ABV
- Utah had the lowest median ABV at 4.0%, likely due to state regulations
- Kansas had the lowest median IBU at 22

### Notable Statistics

- The beer with the highest alcohol content (12.8% ABV) was Lee Hill Series Vol. 5 Belgian Style Quadrupel Ale from Upslope Brewing Company in Colorado
- Oregon produced the most bitter beer with an IBU rating of 138 (Bitter Bitch Imperial IPA from Astoria Brewing Company)
- We discovered a strong positive correlation (0.67) between alcohol content and bitterness, with a p-value of 2.2e-16 confirming statistical significance

### Market Insights

Through density analysis, we identified two underserved market segments:
1. Beers with approximately 5% ABV and IBU under 25
2. Beers with ABV around 7.5% and IBU slightly under 75

Our machine learning model achieved 81% accuracy in distinguishing IPAs from other Ales using only ABV and IBU values, demonstrating that these two metrics are strong predictors of beer style. The model showed 73% sensitivity (correctly identifying IPAs) and 86.5% specificity (correctly identifying other ales).

## Impact

This analysis provided Budweiser with actionable insights to:
- Target specific regional markets with appropriate beer profiles
- Identify potential gaps in the market for new product development
- Better position marketing strategies for different beer styles, such as marketing certain non-IPAs to IPA lovers based on their similar ABV and IBU profiles
- Understand the technical relationships between beer characteristics

## Visualization Techniques

Throughout this project, we employed various visualization methods to extract insights:
- Bar charts showing brewery counts and median metrics by state
- Scatter plots revealing the correlation between ABV and IBU
- Histograms displaying the distribution of alcohol content
- Density heat maps identifying popular combinations of bitterness and alcohol levels
- Missing data visualizations to inform our imputation strategy

## Tools Used

- R for statistical analysis and visualization
- ggplot2 for data visualization
- K-Nearest Neighbors for classification
- Linear regression for data imputation
- naniar package for missing data analysis
- tidyverse for data manipulation

<div class="project-links">
  <a href="https://github.com/CDCastr0/Beer-Data-Analysis" target="_blank">View Code Repository</a>
</div> 