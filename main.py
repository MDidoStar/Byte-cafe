# Import Libraries and Modules
import streamlit as st
import statistics as stat
from func import *
st.set_page_config(page_title="CAFÉ SALES ANALYZER", layout='centered')

if "purchase_amounts" not in st.session_state:
    st.session_state.purchase_amounts = []
if "names" not in st.session_state:
    st.session_state.names = []

st.title("Byte Cafe")
st.header("CAFÉ SALES ANALYZER")
st.markdown("#####  Enter purchase amounts, analyze the data, and display the results")
name = st.text_input("Enter your name:")
purchase_amount = st.number_input("Enter The Purchase amount:", step=1)
c1, c2, c3 = st.columns(3)

if c1.button("Add Purchase", key="add purch"):
    if purchase_amount < 1 or not name:
        st.error("Please Choose a Price Greater Than 0 and Write The Name of The Customer.")
    else:
        st.session_state.purchase_amounts.append(purchase_amount)
        st.session_state.names.append(name.capitalize())
if c2.button("Analyze Sales", key="analyze sales"):
    if not st.session_state.purchase_amounts == []:
        st.subheader("Sales Summary")
        m, med, mod, sum_ss, leng = sales_statistics(st.session_state.purchase_amounts)
        if mod == "":
            mod = "No Single Mode"
        data = {"Sales": ["Total Sales", "Number of Sales", "Average Purchase", "Median Purchase", "Mode"], "Sales Info":[sum_ss, leng, m, med, mod]}
        st.dataframe(data)

        st.subheader("Bonus Sales Sunmmary")
        mx = max(st.session_state.purchase_amounts)
        mn = min(st.session_state.purchase_amounts)
        max_c = st.session_state.names[st.session_state.purchase_amounts.index(mx)]
        min_c = st.session_state.names[st.session_state.purchase_amounts.index(mn)]
        bonus = {
            "Purchase Type":["Highest Purchase","Lowest Purchase"],
            "Purchase Amounts":[set_zero(round(mx, 2)), set_zero(round(mn, 2))],
            "Customer who bought it":[max_c, min_c]
            }    
        st.dataframe(bonus)
if c3.button("Clear Data", key="clear data"):
    st.session_state.purchase_amounts = []
    st.session_state.names = []


if not st.session_state.purchase_amounts == []:
    Purchases = {"Customer Name": st.session_state.names, "Purchase Amounts" : new_zero_list(st.session_state.purchase_amounts)}
    st.subheader("Purchases")
    st.dataframe(Purchases)

    small, medium, large, premium = get_purchase_data(st.session_state.purchase_amounts)
    Purchases_Data = {"Purchase Types": ["Small Purchase", "Medium Purchase", "Large Purchase", "Premium Purchase"], "Num. of Purchase Type" :[small, medium, large, premium]}
    st.subheader("Purchase Categories")
    st.dataframe(Purchases_Data)
else:
    st.warning("No Purchases have been added")
