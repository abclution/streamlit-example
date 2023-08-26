from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

colorBTC = "#F2A900"
colorBCH = "#0AC18E"
seconds_per_day = 86400


"""
Just farting around 
"""
###############################################################################
st.sidebar.write('<font size="+5">Max. TPS','</font>', '</br>', '(Transactions per Second, Full Blocks)', unsafe_allow_html=True)
###############################################################################
#### BTC TPS SLIDER  ##########################################################
format_slider_TPS = "%d"
label_BTC_TPS = ":orange[BTC Network] *(Default: 7)*"
slider_BTC_TPS = st.sidebar.slider(label_BTC_TPS,
                                   1, 7, 7, 1,
                                   format_slider_TPS)

max_daily_transactions_BTC = (seconds_per_day * slider_BTC_TPS)

#### BCH TPS SLIDER  ##########################################################
format_slider_TPS = "%d"
label_BCH_TPS = ':green[BCH Network] *(Default: 224)*' 
slider_BCH_TPS = st.sidebar.slider(label_BCH_TPS,
                                   1, 10000, 224, 1,
                                   format_slider_TPS)

max_daily_transactions_BCH = (seconds_per_day * slider_BCH_TPS)
###############################################################################
st.sidebar.divider()
###############################################################################


###############################################################################
st.sidebar.write('<font size="+5">Hashrate','</font>', '</br>', '(Current hashrate in exa-hashes, 7 Day AVG.)', unsafe_allow_html=True)
###############################################################################
#### BTC HASHRATE SLIDER  #####################################################
format_slider_exaHashes = "%d"
label_exaHashes_BTC = ":orange[BTC Network] *(Default: 402.2)*"
slider_exaHashes_BTC = st.sidebar.slider(label_exaHashes_BTC,
                                         1.0, 1000.0, 402.2, .1,
                                         format_slider_exaHashes)

#### BCH HASHRATE SLIDER  #####################################################
format_slider_exaHashes = "%d"
label_exaHashes_BCH = ":green[BCH Network] *(Default: 2.67)*"
slider_exaHashes_BCH = st.sidebar.slider(label_exaHashes_BCH,
                                         1.0, 1000.0, 2.67, .1,
                                         format_slider_exaHashes)
###############################################################################
st.sidebar.divider()
###############################################################################


###############################################################################
st.sidebar.write('<font size="+5">Energy Usage in TwH','</font>', '</br>', '(Yearly energy usage of entire network in Terrawatt Hours, found here, https://ccaf.io/cbnsi/cbeci )', unsafe_allow_html=True)
###############################################################################
#### BTC ENERGY USAGE SLIDER  #################################################
format_slider_energyUsageYearlyTwH = "%d"
label_energyUsageYearlyTwH_BTC = ":orange[BTC Network] *(Default: 145.02)*"
slider_energyUsageYearlyTwH_BTC = st.sidebar.slider(label_energyUsageYearlyTwH_BTC,
                                                    1.0, 1000.0, 145.02, .1,
                                                    format_slider_energyUsageYearlyTwH)

#### BCH ENERGY USAGE SLIDER  #################################################
# ! No slider for BCH as its energy usage is derived from BTC energy usage per exahash.

# Convert BTC Yearly TwH to KwH, this is because most other calculations are
# done based on the cost of each KwH.
energyUsageYearlyKwH_BTC = (slider_energyUsageYearlyTwH_BTC * 1000000000)

# Get an energy usage ratio by getting the BTC hashrate and its yearly KwH
exaHashToYearlyKwHRatio = (energyUsageYearlyKwH_BTC / slider_exaHashes_BTC)

# Multiply the BCH exahashes by the energy usage ratio, this assumes equivalent
# efficiency between the chains equipment. This is a fair comparison.
energyUsageYearlyKwH_BCH = (slider_exaHashes_BCH * exaHashToYearlyKwHRatio)

# Get BCH yearly TwH used
energyUsageYearlyTwH_BCH = (energyUsageYearlyKwH_BCH / 1000000000)

st.sidebar.write("The energy usage of the BCH network is based on its hashrate in comparison to BTC's energy usage and hashrate.")
st.sidebar.write('KwH Yearly',
                 '<h3>',
                 str(round(energyUsageYearlyKwH_BCH)),
                 '</h3>',
                 'TwH Yearly',
                 '<h3>',
                 str(round(energyUsageYearlyTwH_BCH)),
                 '</h3>',
                 unsafe_allow_html=True)
