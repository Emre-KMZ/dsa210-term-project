# **DSA210 Term Project: Weather and Spending Habits Analysis**

Welcome to the GitHub repository for my term project in the DSA210 course. This project focuses on exploring the relationship between weather conditions and my personal spending habits.

---

## **Introduction**
I am **Emre Kırmızı (32364)**, and for my DSA210 term project, I aim to analyze how weather influences my spending habits. Understanding these patterns can offer insights into my behavior and help me make more informed decisions about personal finance and lifestyle adjustments.

### **Hypothesis**
I hypothesize that my spending habits are influenced by weather conditions, particularly that I tend to spend more money on sunny days compared to other weather conditions. By testing this hypothesis, I hope to uncover patterns in my financial behavior linked to external environmental factors.

---

## **Objectives**
1. **Analyze Weather Trends**:
   - Obtain and analyze weather data to identify patterns across different conditions (e.g., sunny, rainy, cold).
   
2. **Examine Spending Behavior**:
   - Investigate daily, weekly, and seasonal trends in spending data from my Akbank and Yapı Kredi accounts.
   
3. **Correlate Weather and Spending**:
   - Explore correlations between specific weather conditions and spending categories (e.g., entertainment, dining, shopping).

4. **Insights and Recommendations**:
   - Provide actionable insights to manage spending more effectively based on weather conditions.

---

## **Data Sources**

### **Weather Data**
- **[OpenWeatherMap API](https://openweathermap.org/api)**:
  - Provides detailed weather data, including temperature, weather conditions, and timestamps.

### **Spending Data**
1. **Akbank Data**:
   - Transaction records categorized by date, type, and amount.
2. **Yapı Kredi Data**:
   - Similar spending data, including detailed descriptions of purchases.

---

## **Data Collection and Preprocessing**
### **Weather Data Collection**:
- Use the OpenWeatherMap API to fetch daily weather data for my location.
- Parse and clean the data to ensure consistency, focusing on parameters like:
  - Date
  - Temperature
  - Weather condition (e.g., sunny, cloudy, rainy)

### **Spending Data Collection**:
- Export transaction history from Akbank and Yapı Kredi banking apps in a digital format (e.g., CSV, Excel).
- Consolidate data from both sources into a single dataset.
- Standardize transaction categories (e.g., groceries, dining, transportation).

### **Data Cleaning**:
- Remove incomplete or irrelevant entries (e.g., salary deposits, monthly fees/subscriptions).
- Synchronize weather and spending datasets by date.

---

## **Methods and Analysis**
### **1. Exploratory Data Analysis (EDA)**
- Visualize spending trends over time.
- Analyze the frequency and distribution of transactions under different weather conditions.
- Identify outliers or anomalies in spending patterns.

### **2. Statistical Analysis**
- Correlation Analysis:
  - Measure the correlation between weather conditions (e.g., sunny, rainy) and total spending.
- Seasonal Trends:
  - Compare spending across different seasons (summer vs. winter).

### **3. Predictive Modeling**
- **Regression Analysis**:
  - Build a regression model to predict daily spending based on weather variables like temperature and weather condition.
- **Classification**:
  - Classify high-spending vs. low-spending days based on weather conditions.

### **4. Visualization**
- Create interactive dashboards to display:
  - Spending trends by weather condition.
  - Seasonal and category-specific spending patterns.
  - Weather-based spending predictions.

---

## **Expected Findings**
- A positive correlation between sunny weather and higher spending, particularly in leisure and outdoor activities.
- Reduced spending during colder or rainy days, possibly with increased transactions in online shopping or entertainment.

---

### Side Note
- I will keep my personal data private and will not commit any sensitive information to this repository. I might use dummy data for demonstration purposes or anonymize the data before sharing them.
---
