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

#st.number_input(label, min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
start_value = st.sidebar.number_input('Lowest Electricity Price, KwH (Default: .007)', .001, .50, .007, .001, '%f', help="Loaaawasdfasdferrrrrrrrr")
end_value = st.sidebar.number_input('Highest Electricity Price, KwH (Default: .25)', .001, .50, .25, .001, '%f', help="Highestaaa prasdfasdice")
step = st.sidebar.number_input('Stepping for Charts (Default: .001)', .001, .50, .001, .001, '%f', help="Stepping asdfasaaadf")


# start_value = 0.007
# end_value = 0.35
# step = 0.001
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

    st.write('<font size="+5">', str(round(((energyUsageYearlyKwH_BTC/365) / max_daily_transactions_BTC),2)), '</font>', '</br> KwH Per Transaction', unsafe_allow_html=True)

#   st.write('<font size="+5">', str(energyUsageYearlyKwH_BTC/365),'</font>','</br> KwH Per Day', unsafe_allow_html=True)

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
    
    st.write('<font size="+5">', str(round(( (energyUsageYearlyKwH_BCH / 365) / max_daily_transactions_BCH),2)), '</font>', '</br> KwH Per Transaction', unsafe_allow_html=True)
    
#    st.write('<font size="+5">', str(energyUsageYearlyKwH_BCH / 365),'</font>','</br> KwH Per Day', unsafe_allow_html=True)

    '''BCH Info Here'''



















###############################################################################
st.divider()  # YEARLY - SECURITY BUDGET CHART AND TABLE
###############################################################################

# * First lets discuss security budget costs
# * Column 1: Per KwH Cost, .007 to .30
# * Column 2: energyUsageYearlyKwH_BTC * Col1 , energyUsageYearlyKwH_BCH * Col1

# Define the range of values
# start_value = 0.007
# end_value = 0.35
# step = 0.001

# Create a list of values for column 1
costPerKwH = [round(start_value + i * step, 3) for i in range(int((end_value - start_value) / step) + 1)]

# Create a dictionary to hold the data
data = {
    "Electricity Cost per KwH": costPerKwH,
    "BTC, Yearly Security Budget": [value * energyUsageYearlyKwH_BTC for value in costPerKwH],
    "BCH, Yearly Security Budget": [value * energyUsageYearlyKwH_BCH for value in costPerKwH]
}

df = pd.DataFrame(data)

tab1, tab2 = st.tabs(["Yearly Security Budget Costs (aka Electric Bill) - Chart", "Yearly Security Budget Costs (aka Electric Bill)  - Data"])

with tab1:
    st.header("Yearly Cost of Electricity (Security Budget) for (Given Hashrate X Cost per KwH) Chart")
    st.line_chart(
        df,
        x='Electricity Cost per KwH',
        y=['BTC, Yearly Security Budget','BCH, Yearly Security Budget'],
        color=[colorBCH, colorBTC]
        )

with tab2:
    st.header("Data")
    df
''' A simple linear chart showing the effects of electricity price and hashrate interaction (Yearly Scale). 
The very simple formula for determining the cost of the security budget is as follows:
 - Determine the KwH/year used by each network.
 - Multiply the KwH/year * cost per KwH.
 - Make chart.

Suggested exercises include:
 - Adjust both the BTC + BCH hashrate to verify they match, as they are both calculated with identical efficiency.
 - Adjust the BTC "Energy usage in TwH" to get an idea of how the cost of the security budget/electricity bill scales.

Unfortunatly, due to the massive difference in scale, the BCH network looks quite flat. Lets split these charts up and drill down into the daily view.
 '''


























###############################################################################
st.divider()  # DAILY, SPLIT - SECURITY BUDGET CHART AND TABLE WITH BLOCK REWARD
###############################################################################
# # ! This is a simple, linear chart.
# * Next lets see what the costs look like by day.
# * Same as above but divided by 365
# * 

# Define the range of values
# start_value = 0.007
# end_value = 0.14
# step = 0.001

# Create a list of values for column 1
costPerKwH = [round(start_value + i * step, 3) for i in range(int((end_value - start_value) / step) + 1)]

col1, col2 = st.columns(2)
with col1:

    tab1, tab2 = st.tabs(["Chart", "Data"])

    with tab1:
        st.header(":orange[BTC] Daily Security Budget & Block Reward (USD)")
        data = {
            "Electricity Cost per KwH": costPerKwH,
            "BTC, Daily Security Budget": [(value * energyUsageYearlyKwH_BTC)/365 for value in costPerKwH],
            "BTC, Daily (USD) Block Reward": [(totalDailyBlockRewards * slider_PriceBTC) for value in costPerKwH]

        }
        df = pd.DataFrame(data)
        st.line_chart(
            df,
            x='Electricity Cost per KwH',
            y=['BTC, Daily Security Budget','BTC, Daily (USD) Block Reward'],
            color=['#ff0320',colorBTC]
            )
        '''Daily cost of :orange[BTC] security budget with the :red[red line representing the daily block rewards value, sold to USD @ current prices.]'''

        '''With default settings, :orange[BTC] at around .059/Kwh electricity price, the block reward by itself is no longer sufficient to pay for the security budget.  '''

    
    
    with tab2:
        df
    


