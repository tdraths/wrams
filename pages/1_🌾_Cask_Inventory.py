import streamlit as st
import pandas as pd
import datetime

# Setting Page Title & Favicon
st.set_page_config(page_title='Cask Inventory', page_icon='🌾')

# Code for Cask Inventory Page
df = pd.read_csv('wrams.csv')

st.markdown("<h1 style='text-align: center;'>WRAMS</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Recording Casks for the Warehouse</h3>", unsafe_allow_html=True)

with st.form('cask_form'):
    st.header('**Enter Cask Details Below**')
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        cask_number = st.text_input('Cask Number', value='')
        rack_column = st.number_input('Rack Column', min_value=1, step=1)
        rack_row = st.number_input('Rack Row', min_value=1, step=1)
        row_position = st.number_input('Row Position (Front to Back', min_value=1, step=1)
    
    with col2:
        cask_type = st.selectbox('Cask Type', ['PX Hogshead', 'American Ex-Bourbon', 'Oloroso Sherry Butt'])
        cask_size = st.slider('Cask Size (Litres)', min_value=100, max_value=1000, value=250, step=50)
        fill_quantity = st.slider('Fill Quantity (Litres)', min_value=100, max_value=1000, value=250, step=50)
    
    with col3:
        spirit_type = st.selectbox('Spirit Type', ['Single Malt', 'Single Pot Still', 'Single Grain'])
        spirit_category = st.selectbox('Spirit Category', ['Irish Whiskey', 'Scotch Whiskey', 'American Bourbon'])
        current_abv = st.number_input('Current ABV %', min_value=40.0, max_value=69.0, value=60.0, step=0.1)
    
    with col4:
        distillery_name = st.text_input('Distillery')
        distilled_date = st.date_input('Distilled Date', min_value=datetime.date(2000, 1, 1))
        filled_date = st.date_input('Cask Filled Date', min_value=datetime.date(2000, 1, 1))

    submitted = st.form_submit_button('Add Cask')
    if submitted == True:

        new_cask = {'cask_number': cask_number,
                    'rack_column': rack_column,
                    'rack_row': rack_row,
                    'row_position': row_position,
                    'cask_type': cask_type,
                    'cask_size': cask_size,
                    'fill_quantity': fill_quantity,
                    'spirit_type': spirit_type,
                    'spirit_category': spirit_category,
                    'current_abv': current_abv,
                    'distillery_name': distillery_name,
                    'distilled_date': distilled_date,
                    'fill_date': filled_date}
        
        st.markdown("<h3 style='text-align: center';>Cask added successfully!</h3>", unsafe_allow_html=True)

        df = df.append(new_cask, ignore_index=True)

df['distilled_date'] = pd.to_datetime(df['distilled_date'])
df['year_distilled'] = pd.DatetimeIndex(df['distilled_date']).year
df['current_age'] = round((datetime.datetime.today() - df['distilled_date']) / datetime.timedelta(365), 2)
df['fill_date'] = pd.to_datetime(df['fill_date'])

distillery_towns = {'Miltonduff': 'Miltonduff',
                    'Bruichladdich': 'Bruichladdich',
                    'Great Northern': 'Dundalk',
                    'Cooley': 'Cooley Peninsula',
                    'Bushmills': 'Bushmills'}

distillery_regions = {'Miltonduff': 'Speyside',
                        'Bruichladdich': 'Islay',
                        'Great Northern': 'County Louth',
                        'Cooley': 'County Louth',
                        'Bushmills': 'County Antrim'}

distillery_countries = {'Miltonduff': 'Scotland',
                        'Bruichladdich': 'Scotland',
                        'Great Northern': 'Ireland',
                        'Cooley': 'Ireland',
                        'Bushmills': 'Ireland'}

df['distillery_region'] = df['distillery_name'].map(distillery_regions)

df['distillery_town'] = df['distillery_name'].map(distillery_towns)

df['distillery_country'] = df['distillery_name'].map(distillery_countries)


open('wrams.csv', 'w').write(df.to_csv(index=False))


df = pd.read_csv('wrams.csv')

st.markdown("<h3 style='text-align:center;'>Current Cask Inventory</h3>", unsafe_allow_html=True)
st.write(df)

error_button = st.button('Click here to delete your last entry.')
if error_button == True:
    df = df.drop(index=df.index[-1], axis=0)

    st.write(df)