# KPI Reference Guide

## Purpose

This document defines all key performance indicators (KPIs) used in the project.

The objective is to ensure that all stakeholders use the same definitions when interpreting reports and dashboards.

---

# KPI 1 – Households Reached

## Definition

Number of unique households that received assistance during the reporting period.

## Formula

Count distinct beneficiary_uid

## Data Source

Kobo submissions

## Reporting Frequency

Daily / Weekly / Monthly

## Business Importance

Measures operational reach of the intervention.

---

# KPI 2 – Individuals Reached

## Definition

Total number of individuals assisted.

## Formula

Sum(hh_size)

## Data Source

Kobo submissions

## Reporting Frequency

Daily / Weekly / Monthly

## Business Importance

Primary indicator used in donor reporting.

---

# KPI 3 – Active Distribution Sites

## Definition

Number of sites that recorded at least one valid distribution during the reporting period.

## Formula

Count distinct site_id

## Data Source

Distribution records

## Reporting Frequency

Weekly

## Business Importance

Measures operational coverage.

---

# KPI 4 – Data Quality Pass Rate

## Definition

Percentage of records that pass all mandatory quality checks.

## Formula

Valid Records / Total Records × 100

## Data Source

DQA Validation Table

## Reporting Frequency

Daily

## Business Importance

Measures reliability of reporting data.

---

# KPI 5 – Duplicate Rate

## Definition

Percentage of records flagged as potential duplicates.

## Formula

Duplicate Records / Total Records × 100

## Data Source

Risk Monitoring Table

## Reporting Frequency

Daily

## Business Importance

Helps identify data collection problems and fraud risks.

---

# KPI 6 – Reporting Delay

## Definition

Average number of days between distribution and submission.

## Formula

Submitted Date − Distribution Date

## Data Source

Kobo submissions

## Reporting Frequency

Weekly

## Business Importance

Measures timeliness of reporting.

---

# KPI 7 – Missing Data Rate

## Definition

Percentage of records containing missing mandatory fields.

## Formula

Records With Missing Fields / Total Records × 100

## Data Source

DQA Validation Table

## Reporting Frequency

Daily

## Business Importance

Measures completeness of data.

---

# KPI 8 – Distribution Compliance Rate

## Definition

Percentage of distributions that comply with project rules.

## Validation Rules

* Consent collected
* Quantity within standard range
* Signature available

## Formula

Compliant Records / Total Records × 100

## Reporting Frequency

Weekly

## Business Importance

Measures adherence to operational procedures.

---

# KPI 9 – Geographic Coverage

## Definition

Percentage of planned territories reached by the intervention.

## Formula

Territories Reached / Planned Territories × 100

## Reporting Frequency

Monthly

## Business Importance

Measures implementation coverage.

---

# KPI 10 – High-Risk Records

## Definition

Number of records requiring investigation.

## Examples

* Duplicate beneficiaries
* Suspicious quantities
* GPS anomalies
* Enumerator anomalies

## Reporting Frequency

Daily

## Business Importance

Supports fraud prevention and accountability.

---

# Dashboard Usage

## Executive Dashboard

Uses:

* Households Reached
* Individuals Reached
* Active Sites
* Reporting Delay

---

## MEL Dashboard

Uses:

* Geographic Coverage
* Distribution Compliance
* Beneficiaries Reached

---

## Data Quality Dashboard

Uses:

* DQA Pass Rate
* Missing Data Rate
* Duplicate Rate

---

## Risk Dashboard

Uses:

* High-Risk Records
* Duplicate Beneficiaries
* Enumerator Anomalies

---

# Reporting Principles

All KPI definitions must remain stable over time.

Any change in methodology must be documented and approved before implementation.
