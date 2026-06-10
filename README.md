Kobo-to-PowerBI-Pipeline-MEL
Overview

This project demonstrates an end-to-end Monitoring, Evaluation and Learning (MEL) reporting pipeline for a humanitarian NGO operating in Eastern Democratic Republic of Congo.

The objective is to automate the reporting process from KoboToolbox data collection to Power BI dashboards.

The project uses synthetic data and does not contain any real beneficiary information.

Business Context

An NGO conducts Non-Food Item (NFI) distributions for internally displaced households in:

Goma
Nyiragongo
Rutshuru
Masisi

Field teams collect data using KoboToolbox.

The reporting process is often manual:

CSV exports
Excel cleaning
Manual consolidation
Delayed reporting

This project proposes an automated solution.

Problem Statement

The manual process creates:

Reporting delays
Data quality issues
Duplicate records
Difficult donor reporting
High workload for MEL teams
Proposed Solution

KoboToolbox

↓

Python Data Processing

↓

Data Quality Checks

↓

SQLite Database

↓

Power BI Dashboard

↓

Decision Making

Project Objectives
Automate data extraction
Standardize data cleaning
Improve data quality
Reduce reporting delays
Create reliable dashboards
Support evidence-based decisions
Technologies Used
Python
Pandas
SQLite
SQL
Power BI
GitHub
Project Structure

data/
Raw and processed datasets

docs/
Business documentation

sql/
Database scripts

src/
Python scripts

powerbi/
Dashboard files

screenshots/
Project screenshots

Key Performance Indicators (KPIs)
MEL Indicators
Households reached
Individuals reached
Distribution coverage
Distribution trends
Data Quality Indicators
Missing values
Duplicate records
Reporting delays
Validation pass rate
Expected Results

The project demonstrates how an NGO can:

Improve reporting quality
Reduce manual work
Increase transparency
Strengthen donor reporting
Data Privacy

All datasets are synthetic.

No real beneficiary information is included.

Author

Portfolio project developed for Data Analytics, MEL and Information Management positions within NGOs, international organizations and development programs.