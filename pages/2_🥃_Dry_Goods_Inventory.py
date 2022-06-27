import streamlit as st
import pandas as pd

# Setting Page Title & Favicon
st.set_page_config(page_title="Dry Goods Inventory", page_icon="🥃")

# Code for Dry Goods Inventory Page

# Setting Sidebar Choices
choice = ['Home', 'Add Dry Goods to the Inventory', 'Remove Dry Goods from the Inventory', 'Plan a Bottling Run']

st.sidebar.markdown("<h1 style=text-align:center;'>Dry Goods Inventory Editor</h1>", unsafe_allow_html=True)
st.sidebar.write("From the list below, pick the area you'd like to edit in the inventory. Please note that if you plan a bottling run, you will remove goods from the inventory when you click the form submit button.")

inventory_action = st.sidebar.selectbox(label='What Update Would You Like To Make?', options=choice, index=0)

if inventory_action == choice[0]:
    st.markdown("<h1 style=text-align:center;>Dry Goods Inventory</h1>", unsafe_allow_html=True)

    df = pd.read_csv('warehouse_inventory.csv')
    st.subheader('Current Warehouse Inventory')
    st.table(df)

if inventory_action == choice[1]:
    st.markdown("<h1 style=text-align:center;>Add Dry Goods</h1>", unsafe_allow_html=True)

    st.markdown("<h3 style=text-align:center;>Search by SKU or keyword to add items to the Dry Goods Inventory</h3>", unsafe_allow_html=True)





if inventory_action == choice[2]:
    st.markdown("<h1 style=text-align:center;>Remove Dry Goods</h1>", unsafe_allow_html=True)

if inventory_action == choice[3]:
    st.markdown("<h1 style=text-align:center;>Plan a Bottling Run</h1>", unsafe_allow_html=True)