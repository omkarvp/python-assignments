import streamlit as st

st.title("Marvellous Infosystems")
st.title("Celsius to Fahrenheit Converter")

celsius = st.number_input("Enter Temperature in Celsius : ", value=0.0)

if st.button("Convert"):
    fahrenheit = (celsius * 9 / 5) + 32

    st.success("Temperature in Fahrenheit is : " + str(round(fahrenheit, 2)))

st.divider()
st.caption("Marvellous Infosystems")
