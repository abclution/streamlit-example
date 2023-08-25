from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:

farts
"""

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

st.dataframe(df, use_container_width=True)

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))


# st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

#! st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
#! Formatter for int/float supports: %d %e %f %g %i Formatter for date/time/datetime uses Moment.js notation: https://momentjs.com/docs/#/displaying/format/

seconds_per_day = 86400

#### FORMATS #################################################################
format_slider_TPS = "%d"
format_slider_energyUsageYearlyTwH = "%d"

format_slider_exaHashes_BTC = "%d"
format_slider_exaHashes_BCH = "%d"

format_slider_PriceBTC = "%d"
format_slider_PriceBCH = "%d"

#### FORMATS #################################################################

#### LABELS #################################################################
label_BTC_TPS = "BTC Network, Maximum Transactions Per Second"
label_BCH_TPS = "BCH Network, Maximum Transactions Per Second" 

label_energyUsageYearlyTwH_BTC = "BTC: Yearly energy usage of entire network in Terrawatt Hours, found here: https://ccaf.io/cbnsi/cbeci " 

label_exaHashes_BTC = "BTC: Current Exahashes (7 Day AVG)"
label_exaHashes_BCH = "BCH: Current Exahashes (7 Day AVG)"

label_priceBTC = "BTC: Current Price"
label_priceBCH = "BCH: Current Price"

#### LABELS #################################################################

#### SIDEBAR #################################################################
slider_BTC_TPS = st.sidebar.slider(label_BTC_TPS, 1, 7, 7, 1, format_slider_TPS)
slider_BCH_TPS = st.sidebar.slider(label_BCH_TPS, 1, 10000, 224, 1, format_slider_TPS)

slider_exaHashes_BTC = st.sidebar.slider(label_exaHashes_BTC, 1.0, 1000.0, 402.2, .1, format_slider_exaHashes_BTC)
slider_exaHashes_BCH = st.sidebar.slider(label_exaHashes_BCH, 1.0, 1000.0, 2.67, .1, format_slider_exaHashes_BCH)

slider_energyUsageYearlyTwH_BTC = st.sidebar.slider(label_energyUsageYearlyTwH_BTC, 1.0, 1000.0, 145.02, .1, format_slider_energyUsageYearlyTwH)
# ! No slider for BCH as its energy usage is derived from BTC energy usage per exahash.

slider_PriceBTC = st.sidebar.slider(label_priceBTC, 1.0, 100000.0, 26091.70, .1, format_slider_PriceBTC)
slider_PriceBCH = st.sidebar.slider(label_priceBCH, 1.0, 100000.0, 190.02, .1, format_slider_PriceBCH)


#### SIDEBAR #################################################################

#### MAIN #################################################################
max_daily_transactions_BTC = seconds_per_day * slider_BTC_TPS
max_daily_transactions_BCH = seconds_per_day * slider_BCH_TPS

energyUsageYearlyKwH_BTC = slider_energyUsageYearlyTwH_BTC * 1000000000

st.write('##BTC Maximum Daily Transactions:', max_daily_transactions_BTC)
st.write('##BCH Maximum Daily Transactions:', max_daily_transactions_BCH)

st.write('energyUsageYearlyTwH_BTC:', slider_energyUsageYearlyTwH_BTC)
