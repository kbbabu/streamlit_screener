import pandas as pd
import streamlit as st
from scr_fund import *
st.title("Stock fundamentals of Indian Companies")
stocks = ('ADANIENT','ADANIPORTS','APOLLOHOSP','ASIANPAINT','AXISBANK','BAJAJ-AUTO','BAJFINANCE','BAJAJFINSV','BPCL','BHARTIARTL','BRITANNIA','CIPLA','COALINDIA','DIVISLAB','DRREDDY','EICHERMOT','GRASIM','HCLTECH','HDFCBANK','HDFCLIFE','HEROMOTOCO','HINDALCO','HINDUNILVR','HDFC','ICICIBANK','ITC','INDUSINDBK','INFY','JSWSTEEL','KOTAKBANK','LT','M&M','MARUTI','NTPC','NESTLEIND','ONGC','POWERGRID','RELIANCE','SBILIFE','SBIN','SUNPHARMA','TCS','TATACONSUM','TATAMOTORS','TATASTEEL','TECHM','TITAN','UPL','ULTRACEMCO','WIPRO')

N50 = pd.read_csv("https://archives.nseindia.com/content/indices/ind_nifty50list.csv").Symbol
NN50 = pd.read_csv("https://archives.nseindia.com/content/indices/ind_niftynext50list.csv").Symbol
#N100 = pd.read_csv("https://archives.nseindia.com/content/indices/ind_nifty100list.csv").Symbol
#N200 = pd.read_csv("https://archives.nseindia.com/content/indices/ind_nifty200list").Symbol
N_M50 = pd.read_csv("https://archives.nseindia.com/content/indices/ind_niftymidcap50list.csv").Symbol
#N_M100 = pd.read_csv("https://archives.nseindia.com/content/indices/ind_niftymidcap100list.csv").Symbol
N_S50 = pd.read_csv("https://archives.nseindia.com/content/indices/ind_niftysmallcap50list.csv").Symbol
#N_S100 = pd.read_csv("https://archives.nseindia.com/content/indices/ind_niftysmallcap100list.csv").Symbol

status = st.radio("Choose your preferred format:",('NIFTY_50','NIFTY_Next_50','NIFTY_Midcap_50','NIFTY_Smallcap_50','Search'))#'NIFTY_Next_50','NIFTY_Midcap_50','NIFTY_Smallcap_50',
if(status=='NIFTY_50'):
    selected_stock = st.selectbox("Select stocks from NIFTY 50", N50)
    try:
        st.write(st.dataframe(fundamental(selected_stock)))
    except:
        pass
elif(status=='NIFTY_Next_50'):
    selected_stock1 = st.selectbox("Select stocks from NIFTY Next 50", NN50)
    try:
        st.write(st.dataframe(fundamental(selected_stock1)))
    except:
        pass
elif(status=='NIFTY_Midcap_50'):
        selected_stock2 = st.selectbox("Select stocks from NIFTY Midcap 50", N_M50)
        try:
            st.write(st.dataframe(fundamental(selected_stock2)))
        except:
            pass
elif(status=='NIFTY_Smallcap_50'):
    selected_stock3 = st.selectbox("Select stocks from NIFTY SmallCap 50", N_S50)
    try:
        st.write(st.dataframe(fundamental(selected_stock3)))
    except:
        pass

else:
    try:
        saj = st.text_input(
            "Enter ticker name (by default TCS ticker name present you can change the ticker name as per your requirement:",
            "TCS")
        st.dataframe(fundamental(saj))
        st.text(f"Nifty 50 stock ticker for your reference : {stocks}")
    except:
        pass
    #else:
    #    st.write("Stock details not available")

