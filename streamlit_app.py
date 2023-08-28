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
st.sidebar.write('<font size="+5">Max. TPS','</font>', '</br>', '(Maximum Transactions per Second, Full Blocks)', unsafe_allow_html=True)
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

###############################################################################
st.sidebar.divider()
###############################################################################
###############################################################################
st.sidebar.write('<font size="+5">Chart Settings','</font>', '</br>', '(Settings that control the scale of the chart. Helpful for zooming in.)', unsafe_allow_html=True)
###############################################################################



#st.number_input(label, min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
start_value = st.sidebar.number_input('Lowest Electricity Price, KwH (Default: .007)', .001, .50, .007, .001, '%f', help="Loaaawasdfasdferrrrrrrrr")
end_value = st.sidebar.number_input('Highest Electricity Price, KwH (Default: .25)', .001, .50, .25, .001, '%f', help="Highestaaa prasdfasdice")
step = st.sidebar.number_input('Stepping for Charts (Default: .001)', .001, .50, .001, .001, '%f', help="Stepping asdfasaaadf")


# start_value = 0.007
# end_value = 0.35
# step = 0.001
#### MAIN START  #############################################################
col_font_statistic = '<center> <font size="+8">'
end_col_font_statistic = '</font> </center> </br>'

col_font_label = '<center> <font size="+4">'
end_col_font_label = '</font> </center>'

col1, col2, col3 = st.columns(3)


col1, col2 = st.columns(2)
with col1:
    st.header(":orange[Bitcoin - BTC]")
    st.divider()
    st.write(col_font_statistic, str(round(slider_BTC_TPS)), end_col_font_statistic, col_font_label, 'Max. TPS </br> (Transactions per Second)', end_col_font_label, unsafe_allow_html=True)
    st.write(col_font_statistic, str(round(max_daily_transactions_BTC)),end_col_font_statistic, col_font_label, 'Max. Daily Transactions </br> (Full Blocks)', end_col_font_label, unsafe_allow_html=True)
    st.divider()
    st.write(col_font_statistic, str(round(slider_exaHashes_BTC,2)),end_col_font_statistic, col_font_label, 'Hashrate </br> (in Exahashes/s)', end_col_font_label, unsafe_allow_html=True)
    st.write(col_font_statistic, str(round(slider_energyUsageYearlyTwH_BTC,2)),end_col_font_statistic, col_font_label, 'Energy Usage </br> (TwH/Yearly)', end_col_font_label, unsafe_allow_html=True)
    st.divider()
    st.write(col_font_statistic, '$', str(round(slider_PriceBTC)),end_col_font_statistic, col_font_label, 'Price </br> (in USD)', end_col_font_label, unsafe_allow_html=True)
    st.divider()
    st.write(col_font_statistic, str(round(blockReward)),end_col_font_statistic, col_font_label, 'Block Reward </br> (in Bitcoins, BTC)', end_col_font_label, unsafe_allow_html=True)
    st.write(col_font_statistic, str(round(totalDailyBlockRewards)),end_col_font_statistic, col_font_label, 'Total Daily Block Reward </br> (in Bitcoins, BTC)', end_col_font_label, unsafe_allow_html=True)
    st.divider()
    st.write(col_font_statistic, '$', str(round(totalDailyBlockRewards * slider_PriceBTC)),end_col_font_statistic, col_font_label, 'Total Daily Block Reward </br> (if sold to USD)', end_col_font_label, unsafe_allow_html=True)

    st.write(col_font_statistic, str(round(((energyUsageYearlyKwH_BTC/365) / max_daily_transactions_BTC),2)), end_col_font_statistic, col_font_label,  'KwH Per Transaction', end_col_font_label, unsafe_allow_html=True)

#   st.write(col_font_statistic, str(energyUsageYearlyKwH_BTC/365),end_font,'KwH Per Day', end_col_font_label, unsafe_allow_html=True)

    ''' BTC Info here'''


