from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np


st.set_page_config(layout="wide")
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:

farts
"""
colorBTC = "#F2A900"
colorBCH = "#0AC18E"

# df = pd.DataFrame(
#     [
#         {"command": "st.selectbox", "rating": 4, "is_widget": True},
#         {"command": "st.balloons", "rating": 5, "is_widget": False},
#         {"command": "st.time_input", "rating": 3, "is_widget": True},
#     ]
# )

# st.dataframe(df, use_container_width=True)

# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#     Point = namedtuple('Point', 'x y')
#     data = []

#     points_per_turn = total_points / num_turns

#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))

#     st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#         .mark_circle(color='#0068c9', opacity=0.5)
#         .encode(x='x:Q', y='y:Q'))


# st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

#! st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
#! Formatter for int/float supports: %d %e %f %g %i Formatter for date/time/datetime uses Moment.js notation: https://momentjs.com/docs/#/displaying/format/

seconds_per_day = 86400

#### FORMATS #################################################################
format_slider_TPS = "%d"
format_slider_energyUsageYearlyTwH = "%d"

format_slider_exaHashes = "%d"

format_slider_Price = "%d"

#### FORMATS #################################################################

#### LABELS #################################################################
label_BTC_TPS = "BTC Network, Maximum Transactions Per Second (Default: 7)"
label_BCH_TPS = "BCH Network, Maximum Transactions Per Second (Default: 224)" 

label_energyUsageYearlyTwH_BTC = "BTC: Yearly energy usage of entire network in Terrawatt Hours (Default: 145.02), found here: https://ccaf.io/cbnsi/cbeci " 

label_exaHashes_BTC = "BTC: Current Exahashes (7 Day AVG) (Default: 402.2)"
label_exaHashes_BCH = "BCH: Current Exahashes (7 Day AVG) (Default: 2.67)"

label_priceBTC = "BTC: Current Price "
label_priceBCH = "BCH: Current Price"

#### LABELS #################################################################

#### SIDEBAR #################################################################
slider_BTC_TPS = st.sidebar.slider(label_BTC_TPS, 1, 7, 7, 1, format_slider_TPS)

st.sidebar.write('Current TPS', '<h2>', str(slider_BTC_TPS), '</h2>', unsafe_allow_html=True)


slider_BCH_TPS = st.sidebar.slider(label_BCH_TPS, 1, 10000, 224, 1, format_slider_TPS)

slider_exaHashes_BTC = st.sidebar.slider(label_exaHashes_BTC, 1.0, 1000.0, 402.2, .1, format_slider_exaHashes)
slider_exaHashes_BCH = st.sidebar.slider(label_exaHashes_BCH, 1.0, 1000.0, 2.67, .1, format_slider_exaHashes)

slider_energyUsageYearlyTwH_BTC = st.sidebar.slider(label_energyUsageYearlyTwH_BTC, 1.0, 1000.0, 145.02, .1, format_slider_energyUsageYearlyTwH)
# ! No slider for BCH as its energy usage is derived from BTC energy usage per exahash.
energyUsageYearlyKwH_BTC = slider_energyUsageYearlyTwH_BTC * 1000000000

exaHashToYearlyKwHRatio = energyUsageYearlyKwH_BTC / slider_exaHashes_BTC
energyUsageYearlyKwH_BCH = slider_exaHashes_BCH * exaHashToYearlyKwHRatio
energyUsageYearlyTwH_BCH = energyUsageYearlyKwH_BCH /  1000000000
st.sidebar.write('BTC: Yearly energy usage of entire network in Kilowatt(KwH) Hours :', energyUsageYearlyKwH_BTC)

st.sidebar.write('BCH: Yearly energy usage of entire network in Terawatt(TwH) Hours :', energyUsageYearlyTwH_BCH)
st.sidebar.write('BCH: Yearly energy usage of entire network in Kilowatt(KwH) Hours :', energyUsageYearlyKwH_BCH)

slider_PriceBTC = st.sidebar.slider(label_priceBTC, 1.0, 100000.0, 26091.70, .1, format_slider_Price)
slider_PriceBCH = st.sidebar.slider(label_priceBCH, 1.0, 100000.0, 190.02, .1, format_slider_Price)


# st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder="Select...", disabled=False, label_visibility="visible")
blockReward = st.sidebar.selectbox('Choose block reward (Default: 6.25)', (50, 25, 12.5, 6.25, 3.125, 1.5625, .78125, .390625, .195325, .09765625, 0), 3)

# (6 blocks per hour * 24 hours) * (block reward)
totalDailyBlockRewards = (6*24) * blockReward

#### SIDEBAR #################################################################

#### MAIN #################################################################
max_daily_transactions_BTC = seconds_per_day * slider_BTC_TPS
max_daily_transactions_BCH = seconds_per_day * slider_BCH_TPS


st.write('##BTC Maximum Daily Transactions:', max_daily_transactions_BTC)
st.write('##BCH Maximum Daily Transactions:', max_daily_transactions_BCH)

st.write('energyUsageYearlyTwH_BTC:', slider_energyUsageYearlyTwH_BTC)
st.write('energyUsageYearlyTwH_BCH:', energyUsageYearlyTwH_BCH)

st.write('Exahash to Kwh/year ratio:', exaHashToYearlyKwHRatio)
# ! Derived from (energyUsageYearlyKwH_BTC / slider_exaHashes_BTC) * exaHashToYearlyKwHRatio

st.write('BTC Price:', slider_PriceBTC)
st.write('BCH Price:', slider_PriceBCH)

st.write('BTC Total Daily Block Rewards (USD):', totalDailyBlockRewards * slider_PriceBTC)
st.write('BCH Total Daily Block Rewards (USD):', totalDailyBlockRewards * slider_PriceBCH)


# * First lets discuss security budget costs
# * Column 1: Per KwH Cost, .007 to .30
# * Column 2: energyUsageYearlyKwH_BTC * Col1 , energyUsageYearlyKwH_BCH * Col1

KwHCostList = [.5,.6,.7,.8]

df = pd.DataFrame(KwHCostList)


st.dataframe(df, use_container_width=True)

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

# Define the range of values
start_value = 0.007
end_value = 0.35
step = 0.001


# Define the variable for energy usage
#energyUsageYearlyKwH = 1000  # Example value, replace with your actual value




# Create a list of values for column 1
costPerKwH = [round(start_value + i * step, 3) for i in range(int((end_value - start_value) / step) + 1)]

# Create a dictionary to hold the data
data = {
    "Electricity Cost (per KwH)": costPerKwH,
    "Yearly, BTC Security Budget": [value * energyUsageYearlyKwH_BTC for value in costPerKwH],
    "Yearly, BCH Security Budget": [value * energyUsageYearlyKwH_BCH for value in costPerKwH]
}

df = pd.DataFrame(data)
# st.line_chart(df, x = 'Electricity Cost (per KwH)', y = ['Yearly BTC Security Budget','Yearly BCH Security Budget'], color = [colorBTC, colorBCH])
#st.line_chart(data = df, x = 'Electricity Cost (per KwH)')

# st.line_chart(
#     data=df,
#     x='Electricity Cost (per KwH)',
#     y=['Yearly, BTC Security Budget','Yearly, BCH Security Budget'],
#     color=['#F2A900', '#0AC18E']
#     )



st.line_chart(
    df,
    x = 'Electricity Cost (per KwH)',
    y = ['Yearly, BTC Security Budget','Yearly, BCH Security Budget'],
    color = ['#FF0000', '#0000FF'])


    # ['#F2A900', '#0AC18E']


# # ! This is a simple, linear chart.

colorBTC = "#F2A900"
colorBCH = "#0AC18E"



# * Next lets see what the costs look like by day.
# * Same as above but divided by 365
# * 

data = {
    "Electricity Cost (per KwH)": costPerKwH,
    "Daily, BTC Security Budget": [(value * energyUsageYearlyKwH_BTC)/365 for value in costPerKwH],
    "Daily, BCH Security Budget": [(value * energyUsageYearlyKwH_BCH)/365 for value in costPerKwH]
    
}
df = pd.DataFrame(data)
st.line_chart(df,x = 'Electricity Cost (per KwH)')
# ! Again, this is a simple, linear chart. Just scaled to daily.

# * Next lets discuss if block reward covers security budget costs
# * Same as above but divided by 365
# * 

data = {
    "Electricity Cost (per KwH)": costPerKwH,
    "Daily, BTC Security Costs minus Block Reward": [((value * energyUsageYearlyKwH_BTC)/365) - (totalDailyBlockRewards * slider_PriceBTC) for value in costPerKwH],
    "Daily, BCH Security Costs minus Block Reward": [((value * energyUsageYearlyKwH_BCH)/365) - (totalDailyBlockRewards * slider_PriceBCH) for value in costPerKwH]
    
}
df = pd.DataFrame(data)
st.line_chart(df,x = 'Electricity Cost (per KwH)')

st.write('BTC Total Daily Block Rewards (USD):', totalDailyBlockRewards * slider_PriceBTC)
st.write('BCH Total Daily Block Rewards (USD):', totalDailyBlockRewards * slider_PriceBCH)

''' And now we see some interesting things start to emerge...
What we see here is... once the price per KwH gets close the the cheapest availiable KwH.

- Libya by the way is/was cheapest in the world with .007 USD per KwH)
- The current (6.25) block rewards are no longer sufficient to cover the security budget.
- This means it will be neccesary for the remaining of the security budget to be covered by the transaction fees.

Some exercises to do.
- Adjust the block reward up and down
    - @ 25 Bitcoins (BTC) the block reward was enough to cover the energy costs up to about .235/Kwh.
    - @ 50 Bitcoins (BTC) the block reward was enough to cover the energy costs up to about .45/Kwh.

Lets break that down..

'''
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.header("BTC")
    data = {
    "Electricity Cost (per KwH)": costPerKwH,
    "Daily, BTC Security Costs minus Block Reward": [((value * energyUsageYearlyKwH_BTC)/365) - (totalDailyBlockRewards * slider_PriceBTC) for value in costPerKwH]   
    }
    df = pd.DataFrame(data)
    st.line_chart(df,x = 'Electricity Cost (per KwH)')
    ''' BTC Info here'''

#    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("BCH")
    data = {
    "Electricity Cost (per KwH)": costPerKwH,
    "Daily, BCH Security Costs minus Block Reward": [((value * energyUsageYearlyKwH_BCH)/365) - (totalDailyBlockRewards * slider_PriceBCH) for value in costPerKwH]
    }
    df = pd.DataFrame(data)
    st.line_chart(df,x = 'Electricity Cost (per KwH)')
    '''BCH Info Here'''

#    st.image("https://static.streamlit.io/examples/dog.jpg")
