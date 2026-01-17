# SpendWise AI — Knowledge Base Documentation

## 1. Overview

This document describes the knowledge base used by **SpendWise AI**. The agent relies exclusively on a **single structured dataset** to generate insights and answer user questions related to personal finance behavior, including income, expenses, and balance.

All responses produced by the agent are strictly grounded in the dataset described below.

---

## 2. Knowledge Scope

The knowledge base supports the following types of analysis:

- Transaction-level financial analysis
- Income and expense aggregation
- Balance calculation (income minus expenses)
- Category-based expense analysis

The knowledge base does **not** support predictive modeling, investment advice, budgeting recommendations, or external financial data enrichment.

---

## 3. Data Source Description

### 3.1 transactions.csv

**Description:**  
Contains mock records of personal financial transactions used for educational and analytical purposes.

**Key Fields:**

- `date`: Date of the transaction  
- `description`: Short description of the transaction  
- `category`: Transaction category (e.g., Food, Housing, Transportation)  
- `amount`: Monetary value of the transaction  
- `type`: Transaction type (`income` or `expense`)

**Usage by the Agent:**

- Calculate total income
- Calculate total expenses
- Compute current balance
- Aggregate expenses by category
- Identify highest spending categories

The dataset is static and fully contained within the project repository.

---

## 4. Data Access Rules

- The agent must not infer or fabricate missing data
- The agent must not generate transactions or categories not present in the dataset
- All numerical results must be directly traceable to the dataset
- If requested information is unavailable, the agent must explicitly state the limitation

---

## 5. Knowledge Boundaries

The agent will refuse or safely redirect questions related to:

- Investment performance or recommendations
- Credit approval or scoring
- Financial forecasting or predictions
- Legal, tax, or accounting advice

---

## 6. Data Assumptions

- All transactions are fictional
- All monetary values are positive
- Balance is calculated as total income minus total expenses
- Categories are used solely for descriptive aggregation

---

## 7. Success Criteria

The knowledge base is considered effective if:

- Every answer can be traced back to `transactions.csv`
- The agent clearly communicates data limitations
- Insights remain consistent, explainable, and reproducible

---

*Document version: 1.0*

