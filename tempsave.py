
# * First lets discuss security budget costs
# * Column 1: Per KwH Cost, .007 to .30
# * Column 2: energyUsageYearlyKwH_BTC * Col1 , energyUsageYearlyKwH_BCH * Col1

# Define the range of values
start_value = 0.007
end_value = 0.35
step = 0.001

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
