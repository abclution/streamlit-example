import streamlit as st
import pandas as pd
import numpy as np

# from collections import namedtuple
# import altair as alt
# import math


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

st.sidebar.write("The energy usage of the BCH network is proportional based on its hashrate in comparison to BTC's energy usage and hashrate.")

###############################################################################
st.sidebar.divider()
###############################################################################



###############################################################################
st.sidebar.write('<font size="+5">Prices in USD','</font>', '</br>', '(Not yet updated dynamically )', unsafe_allow_html=True)
###############################################################################
#### BTC PRICING SLIDER  ######################################################
format_slider_Price = "%d"
label_priceBTC = ":orange[BTC Network] *(Default: 26091.70)*"

slider_PriceBTC = st.sidebar.slider(label_priceBTC,
                                    1.0, 100000.0, 26091.70, .1,
                                    format_slider_Price)

#### BCH PRICING SLIDER  ######################################################
format_slider_Price = "%d"
label_priceBCH = ":green[BCH Network] *(Default: 190.02)*"

slider_PriceBCH = st.sidebar.slider(label_priceBCH,
                                    1.0, 100000.0, 190.02, .1,
                                    format_slider_Price)

###############################################################################
st.sidebar.divider()
###############################################################################


###############################################################################
st.sidebar.write('<font size="+5">Block Reward','</font>', '</br>', '(Amount of Bitcoins awarded as prize for mining.)', unsafe_allow_html=True)
###############################################################################
#### BLOCK REWARD SELECTOR (BOTH)  ############################################

blockReward = st.sidebar.selectbox('Choose block reward *(Default: 6.25)*',
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


###############################################################################
st.divider()
###############################################################################




tab1, tab2 = st.tabs(["Security Budget Costs Chart", "Security Budget Costs Data"])

with tab1:
   st.header("Chart")
#    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("Data")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)



###############################################################################
st.divider()
###############################################################################

energyUsageYearlyKwH_BTC = 1000000
energyUsageYearlyKwH_BCH = 34567
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

st.line_chart(
    df,
    x='Electricity Cost (per KwH)',
    color=['#de0007', '#00ff22']
    )


#    y=['Yearly, BCH Security Budget','Yearly, BTC Security Budget'],

#    y=['Yearly, BTC Security Budget','Yearly, BCH Security Budget'],