###############################################################################
st.sidebar.divider()
###############################################################################

#### BTC PRICING SLIDER  ######################################################
format_slider_Price = "%d"
label_priceBTC = ":orange[BTC] : Current Price"

slider_PriceBTC = st.sidebar.slider(label_priceBTC,
                                    1.0, 100000.0, 26091.70, .1,
                                    format_slider_Price)

#### BCH PRICING SLIDER  ######################################################
format_slider_Price = "%d"
label_priceBCH = ":green[BCH] : Current Price"

slider_PriceBCH = st.sidebar.slider(label_priceBCH,
                                    1.0, 100000.0, 190.02, .1,
                                    format_slider_Price)

###############################################################################
st.sidebar.divider()
###############################################################################

#### BLOCK REWARD SELECTOR (BOTH)  ############################################

blockReward = st.sidebar.selectbox('Choose block reward (Default: 6.25)',
                                   (50, 25, 12.5, 6.25, 3.125, 1.5625,
                                    .78125, .390625, .195325, .09765625, 0),
                                    3)

# (6 blocks per hour * 24 hours) * (block reward)
totalDailyBlockRewards = ((6*24) * blockReward)

###############################################################################



#### MAIN START  #############################################################

col1, col2 = st.columns(2)


with col1:
    st.header("BTC")
    st.divider()
    st.write('<font size="+5">', str(round(slider_BTC_TPS)),'</font>','</br> Max. TPS (Transactions per Second)', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(max_daily_transactions_BTC)),'</font>','</br> Max. Daily Transactions (Full Blocks)', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', str(round(slider_exaHashes_BTC)),'</font>','</br> Hashrate (in Exahashes/s))', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(slider_energyUsageYearlyTwH_BTC)),'</font>','</br> Energy Usage (TwH/Yearly)', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', '$', str(round(slider_PriceBTC)),'</font>','</br> Price (in USD)', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', str(round(blockReward)),'</font>','</br> Block Reward (in Bitcoins, BTC)', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(totalDailyBlockRewards)),'</font>','</br> Total Daily Block Reward (in Bitcoins, BTC)', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', '$', str(round(totalDailyBlockRewards * slider_PriceBTC)),'</font>','</br> Total Daily Block Reward (if sold to USD)', unsafe_allow_html=True)

    ''' BTC Info here'''


with col2:
    st.header("BCH")
    st.divider()
    st.write('<font size="+5">', str(round(slider_BCH_TPS)),'</font>','</br> Max. TPS (Transactions per Second)', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(max_daily_transactions_BCH)),'</font>','</br> Max. Daily Transactions (Full Blocks)', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', str(round(slider_exaHashes_BCH)),'</font>','</br> Hashrate (in Exahashes/s))', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(energyUsageYearlyTwH_BCH)),'</font>','</br> Energy Usage (TwH/Yearly)', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', '$', str(round(slider_PriceBCH)),'</font>','</br> Price (in USD)', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', str(round(blockReward)),'</font>','</br> Block Reward (in Bitcoins, BCH)', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(totalDailyBlockRewards)),'</font>','</br> Total Daily Block Reward (in Bitcoins, BCH)', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', '$', str(round(totalDailyBlockRewards * slider_PriceBCH)),'</font>','</br> Total Daily Block Reward (if sold to USD)', unsafe_allow_html=True)

    '''BCH Info Here'''


################################
# * First lets discuss security budget costs
# * Column 1: Per KwH Cost, .007 to .30
# * Column 2: energyUsageYearlyKwH_BTC * Col1 , energyUsageYearlyKwH_BCH * Col1

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


df

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['col1', 'col2', 'col3'])

chart_data

# st.line_chart(
#     chart_data,
#     x = 'col1',
#     y = ['col2', 'col3'],
#     color = ['#FF0000', '#0000FF']  # Optional
# )

# st.line_chart(
#     df,
#     x = 'Electricity Cost (per KwH)',
#     y = ['Yearly, BTC Security Budget','Yearly, BCH Security Budget'],
#     color = ['#FF0000'])


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
