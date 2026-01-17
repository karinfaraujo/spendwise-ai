# 💰 SpendWise AI

**SpendWise AI** is a data-driven personal finance analysis assistant designed to help users understand their **income, expenses, and financial balance** through clear, transparent, and reliable insights.

This project demonstrates how generative AI concepts can be applied responsibly in personal finance by enforcing **strict data boundaries**, **clear scope definition**, and **low hallucination risk**.

---

## 🚀 Project Overview

Many individuals have access to financial transaction data but struggle to extract meaningful insights from it.  
SpendWise AI transforms raw income and expense records into understandable summaries, helping users gain visibility into their financial behavior.

The agent focuses exclusively on **descriptive financial analysis**, ensuring that all responses are fully grounded in the available dataset.

---

## 🎯 Key Features

- Income and expense tracking
- Financial balance calculation
- Spending analysis by category
- Identification of highest expense categories
- Clear and user-friendly explanations
- Explicit handling of data limitations
- Low hallucination risk through strict scope control

---

## 🧠 Agent Scope and Limitations

SpendWise AI does **not** provide:

- Investment recommendations
- Credit scoring or loan decisions
- Financial predictions or forecasts
- Legal, tax, or accounting advice

All insights are generated **strictly from the provided dataset**.

---

## 🗂️ Project Structure

```
spendwise-ai/
│
├── data/
│   └── transactions.csv
└── docs/
    ├── 01-agent-documentation.md
    ├── 02-knowledge-base.md
    ├── 03-prompts.md
    ├── 04-metrics.md
    └── 05-pitch.md
├── images/
    ├── current-balance.png
    ├── highest-expense.png
    ├── total-expenses.png
├── app.py
├── README.md
├── requirements.txt
```

---

## 🛠️ Technologies Used

- Python  
- Streamlit  
- Pandas  

---

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/karinfaraujo/spendwise-ai.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

---

## 📊 Dataset Notes

- The dataset contains **mock financial transactions** for educational purposes.
- Column names were translated and standardized to English for consistency.
- Transactions are classified as **income** or **expense** using a `type` field.

---

## 📊 Evaluation Criteria

The agent is evaluated based on:
- Accuracy of data-backed responses  
- Transparency about data limitations  
- Clarity and usefulness of insights  
- Compliance with the defined scope  

---

## 📌 Inspiration

This project was inspired by a Digital Innovation One (DIO) challenge.  
All design decisions, documentation, and implementation were independently developed.

---

## 📬 Author

**Karin Araujo**  
Aspiring Data Analyst  