with col2:

    tab1, tab2 = st.tabs(["Chart", "Data"])

    with tab1:
        st.header(":green[BCH] Daily Security Budget & Block Reward (USD)")
        data = {
            "Electricity Cost per KwH": costPerKwH,
            "BCH, Daily Security Budget": [(value * energyUsageYearlyKwH_BCH)/365 for value in costPerKwH],
            "BCH, Daily (USD) Block Reward": [(totalDailyBlockRewards * slider_PriceBCH) for value in costPerKwH]
        }
        df = pd.DataFrame(data)
        st.line_chart(
            df,
            x='Electricity Cost per KwH',
            y=['BCH, Daily Security Budget','BCH, Daily (USD) Block Reward'],
            color=['#ff0320', colorBCH]
            )
    
        ''' Daily cost of :green[BCH] security budget with the :red[red line representing the daily block rewards, sold to USD @ current prices.]'''
        '''With default settings, :green[BCH] at around .0648/Kwh electricity price, the block reward by itself is no longer sufficient to pay for the security budget.  '''

    with tab2:
        df

''' Simple linear charts showing the effects of electricity price and hashrate interaction on a Daily Scale as well as the zero point where block rewards no longer cover the cost of running the networks.

The very simple formula for determining the cost of the security budget is as follows:
 - Determine the KwH/year used by each network.
 - Multiply the KwH/year * cost per KwH.
 - Divide by 365
 - Make chart.

 '''

'''
Some suggested exercises: 
 - Change the "Block Reward" amount as well as the price for both :orange[BTC] & :green[BCH] to see how the chart interacts.
 - Adjust the "Hashrate" of :green[BCH], notice how it affects the :green[BCH] chart.
 - Adjust the "Hashrate" of :orange[BTC]. Notice how strangely it affects the :green[BCH] chart instead of the :orange[BTC] chart. 
     - This is because the power usage for :green[BCH] is derived from the efficiency ratio of the orange:[BTC] network.
     - The power usage for :orange[BTC] is found from here: https://ccaf.io/cbnsi/cbeci
     - The hashrate for :orange[BTC] & :green[BCH] are found here: https://www.fork.lol/pow/hashrate
   - We use the hashrate to power usage ratio from :orange[BTC] and use it to derive :green[BCH] power usage based on :green[BCH] current hashrate. 
     - This assumes each network has equivalent efficiency in terms of the mining machines used.
 - Adjust the "Energy Usage in TwH" :orange[BTC]. Again, this affects both :orange[BTC] & :green[BCH] charts. :red[Remember], :green[BCH] electric efficiencies are derived from :orange[BTC], but scaled for its own hashrate.
    - Raising "Energy Usage in TwH" for :orange[BTC] while keeping the "Hashrate" the same, or lowering it simulates LESS efficient mining machines on both :orange[BTC] & :green[BCH] networks. 
    - Lowering "Energy Usage in TwH" for :orange[BTC] while keeping the "Hashrate" the same, or increasing it simulates MORE efficient mining machines on both :orange[BTC] & :green[BCH] networks. 

'''




























###############################################################################
st.divider()
###############################################################################


# * Next lets discuss if block reward covers security budget costs
# * Same as above but divided by 365
# * 

# data = {
#     "Electricity Cost (per KwH)": costPerKwH,
#     "Daily, BTC Security Costs minus Block Reward": [((value * energyUsageYearlyKwH_BTC)/365) - (totalDailyBlockRewards * slider_PriceBTC) for value in costPerKwH],
#     "Daily, BCH Security Costs minus Block Reward": [((value * energyUsageYearlyKwH_BCH)/365) - (totalDailyBlockRewards * slider_PriceBCH) for value in costPerKwH]
    
# }

# data = {
#     "Electricity Cost (per KwH)": costPerKwH,
#     "Daily, BTC Security Costs minus Block Reward": [((value * energyUsageYearlyKwH_BTC)/365) for value in costPerKwH],
#     "Daily, BTC Block Reward (USD)": [(totalDailyBlockRewards * slider_PriceBTC) for value in costPerKwH],
#     "Daily, BCH Security Costs minus Block Reward": [((value * energyUsageYearlyKwH_BCH)/365) for value in costPerKwH],
#     "Daily, BCH Block Reward (USD)": [(totalDailyBlockRewards * slider_PriceBCH) for value in costPerKwH]
    
# }

data = {
    "Electricity Cost (per KwH)": costPerKwH,
    "Daily, BCH Security Costs minus Block Reward": [((value * energyUsageYearlyKwH_BCH)/365) for value in costPerKwH],
    "Daily, BCH Block Reward (USD)": [(totalDailyBlockRewards * slider_PriceBCH) for value in costPerKwH]
    
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






































###############################################################################
st.divider()
###############################################################################

colorBTC = "#F2A900"
colorBCH = "#0AC18E"

