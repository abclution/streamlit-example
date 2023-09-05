import streamlit as st
import pandas as pd
import numpy as np

# from collections import namedtuple
# import altair as alt
# import math
# page2.py
# import streamlit as st
# If page1 already executed, this should write True


#st.set_page_config(layout="wide")
st.set_page_config(page_title="The Present, The Past & The Future of Bitcoin.", page_icon="📈",layout="wide")
st.write(st.session_state["shared"])



colorBTC = "#F2A900"
colorBCH = "#0AC18E"
seconds_per_day = 86400


"""
# The Present, The Past & The Future of Bitcoin. 
## A simulation of the economics and usability of Bitcoin as it is, as it was and as it will be.


This is meant as a tool for anyone who wants to simulate the economic & end user reality of Bitcoin(s) with an (somewhat) rigorous analysis of the most important aspects of Bitcoin. 

### How to use this tool

#### Settings & Options Sidebar
- On first open of this tool you should be reading this text as well as a visible sidebar menu on the left hand of your screen with various sliders and options.
- If this sidebar is missing, please press the button at the uppermost top left that should look like ">". 
    - On mobile this menu is collapsed on start due to space constraints.
- Any changes made to the settings in the sidebar menu will immediately take effect on both the numbers and charts throughout the presentation.
- The sidebar has more than a full screen worth of options, please make sure to scroll fully down to validate you have seen all availiable settings.
- It is suggested before adjusting any options, to go on to each section carefully and read the information and perform any of the "Suggested Excercises"
- To reset all options to defaults, please refresh the page. All default options are set to the actual current numbers of each network, August 2023.

#### Charts
- Charts can be clicked on to full screen them, mouse wheel to zoom in/out. You can also hover over each line/point to see more detailed information. They can also be exported to various formats.
- Additionally the data used to derive the charts should be availiable in the tab next to each chart, as well as the formula used to derive the datasets.
- The entirety of the source code used to generate this page is also available.

"""
###############################################################################
st.sidebar.write(
    '<font size="+5">Max. TPS',
    "</font>",
    "</br>",
    "(Maximum Transactions per Second, Full Blocks)",
    unsafe_allow_html=True,
)
###############################################################################
#### BTC TPS SLIDER  ##########################################################
format_slider_TPS = "%d"
label_BTC_TPS = ":orange[BTC Network] *(Default: 7)*"
slider_BTC_TPS = st.sidebar.slider(label_BTC_TPS, 1, 7, 7, 1, format_slider_TPS)

max_daily_transactions_BTC = seconds_per_day * slider_BTC_TPS

#### BCH TPS SLIDER  ##########################################################
format_slider_TPS = "%d"
label_BCH_TPS = ":green[BCH Network] *(Default: 224)*"
slider_BCH_TPS = st.sidebar.slider(label_BCH_TPS, 1, 10000, 224, 1, format_slider_TPS)

max_daily_transactions_BCH = seconds_per_day * slider_BCH_TPS
###############################################################################
st.sidebar.divider()
###############################################################################


###############################################################################
st.sidebar.write(
    '<font size="+5">Hashrate',
    "</font>",
    "</br>",
    "(Current hashrate in exa-hashes, 7 Day AVG.)",
    unsafe_allow_html=True,
)
###############################################################################
#### BTC HASHRATE SLIDER  #####################################################
format_slider_exaHashes = "%d"
label_exaHashes_BTC = ":orange[BTC Network] *(Default: 402.2)*"
slider_exaHashes_BTC = st.sidebar.slider(
    label_exaHashes_BTC, 1.0, 1000.0, 402.2, 0.1, format_slider_exaHashes
)

#### BCH HASHRATE SLIDER  #####################################################
format_slider_exaHashes = "%d"
label_exaHashes_BCH = ":green[BCH Network] *(Default: 2.67)*"
slider_exaHashes_BCH = st.sidebar.slider(
    label_exaHashes_BCH, 1.0, 1000.0, 2.67, 0.1, format_slider_exaHashes
)
###############################################################################
st.sidebar.divider()
###############################################################################


###############################################################################
st.sidebar.write(
    '<font size="+5">Energy Usage in TwH',
    "</font>",
    "</br>",
    "(Yearly energy usage of entire network in Terrawatt Hours, found here, https://ccaf.io/cbnsi/cbeci )",
    unsafe_allow_html=True,
)
###############################################################################
#### BTC ENERGY USAGE SLIDER  #################################################
format_slider_energyUsageYearlyTwH = "%d"
label_energyUsageYearlyTwH_BTC = ":orange[BTC Network] *(Default: 145.02)*"
slider_energyUsageYearlyTwH_BTC = st.sidebar.slider(
    label_energyUsageYearlyTwH_BTC,
    1.0,
    1000.0,
    145.02,
    0.1,
    format_slider_energyUsageYearlyTwH,
)

#### BCH ENERGY USAGE SLIDER  #################################################
# ! No slider for BCH as its energy usage is derived from BTC energy usage per exahash.

