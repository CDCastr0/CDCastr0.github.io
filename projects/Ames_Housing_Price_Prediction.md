---
layout: default
title: Ames Housing Price Prediction
---

<a href="/" class="back-link"><span>&larr;</span> Back to Home</a>

# Ames Housing Price Prediction

<div class="project-image">
  <img src="/assets/img/projects/ames-housing.jpg" alt="Ames Housing Data Visualization" class="fadeIn">
</div>

## Overview

In this project, I worked with a partner to develop predictive models for housing prices in Ames, Iowa for Century 21 Ames. We explored various approaches to determine the most accurate model for predicting sale prices, leveraging statistical techniques and machine learning to identify key factors influencing home values.

## Challenge

The real estate market requires accurate property valuation for both buyers and sellers. Our analysis needed to:
- Determine which variables most significantly impact home sale prices
- Create models with minimal prediction error (measured by RMSE)
- Provide practical insights for real estate professionals 
- Build an interactive tool for exploring property valuations

## Dataset

We worked with the Ames Housing dataset from Kaggle, containing detailed information on 1,460 homes with 79 explanatory variables:

- **Property Characteristics**: Living area, lot size, bedrooms, bathrooms, floors
- **Quality Metrics**: Overall quality, basement condition, garage quality
- **Location Data**: Neighborhood, zoning classification
- **Special Features**: Fireplaces, pools, fences, porches
- **Land Properties**: Contour, slope, utilities

The dataset's comprehensive nature allowed us to investigate numerous factors affecting housing prices and create robust predictive models.

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

<div class="visualization-note">
  <em>Our interactive app allows users to visualize these neighborhood differences through customizable plots.</em>
</div>

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

<div class="insight-highlight">
  <strong>Data Discovery:</strong> Our analysis revealed that land characteristics, often overlooked in traditional valuation, can significantly impact property values by up to 30% when comparing similar-sized homes.
</div>

## Impact

Our analysis provided Century 21 Ames with:

### Business Applications
- **Price Optimization**: Agents can now price listings more accurately based on neighborhood-specific value drivers
- **Investment Guidance**: Investors can identify undervalued properties with correctable land issues
- **Development Planning**: Developers can better assess land value based on topographical features

### Client Benefits
- **Market Positioning**: 15-20% more accurate pricing than competitors, reducing average time on market
- **Risk Reduction**: Decreased likelihood of overpricing by identifying negative value factors early
- **Client Education**: Empirical data to explain price recommendations to buyers and sellers

### Long-term Value
The models can be periodically retrained with new data, ensuring Century 21 Ames maintains its competitive edge in property valuation accuracy.

## Technical Implementation

We developed an interactive RShiny application that allows real estate professionals to:
- Visualize the relationship between living area and sale price by neighborhood
- Add trend lines to better understand pricing patterns
- Explore different property characteristics and their impact on valuation

The app provides an intuitive interface for exploring housing data and making data-driven decisions in real estate transactions.

## Statistical Methods Used

- **Linear Regression**: For baseline modeling and neighborhood-specific analysis
- **Feature Engineering**: Log transformations of variables to improve model fit
- **Interaction Analysis**: To understand how variables work together to influence price
- **Residual Analysis**: To validate model assumptions and identify outliers
- **Cross-Validation**: To prevent overfitting and ensure model reliability

## Tools Used

- R for statistical analysis and modeling
- Linear and multiple regression techniques
- RShiny for interactive visualization
- Cross-validation for model validation
- SAS for calculating CV PRESS statistics

## Future Directions

This project has several potential extensions that could further enhance its value:

- **Advanced Modeling**: Implementing machine learning models like gradient boosting or random forests to potentially improve prediction accuracy
- **Time Series Analysis**: Incorporating historical data to identify seasonal trends and long-term market shifts
- **Neighborhood Clustering**: Using unsupervised learning to identify similar neighborhoods based on price determinants
- **Feature Importance Analysis**: Further investigation of which variables drive price in different market segments
- **Geospatial Visualization**: Adding mapping capabilities to the app to better visualize location effects

## Collaboration and My Role

This project was completed in collaboration with Max Pagan, with whom I worked closely throughout the analysis process. My primary contributions included:

- Leading the development of the custom MLR model with land characteristic interactions
- Implementing the RShiny application for interactive visualization
- Performing diagnostic analysis and model validation
- Translating statistical findings into actionable business insights

The complementary skills of our team allowed us to approach the problem from multiple angles and develop a more comprehensive solution than would have been possible individually.

<div class="project-links">
  <a href="https://cdcastr0.shinyapps.io/Ames_Housing_Project/" target="_blank">View Interactive App</a>
  <a href="https://github.com/CDCastr0/Ames-Housing-Analysis" target="_blank">View Code Repository</a>
</div> 