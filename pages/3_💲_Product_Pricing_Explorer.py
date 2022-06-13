import streamlit as st
import pandas as pd

# Setting Page Title & Favicon
st.set_page_config(page_title="Product Pricing Explorer", page_icon="💲")

# Defining whiskey product types
bill_phil = {'name': 'Bill Phil', 'bottle_size': 700, 'abv': 47.50}

single_grain = {'name': 'Single Grain', 'bottle_size': 700, 'abv': 48.00}

from_clare_to_here = {'name': 'From Clare to Here', 'bottle_size': 700, 'abv': 54.00}


# List of Current WDOC Products Supported in the App
products = [bill_phil, single_grain, from_clare_to_here]


st.markdown("<h1 style='text-align: center';>Product Pricing Explorer</h1>", unsafe_allow_html=True)

st.markdown("""To use the Product Pricing Explore, please have the following details available for entry:""")
    
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - Product Name
        - LPA Price
        - Distillery Handling Fees
        - Label Design / Print Cost
        - Bottling Line Fees""")
    with col2:
        st.markdown("""
        - Bottle / Cork Cost
        - Tube / Box Cost
        - Target RRP
        - Retailer Margin %
        - Distributor Margin %""")

st.markdown("<h3 style='text-align:center';>Enter Product Details</h3>", unsafe_allow_html=True)

with st.expander(label='Enter Product Details Here'):
    with st.form(key='cost form'):
        left_column, right_column = st.columns(2)

        with left_column:
            product_name = st.selectbox(label='Product Name', options=[product['name'] for product in products])
    
            if product_name == 'Bill Phil':
                product = bill_phil
            elif product_name == 'Single Grain':
                product = single_grain
            elif product_name == 'From Clare to Here':
                product = from_clare_to_here
                
            lpa_cost = st.number_input('LPA Price', value=14.00, step=0.1, help="Enter the product's price per LPA")
            product['distillery_fees'] = st.number_input('Distillery Handling Fees', value=2.00, step=0.50, help="Enter any distillery handling fees")
            product['label_cost'] = st.number_input('Label Design/Print Cost', value=1.50, step=0.10, help='Enter the cost of the bottle labels')
            product['bottling_line_fees'] = st.number_input('Bottling Line Fees', value=2.00, step=0.10, help='Enter the bottling line cost per bottle')

        with right_column:
            product['dry_good_cost'] = st.number_input('Bottle / Cork Cost', value=1.50, step=0.10, help='Enter the cost of the bottle and cork')
            product['packaging_cost'] = st.number_input('Tube / Box Cost', value=1.20, step=0.01, help='Enter the cost of the bottle packaging')
        
            rrp = st.number_input('Target RRP', value=65.00, step=0.50, help='Enter Target RRP')
            retailer_margin = st.number_input('Retailer Margin', value=20.00, step=2.0, help='Enter Retailer Marging')
            distributor_margin = st.number_input('Distributor Margin', value=30.00, step=2.0, help='Enter Distributor Margin')
        
        submit_product = st.form_submit_button('Submit Product Details')

if submit_product:
    product['whiskey_cost'] = round(lpa_cost * (product['abv']/100) * (product['bottle_size']/1000), 2)
    
    product['excise'] = round(42.57 * (product['abv']/100) * (product['bottle_size']/1000), 2)

    product_costs = [product['whiskey_cost'], product['distillery_fees'], product['label_cost'], product['dry_good_cost'], product['packaging_cost'], product['bottling_line_fees']]

    product['cogs'] = round(sum(product_costs), 2)

    case_on_shelf = rrp * 6
    case_to_retailer = case_on_shelf * (1 - (retailer_margin/100))
    case_to_distributor = case_to_retailer * (1 - (distributor_margin/100))

    bottle_revenue = case_to_retailer / 6
    bottle_ex_vat = bottle_revenue - (bottle_revenue * 0.23)

    profit_per_bottle = round(bottle_ex_vat - product['cogs'], 3)

    our_margin = round(profit_per_bottle / bottle_ex_vat, 3)

    st.subheader('Pricing Details for {}'.format(product['name']))

    st.write('Cost of Goods: €{}'.format(product['cogs']))
    st.write('Revenue per Bottle, ex VAT: €{}'.format(bottle_ex_vat))
    st.write('Profit per Bottle: €{}'.format(profit_per_bottle))

    st.write('Our Margin: {}%'.format(our_margin*100))

    percentages=[22, 25.0, 28.0, 31.0, 34.0, 37.0, 40.0, 43.0, 46.00, 49.00, 52.00, 55.00, 58.00, 61.00, 64.00, 67.00, 70.00, 73.00, 76.00, 79.00, 82.00, 85.00]
    price_per_bottle = [round(product['cogs']/(1-(percentage/100)),3) for percentage in percentages]
    price_per_case = price_per_bottle * 6

    st.subheader('This Still Needs Work')
    df = pd.DataFrame({'WDOC Margins': percentages, 'Price Per Bottle': price_per_bottle})

    df['MSRP'] = ((df['Price Per Bottle'] + df['Price Per Bottle']*.23) * 6) / (1-(distributor_margin/100)) / (1-(retailer_margin/100)) / 6
    
    st.dataframe(df)