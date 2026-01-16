# SpendWise AI — Knowledge Base Documentation

## 1. Overview

This document describes the knowledge base used by **SpendWise AI**. The agent relies exclusively on structured, pre-defined datasets to generate insights and answer user questions related to personal spending behavior.

All responses produced by the agent must be grounded in the data sources described below.

---

## 2. Knowledge Scope

The knowledge base supports the following types of analysis:

* Transaction-level spending analysis
* Category-based expense aggregation
* Temporal spending trends
* Identification of recurring expenses

The knowledge base does **not** support predictive modeling, investment advice, or external financial data enrichment.

---

## 3. Data Sources Description

### 3.1 transactions.csv

**Description:**
Contains detailed records of user financial transactions.

**Key Fields:**

* `transaction_id`: Unique identifier of the transaction
* `date`: Transaction date
* `amount`: Transaction value
* `category`: Expense category (e.g., Food, Transport, Utilities)
* `description`: Short description of the transaction

**Usage by the Agent:**

* Calculate total and average spending
* Identify top spending categories
* Detect recurring payments
* Analyze spending behavior over time

---

### 3.2 historico_atendimento.csv

**Description:**
Stores historical customer service interactions.

**Key Fields:**

* `interaction_id`: Unique interaction identifier
* `date`: Interaction date
* `topic`: Subject of the interaction
* `resolution_status`: Outcome of the interaction

**Usage by the Agent:**

* Provide contextual understanding of past issues
* Support explanations related to financial services

This dataset is used strictly for contextual reference and does not influence financial calculations.

---

### 3.3 perfil_investidor.json

**Description:**
Contains high-level user profile information.

**Key Fields:**

* `risk_profile`: Conservative, Moderate, or Aggressive
* `financial_goals`: Stated user objectives
* `income_range`: Approximate income level

**Usage by the Agent:**

* Adjust explanation depth and tone
* Provide context-aware insights

The agent does not generate investment recommendations based on this data.

---

### 3.4 produtos_financeiros.json

**Description:**
Reference dataset describing available financial products.

**Key Fields:**

* `product_name`
* `product_type`
* `description`

**Usage by the Agent:**

* Answer high-level informational questions
* Explain product characteristics when requested

This dataset is informational only.

---

## 4. Data Access Rules

* The agent must not infer missing values
* The agent must not fabricate transactions or categories
* If requested data is unavailable, the agent must explicitly state the limitation

---

## 5. Knowledge Boundaries

The agent will refuse or safely redirect questions related to:

* Investment performance predictions
* Credit approval or scoring
* Legal or tax advice
* Financial guarantees

---

## 6. Data Update Assumptions

The datasets are considered static for the scope of this project. No real-time updates or external integrations are assumed.

---

## 7. Success Criteria

The knowledge base is considered effective if:

* All answers can be traced back to a specific dataset
* The agent clearly communicates data limitations
* Insights remain consistent and reproducible

---

*Document version: 1.0*
