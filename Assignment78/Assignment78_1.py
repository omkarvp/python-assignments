import streamlit as st

st.title("Marvellous Infosystems")
st.title("Marvellous Addition Calculator")

no1 = st.number_input("Enter First Number : ", value=0.0)
no2 = st.number_input("Enter Second Number : ", value=0.0)

if st.button("Addition"):
    result = no1 + no2

    st.success("Addition is : " + str(result))

st.divider()
st.caption("Marvellous Infosystems")