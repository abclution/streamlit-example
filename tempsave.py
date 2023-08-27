
col1, col2 = st.columns(2)
with col1:
    st.header("BTC")
    st.divider()
    st.write('<font size="+5">', str(round(slider_BTC_TPS)),'</font>','</br> Max. TPS (Transactions per Second)', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(max_daily_transactions_BTC)),'</font>','</br> Max. Daily Transactions (Full Blocks)', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', str(round(slider_exaHashes_BTC,2)),'</font>','</br> Hashrate (in Exahashes/s))', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(slider_energyUsageYearlyTwH_BTC,2)),'</font>','</br> Energy Usage (TwH/Yearly)', unsafe_allow_html=True)
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
    st.write('<font size="+5">', str(round(slider_exaHashes_BCH,2)),'</font>','</br> Hashrate (in Exahashes/s))', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(energyUsageYearlyTwH_BCH,2)),'</font>','</br> Energy Usage (TwH/Yearly)', unsafe_allow_html=True)
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









#### MAIN START  #############################################################

col1, col2, col3 = st.columns(3)
with col1:
    st.header("BTC")
    st.divider()
    st.write('<font size="+5">', str(round(slider_BTC_TPS)),'</font>', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(max_daily_transactions_BTC)),'</font>', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', str(round(slider_exaHashes_BTC,2)),'</font>', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(slider_energyUsageYearlyTwH_BTC,2)),'</font>', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', '$', str(round(slider_PriceBTC)),'</font>', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', str(round(blockReward)),'</font>', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(totalDailyBlockRewards)),'</font>', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', '$', str(round(totalDailyBlockRewards * slider_PriceBTC)),'</font>', unsafe_allow_html=True)

    st.write('<font size="+5">', str(round(((energyUsageYearlyKwH_BTC/365) / max_daily_transactions_BTC),2)), '</font>', unsafe_allow_html=True)

#   st.write('<font size="+5">', str(energyUsageYearlyKwH_BTC/365),'</font>','</br> KwH Per Day', unsafe_allow_html=True)

    ''' BTC Info here'''

with col2:
    st.header("Settings")
    st.divider()
    st.write('Max. TPS (Transactions per Second)', unsafe_allow_html=True)
    st.write('Daily Transactions (Full Blocks)', unsafe_allow_html=True)
    st.divider()
    st.write('Hashrate (in Exahashes/s)', unsafe_allow_html=True)
    st.write('Energy Usage (TwH/Yearly)', unsafe_allow_html=True)
    st.divider()
    st.write('Price (in USD)', unsafe_allow_html=True)
    st.divider()
    st.write('Block Reward (in Bitcoins, BCH)', unsafe_allow_html=True)
    st.write('Total Daily Block Reward (in Bitcoins, BCH)', unsafe_allow_html=True)
    st.divider()
    st.write('Total Daily Block Reward (if sold to USD)', unsafe_allow_html=True)
    
    st.write('KwH Per Transaction', unsafe_allow_html=True)
    
#    st.write('<font size="+5">', str(energyUsageYearlyKwH_BCH / 365),'</font>','</br> KwH Per Day', unsafe_allow_html=True)

with col3:
    st.header("BCH")
    st.divider()
    st.write('<font size="+5">', str(round(slider_BCH_TPS)),'</font>', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(max_daily_transactions_BCH)),'</font>', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', str(round(slider_exaHashes_BCH,2)),'</font>', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(energyUsageYearlyTwH_BCH,2)),'</font>', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', '$', str(round(slider_PriceBCH)),'</font>', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', str(round(blockReward)),'</font>', unsafe_allow_html=True)
    st.write('<font size="+5">', str(round(totalDailyBlockRewards)),'</font>', unsafe_allow_html=True)
    st.divider()
    st.write('<font size="+5">', '$', str(round(totalDailyBlockRewards * slider_PriceBCH)), unsafe_allow_html=True)
    
    st.write('<font size="+5">', str(round(( (energyUsageYearlyKwH_BCH / 365) / max_daily_transactions_BCH),2)), '</font>', unsafe_allow_html=True)
    
#    st.write('<font size="+5">', str(energyUsageYearlyKwH_BCH / 365),'</font>','</br> KwH Per Day', unsafe_allow_html=True)

    '''BCH Info Here'''






















































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