with col2:
    st.header(":green[Bitcoin Cash - BCH]")
    st.divider()
    st.write(col_font_statistic, str(round(slider_BCH_TPS)),end_col_font_statistic, col_font_label, 'Max. TPS </br> (Transactions per Second)', end_col_font_label, unsafe_allow_html=True)
    st.write(col_font_statistic, str(round(max_daily_transactions_BCH)),end_col_font_statistic, col_font_label, 'Max. Daily Transactions </br> (Full Blocks)', end_col_font_label, unsafe_allow_html=True)
    st.divider()
    st.write(col_font_statistic, str(round(slider_exaHashes_BCH,2)),end_col_font_statistic, col_font_label, 'Hashrate </br> (in Exahashes/s)', end_col_font_label, unsafe_allow_html=True)
    st.write(col_font_statistic, str(round(energyUsageYearlyTwH_BCH,2)),end_col_font_statistic, col_font_label, 'Energy Usage </br> (TwH/Yearly)', end_col_font_label, unsafe_allow_html=True)
    st.divider()
    st.write(col_font_statistic, '$', str(round(slider_PriceBCH)),end_col_font_statistic, col_font_label, 'Price </br> (in USD)', end_col_font_label, unsafe_allow_html=True)
    st.divider()
    st.write(col_font_statistic, str(round(blockReward)),end_col_font_statistic, col_font_label, 'Block Reward </br> (in Bitcoins, BCH)', end_col_font_label, unsafe_allow_html=True)
    st.write(col_font_statistic, str(round(totalDailyBlockRewards)),end_col_font_statistic, col_font_label, 'Total Daily Block Reward </br> (in Bitcoins, BCH)', end_col_font_label, unsafe_allow_html=True)
    st.divider()
    st.write(col_font_statistic, '$', str(round(totalDailyBlockRewards * slider_PriceBCH)),end_col_font_statistic, col_font_label, 'Total Daily Block Reward </br> (if sold to USD)', end_col_font_label, unsafe_allow_html=True)
    
    st.write(col_font_statistic, str(round(( (energyUsageYearlyKwH_BCH / 365) / max_daily_transactions_BCH),2)), end_col_font_statistic, col_font_label,  'KwH Per Transaction', end_col_font_label, unsafe_allow_html=True)
    
#    st.write(col_font_statistic, str(energyUsageYearlyKwH_BCH / 365),'</font>','KwH Per Day', end_col_font_label, unsafe_allow_html=True)

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

tab1, tab2 = st.tabs(["Chart", "Data"])

with tab1:
    st.header("Yearly Cost of Electricity (Security Budget) for :orange[BTC] & :green[BCH] (USD)")
    st.line_chart(
        df,
        x='Electricity Cost per KwH',
        y=['BTC, Yearly Security Budget','BCH, Yearly Security Budget'],
        color=[colorBCH, colorBTC]
        )

with tab2:
    st.header("Data")
    df
''' A simple linear chart showing the effects of electricity price and hashrate interaction at a yearly scale. Unfortunatly, due to the massive difference in scale, the :green[BCH] network looks quite flat. In the next chart we will split these charts up and drill down into the daily view.

The very simple formula for determining the cost of the yearly security budget is as follows:
 - Determine the KwH/year used by each network.
 - Multiply the KwH/year * cost per KwH & make chart.

Suggested exercises include:
 - Adjust both the :orange[BTC] + :green[BCH] hashrate to verify they match, as they are both calculated with identical efficiency.
 - Adjust the :orange[BTC] "Energy usage in TwH" to get an idea of how the cost of the security budget/electricity bill scales.
'''


























###############################################################################
st.divider()  # DAILY, SPLIT - SECURITY BUDGET CHART AND TABLE WITH BLOCK REWARD
###############################################################################
# # ! This is a simple, linear chart.
# * Next lets see what the costs look like by day.
# * Same as above but divided by 365
# * 

