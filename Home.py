import streamlit as st
import pandas as pd
import datetime

favicon = 'WDOC_Logo_Black.jpg'

st.set_page_config(
    page_title="O'Connell Whiskey Merchants WRAMS", page_icon=favicon)

col1, col2, col3 = st.columns(3)
with col2:
    st.image('WDOC_Logo_Black.jpg', width=250)

st.sidebar.success('Select an option above.')

# Main Page Code
st.markdown("<h1 style='text-align: center';>O'Connell Whiskey Merchants WRAMS</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left';>Created: May 27, 2022</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left';>Version 1.0.1</h6>", unsafe_allow_html=True)

st.markdown("""This simple web app is designed to for easy updating to O'Connell Whiskey Merchants Warehouse & Records Management, speicifically regarding:""")

st.markdown("""
    - Cask Inventory
    - Dry Goods Inventory
    - Product Pricing Explorer""")
    
st.markdown("""By using the menu to the left, you can select whether you'd like to add, update or delete a cask; add, update or delete dry goods; or explore pricing for WDOC Products.""")

st.markdown("""Note: Using the Pricing Explorer simply creates a pricing model and calculates the profit margin for the end product.""")    


st.markdown('<h6>For help with the app, reach out to Tom!</h6>', unsafe_allow_html=True)












    




    
