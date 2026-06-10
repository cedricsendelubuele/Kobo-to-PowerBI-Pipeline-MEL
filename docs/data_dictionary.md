# Data Dictionary

## Overview

This document defines all key fields used in the Kobo-to-PowerBI-Pipeline-MEL project.

The objective is to ensure that all users interpret the data consistently.

---

# Beneficiary Information

| Field Name      | Type    | Description                   | Example   |
| --------------- | ------- | ----------------------------- | --------- |
| beneficiary_uid | Text    | Unique beneficiary identifier | BEN_10001 |
| hh_size         | Integer | Household size                | 6         |
| sex_head        | Text    | Gender of household head      | Female    |
| age_head        | Integer | Age of household head         | 35        |

---

# Geographic Information

| Field Name | Type | Description                  | Example     |
| ---------- | ---- | ---------------------------- | ----------- |
| province   | Text | Province name                | North Kivu  |
| territory  | Text | Territory name               | Nyiragongo  |
| site_id    | Text | Distribution site identifier | SITE_GOM_01 |

---

# Distribution Information

| Field Name        | Type    | Description          | Example    |
| ----------------- | ------- | -------------------- | ---------- |
| distribution_date | Date    | Date of distribution | 2025-03-12 |
| item_kit_type     | Text    | Type of NFI kit      | NFI_KIT_A  |
| qty               | Integer | Quantity distributed | 1          |

---

# Data Collection Information

| Field Name    | Type     | Description               | Example              |
| ------------- | -------- | ------------------------- | -------------------- |
| submission_id | Text     | Unique Kobo submission ID | SUB_0001             |
| submitted_at  | DateTime | Submission timestamp      | 2025-03-12T10:22:00Z |
| enumerator_id | Text     | Data collector identifier | EN_004               |

---

# Quality Control Fields

| Field Name        | Type    | Description                    | Example |
| ----------------- | ------- | ------------------------------ | ------- |
| consent           | Boolean | Beneficiary consent obtained   | TRUE    |
| signature_present | Boolean | Signature collected            | TRUE    |
| dqa_status        | Text    | Data quality validation status | PASS    |

---

# Risk Monitoring Fields

| Field Name     | Type    | Description                 | Example               |
| -------------- | ------- | --------------------------- | --------------------- |
| duplicate_flag | Boolean | Possible duplicate detected | TRUE                  |
| risk_level     | Text    | Risk assessment level       | Medium                |
| risk_reason    | Text    | Explanation of the risk     | Duplicate beneficiary |

---

# Business Rules

## Household Size

Minimum value:

1

Maximum recommended value:

15

Values above 15 should be reviewed.

---

## Age of Household Head

Minimum expected value:

18

Maximum expected value:

110

Values outside this range should be flagged.

---

## Quantity Distributed

Standard distribution:

1 kit per household.

Values greater than 1 require verification.

---

## Consent

All records should have consent = TRUE.

Records without consent must be investigated.

---

# Data Privacy

This project uses synthetic data only.

No real beneficiary information is stored.

Personal information must never be uploaded to public repositories.