# Convert BTC Yearly TwH to KwH, this is because most other calculations are
# done based on the cost of each KwH.
energyUsageYearlyKwH_BTC = slider_energyUsageYearlyTwH_BTC * 1000000000

# Get an energy usage ratio by getting the BTC hashrate and its yearly KwH
exaHashToYearlyKwHRatio = energyUsageYearlyKwH_BTC / slider_exaHashes_BTC

# Multiply the BCH exahashes by the energy usage ratio, this assumes equivalent
# efficiency between the chains equipment. This is a fair comparison.
energyUsageYearlyKwH_BCH = slider_exaHashes_BCH * exaHashToYearlyKwHRatio

# Get BCH yearly TwH used
energyUsageYearlyTwH_BCH = energyUsageYearlyKwH_BCH / 1000000000

st.sidebar.write(
    "The energy usage of the BCH network is proportional based on its hashrate in comparison to BTC's energy usage and hashrate."
)

###############################################################################
st.sidebar.divider()
###############################################################################


###############################################################################
st.sidebar.write(
    '<font size="+5">Prices in USD',
    "</font>",
    "</br>",
    "(Not yet updated dynamically )",
    unsafe_allow_html=True,
)
###############################################################################
#### BTC PRICING SLIDER  ######################################################
format_slider_Price = "%d"
label_priceBTC = ":orange[BTC Network] *(Default: 26091.70)*"

slider_PriceBTC = st.sidebar.slider(
    label_priceBTC, 1.0, 100000.0, 26091.70, 0.1, format_slider_Price
)

#### BCH PRICING SLIDER  ######################################################
format_slider_Price = "%d"
label_priceBCH = ":green[BCH Network] *(Default: 190.02)*"

slider_PriceBCH = st.sidebar.slider(
    label_priceBCH, 1.0, 100000.0, 190.02, 0.1, format_slider_Price
)

###############################################################################
st.sidebar.divider()
###############################################################################


###############################################################################
st.sidebar.write(
    '<font size="+5">Block Reward',
    "</font>",
    "</br>",
    "(Amount of Bitcoins awarded as prize for mining.)",
    unsafe_allow_html=True,
)
###############################################################################
#### BLOCK REWARD SELECTOR (BOTH)  ############################################

blockReward = st.sidebar.selectbox(
    "Choose block reward *(Default: 6.25)*",
    (50, 25, 12.5, 6.25, 3.125, 1.5625, 0.78125, 0.390625, 0.195325, 0.09765625, 0),
    3,
)

# (6 blocks per hour * 24 hours) * (block reward)
totalDailyBlockRewards = (6 * 24) * blockReward
###############################################################################

###############################################################################
st.sidebar.divider()
###############################################################################
###############################################################################
st.sidebar.write(
    '<font size="+5">Chart Settings',
    "</font>",
    "</br>",
    "(Settings that control the scale of the chart. Helpful for zooming in.)",
    unsafe_allow_html=True,
)
###############################################################################


# st.number_input(label, min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
start_value = st.sidebar.number_input(
    "Lowest Electricity Price, KwH (Default: .007)",
    0.001,
    0.50,
    0.007,
    0.001,
    "%f",
    help="Lowest KwH value for charts. Min. .001",
)
end_value = st.sidebar.number_input(
    "Highest Electricity Price, KwH (Default: .25)",
    0.001,
    0.50,
    0.25,
    0.001,
    "%f",
    help="Highest cost per KwH for charts. Max. .50",
)
step = st.sidebar.number_input(
    "Stepping for Charts (Default: .001)",
    0.001,
    0.50,
    0.001,
    0.001,
    "%f",
    help="Stepping for chart generation.",
)


# start_value = 0.007
# end_value = 0.35
# step = 0.001
#### MAIN START  #############################################################
col_font_statistic = '<center> <font size="+8">'
end_col_font_statistic = "</font> </center> </br>"

col_font_label = '<center> <font size="+4">'
end_col_font_label = "</font> </center>"

col1, col2, col3 = st.columns(3)


