import streamlit as st

st.title("Marvellous Infosystems")
st.title("Even or Odd Number")

no = st.number_input("Enter Integer Number : ", value=0, step=1)

if st.button("Check"):
    if no % 2 == 0:
        st.success("The number is Even")
    else:
        st.success("The number is Odd")

st.divider()
st.caption("Marvellous Infosystems")