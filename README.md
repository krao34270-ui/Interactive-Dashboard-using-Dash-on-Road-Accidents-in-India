#  Road Accidents in India (2014–2017)

An interactive data visualization dashboard built using **Python, Pandas, Plotly, Dash, and Dash Bootstrap Components** to analyze road accident injury data across Indian States and Union Territories from **2014 to 2017**.

The project focuses on identifying highly affected regions, analyzing year-wise trends, comparing states, examining population- and vehicle-based injury rates, and presenting the findings through interactive visualizations.

---
##  Project Overview

Road accidents are a major public safety concern in India, resulting in significant injuries, fatalities, and economic losses.

This project analyzes historical road accident injury data for Indian States and Union Territories from **2014–2017** and presents the results through an interactive web dashboard.

The dashboard helps answer questions such as:

- Which States/UTs have the highest number of road accident injuries?
- How did injuries change between 2014 and 2017?
- Which states have the highest injury rates per lakh population?
- Which states have the highest injury rates per 10,000 vehicles?
- What relationships exist between the numerical variables in the dataset?
- Which states experienced the largest increase or decrease in injuries?

---

##  Features

###  Interactive Dashboard

- Interactive web dashboard built with **Plotly Dash**
- Dark-themed interface using the **Cyborg** Bootstrap theme
- Dynamic year selection
- State comparison
- Interactive Plotly charts
- Automatically generated insights

### Multi-Year Analysis

The dashboard supports analysis for:

- 2014
- 2015
- 2016
- 2017

Users can select a year and dynamically update the dashboard statistics and visualizations.

###  State-wise Comparison

Users can select multiple States/UTs and compare their injury trends across the four-year period.

The line chart displays up to four selected states simultaneously for easier comparison.

###  Key Performance Indicators

The dashboard displays four KPIs for the selected year:

- **Total Persons Injured**
- **Most Affected State**
- **Highest per Lakh Population**
- **Highest per 10,000 Vehicles**
 
###  Interactive Visualizations

The dashboard contains:

- **Bar Chart** — State-wise total injuries
- **Pie Chart** — Top 8 states' share of injuries
- **Line Chart** — Year-wise injury trends for selected states
- **Correlation Heatmap** — Correlations between numerical variables

###  Automated Insights

The dashboard generates:

- Top 5 states based on cumulative injuries from 2014–2017
- State with the highest increase between 2014 and 2017
- State with the highest decrease between 2014 and 2017

---

##  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading, cleaning, and manipulation |
| NumPy | Numerical operations |
| Plotly Express | Interactive visualizations |
| Plotly Graph Objects | Custom interactive charts |
| Dash | Web dashboard framework |
| Dash Bootstrap Components | Dashboard layout and styling |

---

##  Project Structure

```text
Road-Accidents-in-India/
│
├── app.py
├── Road_Accidents_2017-Annuxure_Tables_4.csv
├── README.md
└── Project_documentaion.docx
```

### Main Files

| File | Description |
|---|---|
| `app.py` | Main Dash application |
| `Road_Accidents_2017-Annuxure_Tables_4.csv` | Road accident dataset used by the dashboard |
| `Project_documentaion.docx` | Detailed academic project documentation |
| `README.md` | Project documentation |

---

##  Dataset

The project uses the **Road Accidents in India (2014–2017)** dataset.

The dataset contains State/UT-wise information related to road accident injuries, including:

- Total number of persons injured
- Share of States/UTs in total injuries
- Injuries per lakh population
- Injuries per 10,000 vehicles
- Other numerical accident-related metrics

### Dataset Source

**Kaggle — Road Accidents in India (2014–2017)**

https://www.kaggle.com/datasets/greeshmagirish/road-accidents-in-india-20142017

---

##  Data Preprocessing

The application performs several preprocessing steps before analysis.

### 1. Dataset Validation

The application checks whether the required CSV file exists in the same directory as `app.py`.

### 2. Column Cleaning

Whitespace is removed from column names and State/UT names.

### 3. Numeric Conversion

Numerical columns are converted using Pandas, with invalid values handled as missing values.

### 4. Metric Identification

The application identifies columns corresponding to:

- Total number of persons injured
- State/UT share
- Injuries per lakh population
- Injuries per 10,000 vehicles

### 5. Year Extraction

The application extracts the available years from the relevant dataset columns.

The current analysis covers **2014–2017**.

---

## KPI Calculation

For the selected year, the application calculates the following metrics.

### Total Persons Injured

The total number of injured persons is calculated by summing the corresponding injury values across the dataset.

### Most Affected State

The State/UT with the highest number of injured persons for the selected year is identified.

### Highest per Lakh Population

The State/UT with the highest injury value per lakh population is identified.

### Highest per 10,000 Vehicles

The State/UT with the highest injury value per 10,000 vehicles is identified.

---

##  Visualizations

### 1. Bar Chart

Displays the total number of persons injured for every State/UT for the selected year.

```text
Total Injuries by State - Selected Year
```

The states are sorted according to their injury counts.

### 2. Pie Chart

Displays the contribution of the **top 8 States/UTs** to the total injuries for the selected year.

### 3. Line Chart

Displays year-wise injury trends for selected States/UTs from **2014 to 2017**.

Users can select multiple states for comparison.

### 4. Correlation Heatmap

A correlation matrix is calculated using the numerical columns of the dataset.