col1, col2 = st.columns(2)
with col1:
    st.header(":orange[Bitcoin]")
    st.header(":orange[BTC]", divider="orange")
    st.divider()
    st.write(
        col_font_statistic,
        str(round(slider_BTC_TPS)),
        end_col_font_statistic,
        col_font_label,
        "Max. TPS </br> (Transactions per Second)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.write(
        col_font_statistic,
        str(round(max_daily_transactions_BTC)),
        end_col_font_statistic,
        col_font_label,
        "Max. Daily Transactions </br> (Full Blocks)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.divider()
    st.write(
        col_font_statistic,
        str(round(slider_exaHashes_BTC, 2)),
        end_col_font_statistic,
        col_font_label,
        "Hashrate </br> (in Exahashes/s)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.write(
        col_font_statistic,
        str(round(slider_energyUsageYearlyTwH_BTC, 2)),
        end_col_font_statistic,
        col_font_label,
        "Energy Usage </br> (TwH/Yearly)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.divider()
    st.write(
        col_font_statistic,
        "$",
        str(round(slider_PriceBTC)),
        end_col_font_statistic,
        col_font_label,
        "Price </br> (in USD)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.divider()
    st.write(
        col_font_statistic,
        str(round(blockReward)),
        end_col_font_statistic,
        col_font_label,
        "Block Reward </br> (in Bitcoins, BTC)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.write(
        col_font_statistic,
        str(round(totalDailyBlockRewards)),
        end_col_font_statistic,
        col_font_label,
        "Total Daily Block Reward </br> (in Bitcoins, BTC)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.divider()
    st.write(
        col_font_statistic,
        "$",
        str(round(totalDailyBlockRewards * slider_PriceBTC)),
        end_col_font_statistic,
        col_font_label,
        "Total Daily Block Reward </br> (if sold to USD)",
        end_col_font_label,
        unsafe_allow_html=True,
    )

    st.write(
        col_font_statistic,
        str(round(((energyUsageYearlyKwH_BTC / 365) / max_daily_transactions_BTC), 2)),
        end_col_font_statistic,
        col_font_label,
        "KwH Per Transaction",
        end_col_font_label,
        unsafe_allow_html=True,
    )

    #   st.write(col_font_statistic, str(energyUsageYearlyKwH_BTC/365),end_font,'KwH Per Day', end_col_font_label, unsafe_allow_html=True)

    """ BTC Info here"""


with col2:
    st.header(":green[Bitcoin Cash]")
    st.header(":green[BCH]", divider="green")

    st.divider()
    st.write(
        col_font_statistic,
        str(round(slider_BCH_TPS)),
        end_col_font_statistic,
        col_font_label,
        "Max. TPS </br> (Transactions per Second)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.write(
        col_font_statistic,
        str(round(max_daily_transactions_BCH)),
        end_col_font_statistic,
        col_font_label,
        "Max. Daily Transactions </br> (Full Blocks)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.divider()
    st.write(
        col_font_statistic,
        str(round(slider_exaHashes_BCH, 2)),
        end_col_font_statistic,
        col_font_label,
        "Hashrate </br> (in Exahashes/s)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.write(
        col_font_statistic,
        str(round(energyUsageYearlyTwH_BCH, 2)),
        end_col_font_statistic,
        col_font_label,
        "Energy Usage </br> (TwH/Yearly)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.divider()
    st.write(
        col_font_statistic,
        "$",
        str(round(slider_PriceBCH)),
        end_col_font_statistic,
        col_font_label,
        "Price </br> (in USD)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.divider()
    st.write(
        col_font_statistic,
        str(round(blockReward)),
        end_col_font_statistic,
        col_font_label,
        "Block Reward </br> (in Bitcoins, BCH)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.write(
        col_font_statistic,
        str(round(totalDailyBlockRewards)),
        end_col_font_statistic,
        col_font_label,
        "Total Daily Block Reward </br> (in Bitcoins, BCH)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
    st.divider()
    st.write(
        col_font_statistic,
        "$",
        str(round(totalDailyBlockRewards * slider_PriceBCH)),
        end_col_font_statistic,
        col_font_label,
        "Total Daily Block Reward </br> (if sold to USD)",
        end_col_font_label,
        unsafe_allow_html=True,
    )

    st.write(
        col_font_statistic,
        str(round(((energyUsageYearlyKwH_BCH / 365) / max_daily_transactions_BCH), 2)),
        end_col_font_statistic,
        col_font_label,
        "KwH Per Transaction",
        end_col_font_label,
        unsafe_allow_html=True,
    )

    #    st.write(col_font_statistic, str(energyUsageYearlyKwH_BCH / 365),'</font>','KwH Per Day', end_col_font_label, unsafe_allow_html=True)

    """BCH Info Here"""


###############################################################################
st.divider()  # YEARLY - SECURITY BUDGET CHART AND TABLE
###############################################################################
st.header("Bitcoin Mining & Security Budget Economics", divider="rainbow")


# * First lets discuss security budget costs
# * Column 1: Per KwH Cost, .007 to .30
# * Column 2: energyUsageYearlyKwH_BTC * Col1 , energyUsageYearlyKwH_BCH * Col1

# Define the range of values
# start_value = 0.007
# end_value = 0.35
# step = 0.001

# Create a list of values for column 1
costPerKwH = [
    round(start_value + i * step, 3)
    for i in range(int((end_value - start_value) / step) + 1)
]

# Create a dictionary to hold the data
data = {
    "Electricity Cost per KwH": costPerKwH,
    "BTC, Yearly Security Budget": [
        value * energyUsageYearlyKwH_BTC for value in costPerKwH
    ],
    "BCH, Yearly Security Budget": [
        value * energyUsageYearlyKwH_BCH for value in costPerKwH
    ],
}

df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(
    [":bar_chart: Chart", ":clipboard: Data", ":baby_bottle: Formula"]
)

with tab1:
    st.header(
        "Yearly Cost of Electricity (Security Budget) for :orange[BTC] & :green[BCH] (USD)"
    )
    st.line_chart(
        df,
        x="Electricity Cost per KwH",
        y=["BTC, Yearly Security Budget", "BCH, Yearly Security Budget"],
        color=[colorBCH, colorBTC],
    )

with tab2:
    st.header("Data")
    df

with tab3:
    st.header("Formula")
    """The very simple formula for determining the cost of the yearly security budget is as follows:
    - Determine the KwH/year used by each network.
    - Multiply the KwH/year * cost per KwH & make chart."""


""" A simple linear chart showing the price of electricity and its resultant cost of the security budget at a Yearly scale."""

"""> **Unfortunately, due to the massive difference in scale, the :green[BCH] network line looks quite flat. In the next chart we will split these charts up and drill down into the Daily view.**"""

with st.expander(":bulb: CLICK HERE FOR SUGGESTED EXERCISES."):
    """
    - Adjust both the :orange[BTC] + :green[BCH] "Hashrate" setting to equal levels.
        - Verify their lines on the chart match. Understand how they are both calculated with identical efficiency and costs.
    - Adjust the :orange[BTC] "Energy usage in TwH" to get an idea of how the cost of the security budget/electricity bill scales.
    """


###############################################################################
st.divider()  # DAILY, SPLIT - SECURITY BUDGET CHART AND TABLE WITH BLOCK REWARD
###############################################################################
# # ! This is a simple, linear chart.
# * Next lets see what the costs look like by day.
# * Same as above but divided by 365
# *

st.header(
    "Daily Cost of Electricity (Security Budget) for :orange[BTC] & :green[BCH] (USD)"
)
""":red[Red line overlay representing the respective daily block rewards, sold to USD @ current prices.]"""
# Create a list of values for column 1
costPerKwH = [
    round(start_value + i * step, 3)
    for i in range(int((end_value - start_value) / step) + 1)
]

col1, col2 = st.columns(2)
with col1:
    tab1, tab2, tab3 = st.tabs(
        [":bar_chart: Chart", ":clipboard: Data", ":baby_bottle: Formula"]
    )

    with tab1:
        st.header(":orange[BTC] Daily Security Budget (USD)")
        data = {
            "Electricity Cost per KwH": costPerKwH,
            "BTC, Daily Security Budget": [
                (value * energyUsageYearlyKwH_BTC) / 365 for value in costPerKwH
            ],
            "BTC, Daily (USD) Block Reward": [
                (totalDailyBlockRewards * slider_PriceBTC) for value in costPerKwH
            ],
        }
        df = pd.DataFrame(data)
        st.line_chart(
            df,
            x="Electricity Cost per KwH",
            y=["BTC, Daily Security Budget", "BTC, Daily (USD) Block Reward"],
            color=["#ff0320", colorBTC],
        )
        """Daily cost of :orange[BTC] security budget with the :red[red line representing the daily block rewards value, sold to USD @ current prices.]"""

        """With default settings, :orange[BTC] at around .059/Kwh electricity price, the block reward by itself is no longer sufficient to pay for the security budget.  """

    with tab2:
        df

    with tab3:
        """The very simple formula for determining the cost of the security budget is as follows:

        - Determine the KwH/year used by each network.
        - Multiply the KwH/year * cost per KwH.
        - Divide by 365, make chart."""


with col2:
    tab1, tab2, tab3 = st.tabs(
        [":bar_chart: Chart", ":clipboard: Data", ":baby_bottle: Formula"]
    )

    with tab1:
        st.header(":green[BCH] Daily Security Budget (USD)")
        data = {
            "Electricity Cost per KwH": costPerKwH,
            "BCH, Daily Security Budget": [
                (value * energyUsageYearlyKwH_BCH) / 365 for value in costPerKwH
            ],
            "BCH, Daily (USD) Block Reward": [
                (totalDailyBlockRewards * slider_PriceBCH) for value in costPerKwH
            ],
        }
        df = pd.DataFrame(data)
        st.line_chart(
            df,
            x="Electricity Cost per KwH",
            y=["BCH, Daily Security Budget", "BCH, Daily (USD) Block Reward"],
            color=["#ff0320", colorBCH],
        )

        """ Daily cost of :green[BCH] security budget with the :red[red line representing the daily block rewards, sold to USD @ current prices.]"""
        """With default settings, :green[BCH] at around .0648/Kwh electricity price, the block reward by itself is no longer sufficient to pay for the security budget.  """

    with tab2:
        df

    with tab3:
        """The very simple formula for determining the cost of the security budget is as follows:

        - Determine the KwH/year used by each network.
        - Multiply the KwH/year * cost per KwH.
        - Divide by 365, make chart."""

with st.expander(":bulb: CLICK HERE FOR SUGGESTED EXERCISES."):
    """
    Some suggested exercises:
    - Change the "Block Reward" amount as well as the "Prices in USD" for each :orange[BTC] & :green[BCH] to see how the chart interacts.
    - Adjust the "Hashrate" of :green[BCH], notice how it affects the :green[BCH] chart.
    - Adjust the "Hashrate" of :orange[BTC]. Notice how the :orange[BTC] chart stays the same, "Hashrate" ≠ Energy Usage.
        - On the other hand, notice how strangely it affects the :green[BCH] chart instead of the :orange[BTC] chart. This is because the power usage for :green[BCH] is derived from the efficiency ratio of the orange:[BTC] network.
        - The power usage for :orange[BTC] is found from here: https://ccaf.io/cbnsi/cbeci and the hashrate for :orange[BTC] & :green[BCH] are found here: https://www.fork.lol/pow/hashrate
        - We use the hashrate to power usage ratio from :orange[BTC] and use it to derive :green[BCH] power usage based on :green[BCH] current hashrate.
        - This assumes each network has equivalent efficiency in terms of the mining machines used.
    - Adjust the "Energy Usage in TwH" :orange[BTC]. Again, this affects both :orange[BTC] & :green[BCH] charts. :red[Remember], :green[BCH] electric efficiencies are derived from :orange[BTC], but scaled for its own hashrate.
        - Raising "Energy Usage in TwH" for :orange[BTC] while keeping the "Hashrate" the same, or lowering it simulates LESS efficient mining machines on both :orange[BTC] & :green[BCH] networks.
        - Lowering "Energy Usage in TwH" for :orange[BTC] while keeping the "Hashrate" the same, or increasing it simulates MORE efficient mining machines on both :orange[BTC] & :green[BCH] networks.

    """  # noqa: E501


"""Libya is/was cheapest electricity in the world with .007 USD per KwH, feel free to adjust the price ranges in the sidebar.

Now some interesting things start to emerge... once the price per KwH gets close the the cheapest availiable KwH we see that:
 
- The current (6.25) block rewards are no longer sufficient to cover the security budget.
    - @ 25 Bitcoins (BTC) *the block reward* **was enough to cover the energy costs up to about .235/Kwh.**
    - @ 50 Bitcoins (BTC) *the block reward* **was enough to cover the energy costs up to about .45/Kwh.**
    
> **So its easy to see that the current security budget of both :orange[BTC] & :green[BCH] are NOT covered by solely the block rewards any longer. This means it will be necessary for the remaining of the security budget to be covered by the transaction fees which we will visit next.** 

"""  # noqa: E501


###############################################################################
st.divider()
###############################################################################
st.header("Transaction Fees & Security Budget Economics", divider="rainbow")

# * So if the block reward doesn't cover the bare costs for the security budget
# * and transaction fees are supposed to, lets see what the transaction fees are
# * likely to be for a set of variables.


# Create a list of values for column 1
costPerKwH = [
    round(start_value + i * step, 3)
    for i in range(int((end_value - start_value) / step) + 1)
]


tab1, tab2, tab3 = st.tabs(
    [":bar_chart: Chart", ":clipboard: Data", ":baby_bottle: Formula"]
)

with tab1:
    st.header(
        ":orange[BTC] & :green[BCH] Per Transaction Fee Needed to Pay the remainder of the Security Budget (Electricity Costs)"
    )
    """This is the cost per transaction **REQUIRED** for each :orange[BTC] and :green[BCH] to maintain their security budget (electricity bill) adjusted for having sold the daily block rewards to USD @ current prices."""

    data = {
        "Electricity Cost per KwH": costPerKwH,
        "BTC, Per Transaction Fee Needed": [
            (
                ((value * energyUsageYearlyKwH_BTC) / 365)
                - (totalDailyBlockRewards * slider_PriceBTC)
            )
            / max_daily_transactions_BTC
            for value in costPerKwH
        ],
        "BCH, Per Transaction Fee Needed": [
            (
                ((value * energyUsageYearlyKwH_BCH) / 365)
                - (totalDailyBlockRewards * slider_PriceBCH)
            )
            / max_daily_transactions_BCH
            for value in costPerKwH
        ],
    }
    df = pd.DataFrame(data)
    st.line_chart(
        df,
        x="Electricity Cost per KwH",
        y=["BTC, Per Transaction Fee Needed", "BCH, Per Transaction Fee Needed"],
        color=[colorBCH, colorBTC],
    )

with tab2:
    df

with tab3:
    """todo"""

with st.expander(":bulb: CLICK HERE FOR SUGGESTED EXERCISES."):
    """
    - Validate the presented data. Match the :orange[BTC] & :green[BCH] settings and make sure the chart lines match. I suggest the following settings to assist in setting the sliders which are unfriendly for detail work.
    - "Max TPS", bring :green[BCH] all the way down to 1, then use keyboard to move it to 7.
    - "Hashrate", move both :orange[BTC] & :green[BCH] fully to the right, 1000. They have equal efficiency so this is fine and "Energy Usage in TwH" is not needed for this chart.
    - "Prices in USD", move both :orange[BTC] & :green[BCH] fully to the left, 1. Or the right, 100000. Leave one of them a tick off so you can observe both lines.
    - Great, once you are satisfied they match, you should have confidence to continue.
    - I suggest to refresh the page to reset to defaults.
    """  # noqa: E501

col1, col2 = st.columns(2)
with col1:
    """Again sadly, you may have noticed that :green[BCH] seems to have flatlined in comparison to :orange[BTC]."""  # noqa: E501

    """Except this time, the line represents having **much lower fees** to maintain the security budge. But how can :green[BCH] have such lower fees than :orange[BTC]?"""  # noqa: E501

    """**What is going on?**"""

    """The more astute will immediately realize :red[**THE PROBLEM**] here. :thinking_face:"""  # noqa: E501

    """:green[BCH's] level of security, its **"Hashrate"** is a mere fraction of :orange[BTC]! :broken_heart:"""  # noqa: E501

with col2:
    """**Now it all makes makes sense!**"""
    """:green[BCH] cannot possibly compete when its security level and security budget costs approach :orange[BTC's]!!!1!"""  # noqa: E501
    """...or can it. :microphone:"""
    """Feel free to adjust :green[BCH's] **"Hashrate"** to match :orange[BTC's]**"Hashrate"** and look at the chart"""  # noqa: E501
    st.write(
        "In fact :green[BCHs] security level is exactly:",
        '<font size="+6">',
        str(round(((slider_exaHashes_BCH / slider_exaHashes_BTC) * 100), 2)),
        "%",
        "</font>",
        "of :orange[BTCs]",
        unsafe_allow_html=True,
    )


###############################################################################
st.divider()
###############################################################################
st.header("Bitcoin Miner Profits aka Why Mine Bitcoin?", divider="rainbow")
st.header("Everything here and down in work in progress.....", divider="rainbow")


""" So, from the previous charts and exercise, we learned un-intuitively that something BCH is doing makes it better for all those who use it, both the end users and the miners.
Additionally and unexpectedly, we also learned it is much easier for activities, transacting on the BCH network to pay and cover its security budget compared to BTC.
Transaction Fees are lower, and the cost of its security budget, even if its security levels are raised to equal with BTC, are covered much more easily by transaction fees.
All of this, even when its price is much lower than BTC. Very strange indeed."""  # noqa: E501

"""This is what happens when you serve the needs of the many instead of the wishes of a few."""
"""So, in order to find profits, we must decide on some costs. The costs that both affect the production and protection of the Bitcoin networks and scale the most are the electric costs
Here is a new slider where you can choose what the rest of the charts in this section validate or invalidate your notions.
"""  # noqa: E501


""" Add cost of "storage" """
"""Secret is every single thing that could possibly be useful to improve from BTC can be slapped just as easily into BCH.. including lightning."""  # noqa: E501


with st.expander(":bulb: CLICK HERE FOR SUGGESTED EXERCISES."):
    """asfasdfasd"""


# Create a list of values for column 1
# costPerKwH = [round(start_value + i * step, 3) for i in range(int((end_value - start_value) / step) + 1)]

fee_start_value = 0.001
fee_stop_value = 10
fee_step = 0.001
feePerTransaction = [
    round(fee_start_value + i * fee_step, 3)
    for i in range(int((fee_stop_value - fee_start_value) / fee_step) + 1)
]


tab1, tab2, tab3 = st.tabs(
    [":bar_chart: Chart", ":clipboard: Data", ":baby_bottle: Formula"]
)

with tab1:
    st.header(":orange[BTC] & :green[BCH] Miner Profits Now & Future")

    data = {
        "Fee Per Transaction": feePerTransaction,
        "BTC, Daily Miner Profit": [
            (value * max_daily_transactions_BTC) for value in feePerTransaction
        ],
        "BCH, Daily Miner Profit": [
            (value * max_daily_transactions_BCH) for value in feePerTransaction
        ],
    }
    df = pd.DataFrame(data)
    st.line_chart(
        df,
        x="Fee Per Transaction",
        y=["BTC, Daily Miner Profit", "BCH, Daily Miner Profit"],
        color=[colorBCH, colorBTC],
    )

with tab2:
    df

with tab3:
    """todo"""

st.header("A closer look at Transaction Fees", divider="rainbow")

""" So far, we have been approaching the statistics of Bitcoin from a particular angle, The costs of running the network (as a miner!)
And we have been presenting the fee structure as a static, per transaction cost, valued in USD when doing calculations.

Alas, this is not quite correct. Bitcoin fees are not based "per transaction" in fact they are based "satoshis per byte" of size of the data that the transaction itself is composed of."""  # noqa: E501

"""Additionally the data size of a Bitcoin transaction is variable. Many factors can influence the size of the transaction making calculation difficult"""

"""A satoshi is (currently) the smallest unit of Bitcoin currency, 1 satoshi = 0.00000001 BTC/BCH.
If you play with BTC/BCH prices you can see even at a price of $100,000 USD, a satoshi is worth only 1 cent. """  # noqa: E501

col1, col2 = st.columns(2)

with col1:
    st.write(
        "1 :orange[BTC] satoshi is worth </br>",
        '<font size="+6">$',
        str.rstrip(format(slider_PriceBTC / 10000000, ".8f"), "0"),
        "USD </font>",
        unsafe_allow_html=True,
    )


with col2:
    st.write(
        "1 :green[BCH] satoshi is worth </br>",
        '<font size="+6">$',
        str.rstrip(format(slider_PriceBCH / 10000000, ".8f"), "0"),
        "USD </font>",
        unsafe_allow_html=True,
    )
"""In the future, if a satoshi is no longer a negligible amount of value, Bitcoin can be divided into ever smaller units of measure, sub-satoshi measurements.

So as it is currently, the absolute lowest fee level is 1 satoshi per byte.
BTC currently averages between 3-7 satoshis per byte
BCH currently (and intends to continue) an average of 1 satoshi per byte, or lower.

"""  # noqa: E501
"""
Legacy BTC Block Size Limit: 1 MB
Segwit + Taproot BTC Block Size Limit: 4 MB
1 Megabyte = 1048576 bytes 4194304
"""
#### BTC MAXIMUM BILLABLE BYTES SLIDER  #######################################
format_slider_TPS = "%d"
label_BTC_MaxBillableBytes = (
    ":orange[BTC Network] Maximum Billable Bytes *(Default: 1048576)*"
)
BTC_MaxBillableBytes = st.slider(
    label_BTC_MaxBillableBytes, 1048576, 4194304, 1048576, 1, format_slider_TPS
)

#### BTC SATOSHIS PER BYTE TRANSACTION FEE SLIDER SLIDER  #######################################
format_slider_TPS = "%d"
label_BTC_SatoshisPerByte = (
    ":orange[BTC Network] Satoshis Per Byte Transaction Fee *(Default: 1)*"
)
BTC_SatoshisPerByte = st.slider(
    label_BTC_SatoshisPerByte, 1, 1000, 1, 1, format_slider_TPS
)


col1, col2 = st.columns(2)

with col1:
    st.write(
        ":orange[BTC] Max Fees collected per block, in satoshis based on Maximum Billable bytes per block</br>",
        '<font size="+6">',
        str.rstrip(format(BTC_MaxBillableBytes * BTC_SatoshisPerByte, ".8f"), "0"),
        "Satoshis </font>",
        unsafe_allow_html=True,
    )
with col2:
    st.write(
        ":orange[BTC] Max Fees collected per block, in USD</br>",
        '<font size="+6">$',
        str.rstrip(
            format(
                (BTC_MaxBillableBytes * BTC_SatoshisPerByte)
                * (slider_PriceBTC / 10000000),
                ".2f",
            ),
            "0",
        ),
        "USD </font>",
        unsafe_allow_html=True,
    )


"""List of BTC Transactions & Sizes
Each transaction consists of the most common type of transaction in a functional ecosystem, assuming an entity has their entirety of their balance on a single address (1 input), and sends a single payment to another entity, but doesnt spend their entire balance. (2 outputs, change address.)
"""

def transactionTypeInfoBTC(transaction_name,transaction_cost):
    st.write(
        transaction_name,",",
        transaction_cost,
        " vbytes each. ",
        "</br> MAX. transactions per block of this type: ",
        format(BTC_MaxBillableBytes / transaction_cost, ".2f"),
        "</br> Cost in satoshis is ",
        transaction_cost,
        " which equals (approx):",
        round(transaction_cost * (slider_PriceBTC / 10000000), 2), "USD",
        "</br> A block composed solely of these:",
        str(((BTC_MaxBillableBytes / transaction_cost) * (transaction_cost * (slider_PriceBTC / 10000000)))),
        "USD in fees.",
        unsafe_allow_html=True,
    )
col1, col2 = st.columns(2)
with col1:
    transactionTypeInfoBTC("P2PKH Transaction", 226)
    transactionTypeInfoBTC("P2WPKH Transaction", 140.5)
    transactionTypeInfoBTC("P2SH 2-OF-3 MULTISIG Transaction", 371)
    transactionTypeInfoBTC("P2WSH 2-OF-3 MULTISIG Transaction", 201)
    transactionTypeInfoBTC("P2TR (Taproot) Transaction", 154)

with col2:
    '''So looking at the differing types of transactions availiable for the BTC chain, regardless of which one is used the total available "billable" bytes per transactions remains the same.'''
    '''And therefore the maximum amount of fee income miners can receive is only affected by the "satoshis per byte" scaling soley by increasing the charge per byte!'''
    '''However, what does change is how many transactions can fit per block, for users to take advantage of! The least efficient lets us fit 2826 transactions and the most efficient 7463 transactions per block!'''

    '''If we assume a mix of the various transactions per block, we can take the average.'''
    
    # Max amount of these type of transactions per billable block space.
    perBlockP2PKH = (BTC_MaxBillableBytes / 226)
    perBlockP2WPKH = (BTC_MaxBillableBytes / 140.5)
    perBlockP2SH_2OF3_MULTISIG = (BTC_MaxBillableBytes / 371) 
    perBlockP2WSH_2OF3_MULTISIG = (BTC_MaxBillableBytes / 201)
    perBlockP2TR = (BTC_MaxBillableBytes / 154)
    

    BTC_TransPerBlockList = [perBlockP2PKH, perBlockP2WPKH, perBlockP2SH_2OF3_MULTISIG, perBlockP2WSH_2OF3_MULTISIG,perBlockP2TR] 
    avgQntTransPerBTCBlock = sum(BTC_TransPerBlockList) / len(BTC_TransPerBlockList)
    minQntTransPerBTCBlock = max(BTC_TransPerBlockList)
    maxQntTransPerBTCBlock = min(BTC_TransPerBlockList)

    st.write(
        "Average Possible Transactions Per Block (Average All Types Transactions)",
        format(avgQntTransPerBTCBlock,".2f"),
        unsafe_allow_html=True
    )
    st.write(
        "Minimum Possible Transactions Per Block (All P2SH 2-OF-3 MULTISIG Transactions)",
        format(minQntTransPerBTCBlock,".2f"),
        unsafe_allow_html=True
    )
    st.write(
        "Maximum Possible Transactions Per Block (All P2WPKH Transactions)",
        format(maxQntTransPerBTCBlock,".2f"),
        unsafe_allow_html=True
    )
    '''As you can see, with all the protocol improvements in BTC I propose a change to the widely quoted "7 Max. TPS limit for BTC." based on this information.'''
    '''From: 7 TPS = 4200 Transactions per Block'''
    '''To: 8.9 (9) TPS = 5390.99 Transactions per Block'''


###############################################################################
st.sidebar.divider()
###############################################################################

"""
BTC Fee Philosophy - Fees will increase until morale improves.
Keep the blockspace small and full. When blocks are full, people need to compete in the "limited blockspace created fee market" to have their transaction sent.

BCH Fee Philosophy - Always less than a penny no matter what the BCH price is.
Blocks should never be full enough that fees have to increase.
When BCH dollar price increases so much that the smallest divisible unit of BCH is worth more than a penny, we create a even smaller divisible unit
"""  # noqa: E501


"""List of largest BTC blocks ever and stats
https://mempool.space/block/00000000000000000001763c6ac07b72152f7cd9ba42949af2269ff83b379cfd
https://mempool.space/block/0000000000000000000515e202c8ae73c8155fc472422d7593af87aa74f2cf3d
https://blockchair.com/bitcoin/blocks?s=size(desc)#

https://cointelegraph.com/news/the-current-state-of-the-bitcoin-network-and-its-biggest-block
https://news.bitcoin.com/bitcoin-records-largest-mined-block-to-date-4-mb-block-containing-nft-causes-unease-among-small-block-supporters/

https://trustmachines.co/blog/bitcoin-ordinals-reignited-block-size-debate/
https://bitcoin.stackexchange.com/questions/92689/how-is-the-size-of-a-bitcoin-transaction-calculated#:~:text=Each%20Non%2DSegwit%20byte%20of,for%20numbers%20up%20to%20252)
https://bitcoin.stackexchange.com/questions/92587/calculate-transaction-fee-for-external-addresses-which-doesnt-belong-to-my-loca/92600#92600

https://www.semanticscholar.org/paper/How-many-transactions-per-second-can-bitcoin-really-Georgiadis/cd19b9bd1c726df7c6e9d14d9bcfd5104b599a96

https://eprint.iacr.org/2019/416.pdf


https://www.reddit.com/r/Bitcoin/comments/xz2zxj/calculating_batch_throughput_and_its_theoretical/


"""  # noqa: E501

"""Environmental efficiency"""


###############################################################################
st.divider()
###############################################################################

"""
Ok, so lets look into the far future.
All of this has been based on the current fact regarding the cost of electricity.

If we ever manage to figure out superconductors and fusion, the price of electricity is going to go towards zero.

So in effect at this point, the price of electricity doesn't matter. This will cause several interesting things. Lets explore this.
Additionally there are definitely miners who already produce and use electricity for free.

Additionally the block reward ever increasingly moves towards zero as well. This will be an interesting thing as well.

The breakpoint will be only the availability and efficiency of the mining equipment.
"""  # noqa: E501
###############################################################################
st.divider()
###############################################################################


''' Reality check about adoption and transactions. How many tranactions would be happening with all BTC transactions on BCH. And Ether as well etc.'''


'''Lmao.. so I'm trying to research the math behind BTC/BCH maximum transactions per second.. came across this paper which claims BTC can do 27 TPS! But there is a hilarious punchline at the end of the paper about this. Its only 6 pages long if someone wants to have a look https://eprint.iacr.org/2019/416.pdf'''