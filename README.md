# **DSA210 Term Project: Weather and Spending Habits Analysis**

Welcome to the GitHub repository for my term project in the DSA210 course. This project focuses on exploring the relationship between weather conditions and my personal spending habits.

**NOTE:** Please also check out the source codes for detailed information on implementation, some of the implementation details are overlooked in the report for clarity.

**NOTE:** Due to privacy concerns, I will not share my personal spending data in this repository. However, I have included sample data to demonstrate the structure of the data. [data/yapikredi_formatted/sample_yapikredi_data.csv](data/yapikredi_formatted/sample_yapikredi_data.csv)


---

## **Introduction**
I am **Emre Kırmızı (32364)**, and for my DSA210 term project, I aim to analyze how weather influences my spending habits. Understanding these patterns can offer insights into my behavior and help me make more informed decisions about personal finance and lifestyle adjustments.

### **Hypothesis**
I hypothesize that my spending habits are influenced by weather conditions, particularly that I tend to spend more money days with high temperature, and I tend to spend less on days with precipitation (rain and snow).

---

## **Objectives**
1. **Gather Weather Trends**:
   - Gather weather data to identify patterns across different conditions (e.g., sunny, rainy, cold).
   
2. **Gather Spending Data**:
   - Gather my spending data from my Yapı Kredi account.
   
3. **Analyze Data**:
   - Analyze the data to identify patterns and correlations between weather conditions and my spending habits.
---

## **Data Sources**

### **Weather Data**
- **[Open-Meteo API](https://open-meteo.com)**:
  - Provides detailed weather data, including temperature, weather conditions, and timestamps.

- **[Yapı Kredi](https://yapikredi.com.tr)**:
  - Provides detailed spending data, including transaction dates, descriptions, and amounts.



## **Data Extraction & Preprocessing**

### **Weather Data**
- **[Open-Meteo API](https://open-meteo.com)**:
  - Provides detailed weather data, including temperature, weather conditions, and timestamps.
  - I gathered the weather (mean temperature, rain, snow) data for the interested time period (2024-02-27 to 2024-12-03).
  - Since I was in different locations during different time intervals, I fetched the weather data for each location separately and concatenated them since it would also affect my spending habits:
    - Istanbul: 2024-02-27 to 2024-07-25
    - Bodrum: 2024-07-26 to 2024-07-29 
    - Istanbul: 2024-07-30 to 2024-12-03
  - I converted all the dates to a single integer (as i_th the day of the year 2024) format to have a consistent data format for the dates between the weather and spending data.
  - Check out the implementation [get_weather_data.py](get_weather_data.py).

### **Spending Data**

- **Yapı Kredi Data**:
  - Initially, I was intended to download a formatted data export from Yapı Kredi webapp, but it was not working properly. Then this led me to download my data as multiple PDF files (for each month) and extract the data from the each PDF file then save it as a csv file. It was a tedious process, since PDF files they shared had a lot of formatting issues (Or I was not able to parse the PDF), so I used a regex pattern to extract the data from the PDF file as I have learned in the CS305 course. I stringified the data and ran a regex match on it to extract the data. 
  - I will not share my personal data, but I included a sample data: [sample_yapikredi_data.csv](data/yapikredi_formatted/sample_yapikredi_data.csv)
  - Again, I converted all the dates to a single integer (as i_th the day of the year 2024) format to have a consistent data format for the dates between the weather and spending data.
  - I had a problem with taking the mean total spending per day over temperature intervals, that I explained why it was happening and how I solved it in the [Analysis.ipynb](Analysis.ipynb) file's comments, also I excluded the days that I was abroad when calculating the mean total spending per day over temperature intervals.
  - I did some EDA on the data to see if there are any anomalies in the data, and I found some of them:
    - The transactions that contain "V.D." in the description, these are my tax payments (V.D. = Vergi Dairesi), and they are not related to my spending habits.
    - The transactions that contain "APPLE STORE" in the description were excluded from the analysis. This was because I purchased my phone from the Apple Store, which is a high-value, one-time purchase that is not representative of my regular spending habits. Including such an outlier transaction would significantly skew the analysis of weather's impact on my typical daily spending patterns.
    - The transactions that contain "AJET" in the description were excluded from the analysis. These are flight ticket purchases which, like the Apple Store purchase, represent large, planned expenditures that are typically booked well in advance and are not influenced by day-to-day weather conditions. Including these transactions would distort the analysis of weather's impact on daily spending patterns.
    - The transactions that contain "SPOTIFY" in the description were excluded from the analysis. These are my monthly subscription payments to Spotify, which occur automatically on a fixed schedule regardless of weather conditions. Including these transactions would not provide meaningful insights into how weather affects my spending decisions since they are pre-scheduled, automated payments.
  - Check out the [data_fetch_yapikredi.py](data_fetch_yapikredi.py) for implementation details.

