import streamlit as st
import pandas as pd

st.set_page_config(page_title="SpendWise AI", layout="centered")

st.title("💰 SpendWise AI")
st.write("Analyze your income and expenses using transaction data.")

@st.cache_data
def load_data():
    return pd.read_csv("data/transactions.csv")

df = load_data()

st.subheader("📄 Transactions Preview")
st.dataframe(df)

question = st.text_input("Ask a question about your finances:")

if question:
    q = question.lower()

    income_df = df[df["type"] == "entry"]
    expense_df = df[df["type"] == "expense"]

    if "total income" in q:
        total_income = income_df["amount"].sum()
        st.write(f"💵 Total income: ${total_income:,.2f}")

    elif "total expense" in q or "total spending" in q:
        total_expense = expense_df["amount"].sum()
        st.write(f"💸 Total expenses: ${total_expense:,.2f}")

    elif "balance" in q:
        balance = income_df["amount"].sum() - expense_df["amount"].sum()
        st.write(f"📊 Current balance: ${balance:,.2f}")

    elif "category" in q:
        category_spending = (
            expense_df.groupby("category")["amount"]
            .sum()
            .sort_values(ascending=False)
        )
        top_category = category_spending.idxmax()
        st.write(f"📌 Highest spending category: **{top_category}**")

    else:
        st.write(
            "🤔 Try asking about total income, total expenses, balance, or spending by category."
        )
