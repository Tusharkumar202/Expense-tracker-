import streamlit as st
import expense as ex

st.title("PERSONAL EXPENSE TRACKER")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Expense", "View Expenses", "Total Expense", "Category Wise"]
)

# Add Expense
if menu == "Add Expense":

    st.header("Add New Expense")

    date = st.text_input("Date")

    category = st.selectbox(
        "Category",
        ["Food", "Travel", "Shopping", "Bills", "Other"]
    )

    amount = st.number_input("Amount")

    note = st.text_input("Note")

    if st.button("Add Expense"):

        ex.addexp(date, category, amount, note)

        st.success("Expense Added Successfully")


# View Expenses
elif menu == "View Expenses":

    st.header("All Expenses")

    expenses = ex.getexp()

    for e in expenses:

        st.write(
            e["date"],
            "|",
            e["category"],
            "| Rupees",
            e["amount"],
            "|",
            e["note"]
        )


# Total Expense
elif menu == "Total Expense":

    st.header("Total Expense")

    total = ex.total_expense()

    st.subheader("Total Expense = Rupees " + str(total))


# Category Wise
elif menu == "Category Wise":
 
    st.header("Category Wise Expense")

    data = ex.cat_exp()

    for i in data:

        st.write(i, ": Rupees", data[i])