The resulting heatmap provides a visual representation of relationships between the numerical variables.

---

##  Automated Insights

The dashboard automatically calculates additional insights across the complete 2014–2017 period.

### Top 5 States

The application calculates cumulative injuries across all four years and identifies the top five States/UTs.

### Highest Increase

The dashboard compares injury values between 2014 and 2017 and identifies the State/UT with the highest increase.

### Highest Decrease

The same comparison identifies the State/UT with the largest decrease between 2014 and 2017.

---

##  System Architecture

```text
                    ┌──────────────────────┐
                    │      CSV Dataset     │
                    │      2014–2017       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Data Loading      │
                    │      Pandas          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Data Preprocessing   │
                    │ Cleaning & Conversion│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Analysis & KPIs    │
                    │ Trends & Risk Rates │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │  Visualizations │        │    Insights     │
        │ Plotly + Dash   │        │   Automated     │
        └────────┬────────┘        └────────┬────────┘
                 │                           │
                 └─────────────┬─────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Interactive Dashboard│
                    └──────────────────────┘
```

---

##  Requirements

### Software Requirements

- Python 3.x
- Web browser
- pip

### Python Libraries

- pandas
- numpy
- plotly
- dash
- dash-bootstrap-components

### Hardware Requirements

The project documentation specifies:

- Processor: Intel i3/i5/i7 or equivalent
- RAM: Minimum 4 GB, 8 GB recommended
- Storage: At least 200 MB free
- Display: 1366×768 or higher
- Internet connection for package installation

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace `YOUR-USERNAME/YOUR-REPOSITORY` with the actual GitHub repository path.

### 2. Install Dependencies

```bash
pip install pandas numpy plotly dash dash-bootstrap-components
```

Alternatively, create a `requirements.txt` file containing:

```text
pandas
numpy
plotly
dash
dash-bootstrap-components
```

Then install:

```bash
pip install -r requirements.txt
```

### 3. Verify the Dataset

Make sure the following files are in the same directory:

```text
app.py
Road_Accidents_2017-Annuxure_Tables_4.csv
```

The application expects the dataset at:

```text
Road_Accidents_2017-Annuxure_Tables_4.csv
```

### 4. Run the Application

```bash
python app.py
```

The Dash development server runs on:

```text
http://127.0.0.1:8050/
```

Open the address in your web browser to access the dashboard.

---

##  Dashboard Layout

The dashboard is organized into four major sections:

```text
┌──────────────────────────────────────────────────────────┐
│               Road Accidents in India                   │
│                       2014–2017                          │
├──────────────────────────────────────────────────────────┤
│ Year Selection │ State Comparison │ Dashboard Controls  │
├──────────────────────────────────────────────────────────┤
│ Total Injured │ Most Affected │ Per Lakh │ Per Vehicle  │
├────────────────────────────┬─────────────────────────────┤
│                            │                             │
│       Bar Chart            │        Pie Chart            │
│                            │                             │
├────────────────────────────┼─────────────────────────────┤
│                            │                             │
│       Line Chart           │    Correlation Heatmap     │
│                            │                             │
├────────────────────────────┴─────────────────────────────┤
│                    Quick Insights                        │
└──────────────────────────────────────────────────────────┘
```

---

##  Project Objectives

The main objectives of the project are:

1. Analyze road accident injury data across Indian States and Union Territories.
2. Study injury trends between 2014 and 2017.
3. Identify highly affected states.
4. Compare injury levels across different states.
5. Analyze population-based injury rates.
6. Analyze vehicle-based injury rates.
7. Identify relationships between numerical variables.
8. Provide an interactive platform for exploring the dataset.
9. Generate data-driven insights from historical accident data.

---

##  Key Outcomes

The project successfully:

- Analyzed road accident injury data from 2014–2017
- Identified highly affected States/UTs
- Provided year-wise injury comparisons
- Calculated population- and vehicle-based injury metrics
- Created interactive visualizations
- Generated automated analytical insights
- Provided a scalable dashboard for exploring accident data

---

## Future Enhancements

The project documentation identifies several possible future improvements:

- Add road accident fatality data
- Include accident causes
- Integrate real-time API-based accident reporting
- Use machine learning to predict accident hotspots
- Add interactive GIS maps with precise state boundaries
- Include road type information
- Include weather conditions
- Include vehicle category information
- Add additional accident-related metrics
- Extend the analysis to newer years

---

##  Academic Project

This project was developed as a mini project at:

**SR University**  
School of Computer Science and Artificial Intelligence  
Ananthasagar, Warangal, Telangana, India

### Project Team

- **Bandi Sreesaicharan**
- **Sriram Sushanth**
- **Sandela Navatej Varma**
- **Rayella Dinesh Babu**

### Project Guide

**Mr. N. Venkatesh**  
Assistant Professor  
School of Computer Science and Artificial Intelligence  
SR University

---

##  References

1. **Kaggle — Road Accidents in India (2014–2017)**  
   https://www.kaggle.com/datasets/greeshmagirish/road-accidents-in-india-20142017

2. **Python Software Foundation**  
   https://www.python.org/

3. **Pandas Documentation**  
   https://pandas.pydata.org/

4. **Plotly Python Documentation**  
   https://plotly.com/python/

5. **Dash Documentation**  
   https://dash.plotly.com/

---

##  License

This project was developed for academic and educational purposes.