st.header("Daily Cost of Electricity (Security Budget) for :orange[BTC] & :green[BCH]")
''':red[Red line overlay representing the respective daily block rewards, sold to USD @ current prices.]'''
# Create a list of values for column 1
costPerKwH = [round(start_value + i * step, 3) for i in range(int((end_value - start_value) / step) + 1)]

col1, col2 = st.columns(2)
with col1:

    tab1, tab2 = st.tabs(["Chart", "Data"])

    with tab1:
        st.header(":orange[BTC] Daily Security Budget (USD)")
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
        st.header(":green[BCH] Daily Security Budget (USD)")
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
''' So its easy to see that the current security budget is NOT covered by the block rewards. Thankfully we have transaction fees. Let visit those.'''






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






















###############################################################################
st.divider()
###############################################################################
# * So if the block reward doesn't cover the bare costs for the security budget
# * and transaction fees are supposed to, lets see what the transaction fees are
# * likely to be for a set of variables.



# Create a list of values for column 1
costPerKwH = [round(start_value + i * step, 3) for i in range(int((end_value - start_value) / step) + 1)]


tab1, tab2 = st.tabs(["Chart", "Data"])

with tab1:
    st.header(":orange[BTC] & :green[BCH] Per Transaction Fee Needed to Pay for Remainder of (Security Budget (Electricity Costs) - Block Reward (Sold to USD @ Current Prices))")
    data = {
        "Electricity Cost per KwH": costPerKwH,
        "BTC, Per Transaction Fee Needed": [(((value * energyUsageYearlyKwH_BTC)/365) - (totalDailyBlockRewards * slider_PriceBTC))/max_daily_transactions_BTC  for value in costPerKwH],
        "BCH, Per Transaction Fee Needed": [(((value * energyUsageYearlyKwH_BCH)/365) - (totalDailyBlockRewards * slider_PriceBCH))/max_daily_transactions_BCH  for value in costPerKwH]

    }
    df = pd.DataFrame(data)
    st.line_chart(
        df,
        x='Electricity Cost per KwH',
        y=['BTC, Per Transaction Fee Needed','BCH, Per Transaction Fee Needed'],
        color=[colorBCH, colorBTC]
        )
    '''This is the cost per transaction *needed* for each :orange[BTC] and :green[BCH] to maintain their security budget (electricity bill) adjusted for having sold the daily block rewards to USD @ current prices.]'''

with tab2:
    df

'''
Some suggested exercises for this chart:
 - Validate the presented data. Match the :orange[BTC] & :green[BCH] settings and make sure the chart lines match. I suggest the following settings to assist in setting the sliders which are unfriendly for detail work.
   - "Max TPS", bring :green[BCH] all the way down to 1, then use keyboard to move it to 7.
   - "Hashrate", move both :orange[BTC] & :green[BCH] fully to the right, 1000. They have equal efficiency so this is fine and "Energy Usage in TwH" is not needed for this chart.
   - "Prices in USD", move both :orange[BTC] & :green[BCH] fully to the left, 1. Or the right, 100000. Leave one of them a tick off so you can observe both lines.
   - Great, once you are satisfied they match, you should have confidence to continue.
 - I suggest to refresh the page to reset to defaults.
 -    


'''


'''
Ok, so lets look into the far future.
All of this has been based on the current fact regarding the cost of electricity.

If we ever manage to figure out superconductors and fusion, the price of electricity is going to go torwards zero.

So in effect at this point, the price of electricity doesn't matter. This will cause several interesting thingss. Lets explore this.
Additionally there are definitly miners who already produce and use electricity for free.

Additionally the block reward ever increasingly moves towards zero as well. This will be an interesting thing as well.

The breakpoint will be only the availiablility and efficiency of the mining equipment.
'''





































###############################################################################
st.divider()
###############################################################################







###############################################################################
st.divider()
###############################################################################
