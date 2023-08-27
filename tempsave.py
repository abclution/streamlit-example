col1, col2 = st.columns(2)
with col1:

    tab1, tab2 = st.tabs(["Chart", "Data"])

    with tab1:
        st.header(":orange[BTC] Per Transaction Fee Needed to Pay for Remainder of (Security Budget - Block Reward) (USD)")
        data = {
            "Electricity Cost per KwH": costPerKwH,
            "BTC, Daily Security Budget - Block Reward USD": [ ((value * energyUsageYearlyKwH_BTC)/365) - (totalDailyBlockRewards * slider_PriceBTC) for value in costPerKwH],
            "BTC, Per Transaction Fee Needed": [(((value * energyUsageYearlyKwH_BTC)/365) - (totalDailyBlockRewards * slider_PriceBTC))/max_daily_transactions_BTC  for value in costPerKwH]

        }
        df = pd.DataFrame(data)
        st.line_chart(
            df,
            x='Electricity Cost per KwH',
            y=['BTC, Daily Security Budget - Block Reward USD','BTC, Per Transaction Fee Needed'],
            color=['#ff0320',colorBTC]
            )
        '''Daily cost of :orange[BTC] security budget with the :red[red line representing the daily block rewards value, sold to USD @ current prices.]'''

        '''With default settings, :orange[BTC] at around .059/Kwh electricity price, the block reward by itself is no longer sufficient to pay for the security budget.  '''
    with tab2:
        df


with col2:

    tab1, tab2 = st.tabs(["Chart", "Data"])

    with tab1:
        st.header(":green[BCH] Per Transaction Fee Needed to Pay for Remainder of (Security Budget - Block Reward) (USD)")
        data = {
            "Electricity Cost per KwH": costPerKwH,
            "BCH, Daily Security Budget - Block Reward USD": [ ((value * energyUsageYearlyKwH_BCH)/365) - (totalDailyBlockRewards * slider_PriceBCH) for value in costPerKwH],
            "BCH, Per Transaction Fee Needed": [(((value * energyUsageYearlyKwH_BCH)/365) - (totalDailyBlockRewards * slider_PriceBCH))/max_daily_transactions_BCH  for value in costPerKwH]
        }
        df = pd.DataFrame(data)
        st.line_chart(
            df,
            x='Electricity Cost per KwH',
            y=['BCH, Daily Security Budget - Block Reward USD','BCH, Per Transaction Fee Needed'],
            color=['#ff0320', colorBCH]
            )
    
        ''' Daily cost of :green[BCH] security budget with the :red[red line representing the daily block rewards, sold to USD @ current prices.]'''
        '''With default settings, :green[BCH] at around .0648/Kwh electricity price, the block reward by itself is no longer sufficient to pay for the security budget.  '''

    with tab2:
        df
