import streamlit as st
import pandas as pd

# Setting Page Title & Favicon
st.set_page_config(page_title='Bottling Run Price Calculator', page_icon='💶')

# Setting Cost of Run baseline
cost_of_run = 0

# Setting baseline bottling line fees
per_bottle_fee = 2.00
extra_label_cost = 0.25

# Line Setup & Minimum
line_setup_fee = 250.00
line_minimum_charge = 1000.00

# Administrative Fee
administrative_fee = 100.00

# Monthly Storage Fees
pallet_storage_fee = 15.00
large_pallet_fee = 25.00

# Transportation Fees
regions = ['Within Europe', 'Outside Europe']
within_europe = 100.00
outside_europe = 200.00



st.markdown("<h1 style='text-align: center';>Bottling Run Pricing Calculator</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center';>Enter Run Details</h3>", unsafe_allow_html=True)

with st.expander(label='Enter Run Details Here'):
    left_column, right_column = st.columns(2)
    with left_column:
        brand_name = st.text_input('Brand Name')
        bottle_count = st.number_input('Bottle Count', value=500, step=100, help='Enter the number of bottles expected')
        waive_line_setup_fee = st.checkbox('Waive Line Setup Fee?')
        waive_administrative_fee = st.checkbox('Waive Admin / Paperwork Fee?')
        pallet_storage_required = st.checkbox('Pallet Storage Required?')

    with right_column:
        label_count = st.number_input('Number of Front / Back Labels', value=2, step=1, min_value=0, max_value=5)
        neck_label = st.number_input('Number of Extra Labels, e.g. Neck Label', value=1, step=1, min_value=0, max_value=3)
        transportation = st.selectbox(label='Transport Region', options=regions)
 
line_charge = 0
labeling_charge = 0
labels = label_count + neck_label

# Get bottle count cost baseline
if bottle_count < 10000:
    line_charge += bottle_count * per_bottle_fee
    if line_charge < line_minimum_charge:
        line_charge += line_minimum_charge
if bottle_count > 10000:
    line_charge += bottle_count * 1.00

# Get label count costs
if labels > 2:
    labeling_charge += (bottle_count * 0.25 * (labels - 2))


st.subheader('Run Details for {}'.format(brand_name))

st.write('Line Charge For Run: €{}'.format(line_charge))
st.write('Cost of Extra Labels: €{}'.format(labeling_charge))        

cost_of_run += line_charge
cost_of_run += labeling_charge

cost_of_run = cost_of_run

if waive_line_setup_fee == False:
    cost_of_run += line_setup_fee

if waive_administrative_fee == False:
    cost_of_run += administrative_fee

if pallet_storage_required:
    cost_of_run += pallet_storage_fee

if transportation == 'Within Europe':
    cost_of_run += 100
if transportation == 'Outside Europe':
    cost_of_run += 200

st.write('Total Cost of Bottling Run: €{}'.format(cost_of_run))