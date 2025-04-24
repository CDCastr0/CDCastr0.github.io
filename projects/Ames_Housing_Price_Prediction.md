---
layout: default
title: Ames Housing Price Prediction
---

<a href="/" class="back-link"><span>&larr;</span> Back to Home</a>

# Ames Housing Price Prediction

## Overview

In this project, I worked with a partner to develop predictive models for housing prices in Ames, Iowa for Century 21 Ames. We explored various approaches to determine the most accurate model for predicting sale prices, leveraging statistical techniques and machine learning to identify key factors influencing home values.

## Challenge

The real estate market requires accurate property valuation for both buyers and sellers. Our analysis needed to:
- Determine which variables most significantly impact home sale prices
- Create models with minimal prediction error (measured by RMSE)
- Provide practical insights for real estate professionals 
- Build an interactive tool for exploring property valuations

## Approach

We undertook two parallel modeling approaches:

### Approach 1: Neighborhood-Specific Model

We focused on three specific neighborhoods (NAmes, Edwards, BrkSide) to investigate how square footage and location influence home prices:

1. **Data Preparation**: We cleaned the dataset, removing outliers identified through diagnostic plots and Cook's distance metrics
2. **Linear Regression**: Developed a model using the formula `SalePrice ~ GrLivArea * Neighborhood` to capture both main effects and interactions
3. **Model Validation**: Verified linear regression assumptions through residual analysis and diagnostic plots
4. **Performance Evaluation**: Assessed model performance using adjusted R², CV PRESS, and confidence intervals

### Approach 2: Comprehensive Model Selection

We created three competing models for all Ames neighborhoods:

1. **Simple Linear Regression**: Used log-transformed year built as a predictor
2. **Multiple Linear Regression**: Combined above-ground living area (GrLivArea) and bathroom count (FullBath)
3. **Custom MLR Model**: Incorporated lot area, living area, land contour, and land slope with relevant interaction terms

Each model was evaluated using adjusted R², cross-validation PRESS, and Kaggle score to determine the optimal predictive performance.

## Key Findings

### Neighborhood-Specific Analysis

- The interaction between living area and neighborhood significantly influences housing prices
- In BrkSide, homes start at a baseline of about $20,000 with an $8,716 increase per 100 square feet
- Edwards neighborhood homes start at $68,382 with a $2,975 increase per 100 square feet
- NAmes properties start at $54,705 with a $5,432 increase per 100 square feet
- The model explained 44.7% of price variance (adjusted R² = 0.44)

### Comprehensive Model Analysis

Our custom MLR model outperformed both the simple linear regression and the provided multiple regression model:

| Model | Adjusted R² | CV PRESS | Kaggle Score |
|-------|------------|----------|--------------|
| Simple Linear Regression | 0.270 | 153.891 | 0.33906 |
| Multiple Linear Regression | 0.523 | 4.43×10¹² | 0.28586 |
| Custom MLR Model | 0.571 | 4.09×10¹² | 0.28449 |

Key insights from our custom model:
- Properties with banked land contours (sharp rise from street grade) sell for significantly less despite large lot sizes
- Moderate and severe land slopes negatively impact property values
- The interaction between living area and land characteristics proved highly significant

## Impact

Our analysis provided Century 21 Ames with:
- Accurate price prediction models for different neighborhoods
- Clear understanding of how property features affect sale prices
- Insights into the impact of lot characteristics (contour, slope) on property valuation
- Tools for estimating property values based on measurable characteristics

## Technical Implementation

We developed an interactive RShiny application that allows real estate professionals to:
- Visualize the relationship between living area and sale price by neighborhood
- Add trend lines to better understand pricing patterns
- Explore different property characteristics and their impact on valuation

The app provides an intuitive interface for exploring housing data and making data-driven decisions in real estate transactions.

## Tools Used

- R for statistical analysis and modeling
- Linear and multiple regression techniques
- RShiny for interactive visualization
- Cross-validation for model validation
- SAS for calculating CV PRESS statistics

<div class="project-links">
  <a href="https://amaxpagan.shinyapps.io/RShinyApp/" target="_blank">View Interactive App</a>
  <a href="https://github.com/CDCastr0/Ames-Housing-Analysis" target="_blank">View Code Repository</a>
</div> 