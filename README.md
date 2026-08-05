# HR Workforce Analytics Dashboard

A full-cycle HR analytics project combining **Python** (data cleaning & feature engineering) with **Power BI** (interactive 4-page dashboard) to analyze workforce composition, Saudization progress, attrition, and recruitment performance — aligned with Saudi Vision 2030 localization goals.

## 🎯 Project Overview

This dashboard analyzes a dataset of **929 employees** across 5 departments (Operations, IT, Finance, Sales, HR), tracking:
- Workforce demographics and composition
- Saudization rate vs. Vision 2030 target (75%)
- Employee attrition patterns and exit reasons
- Recruitment funnel performance

## 🛠 Tools & Tech Stack

- **Python** (pandas) — data cleaning, feature engineering, KPI pre-calculation
- **Power BI** — data modeling, DAX measures, interactive visualization
- **DAX** — custom measures for rates, dynamic KPIs, and comparative metrics
- **Power Query** — data transformation and column sorting logic

## 📊 Dashboard Pages

### 1. Overview
Company-wide KPIs: total headcount, Saudization rate, attrition rate, average salary — plus breakdowns by department, gender, age, performance, and salary bands.

### 2. Saudization
Department-level Saudization rates benchmarked against the Vision 2030 target (75%), plus a full nationality breakdown of the workforce.

### 3. Attrition
Attrition rate, exit reasons, average age at exit, exit interview completion rate, and a Saudi vs. non-Saudi leaver comparison.

### 4. Recruitment
Open positions, applicant volume, hiring funnel (applied → screened → interviewed → hired), and average time-to-hire.

## 🐍 Python Data Pipeline

The `hr_cleaning.py` script:
- Cleans and standardizes raw HR data (dates, text fields, numeric precision)
- Engineers 7+ new features: age groups, salary bands, performance labels, experience categories, Saudization flags
- Calculates department-level Saudization percentages
- Exports a Power BI–ready cleaned dataset

## 📈 Key DAX Measures

```dax
Saudization Rate = AVERAGE(Employees_Cleaned[is_saudi])

Attrition Rate = 
DIVIDE(COUNTROWS(Attrition), COUNTROWS(Employees_Cleaned)) * 100

Exit Interview Rate = 
DIVIDE(
    CALCULATE(COUNTROWS(Attrition), Attrition[exit_interview_done] = "Yes"),
    COUNTROWS(Attrition)
)
```

## 🇸🇦 Vision 2030 Alignment

Saudization tracking is built as a core analytical thread throughout the dashboard — comparing department-level localization rates against the national 75% target, supporting workforce planning decisions relevant to Saudi labor market priorities.

## 📁 Repository Structure

```
├── hr_cleaning.py              # Python data cleaning & feature engineering script
├── HR_Workforce_Analytics.xlsx # Raw source data
├── HR_Cleaned.xlsx             # Cleaned, feature-engineered output
└── screenshots/                # Dashboard page screenshots
```

## 🔗 Live Dashboard

The interactive Power BI dashboard is not hosted in this repository. You can view it here: **[Power BI Dashboard Link](https://app.powerbi.com/view?r=eyJrIjoiZjAzZjNiNjEtMWI1Ni00NzRmLThmYmYtZjYyZmNjMzI1MjcxIiwidCI6IjliMDk4M2ViLThmNjQtNGZmZS1hNDk5LWRkYzU3MzUzYjZhMiIsImMiOjl9)**


## 🚀 How to Run the Python Pipeline

1. Install dependencies: `pip install pandas openpyxl`
2. Run the cleaning script: `python hr_cleaning.py`
3. This generates `HR_Cleaned.xlsx`, ready to be loaded into Power BI

---

*Built as a portfolio project demonstrating end-to-end HR analytics: from raw data to actionable, decision-ready dashboards.*
