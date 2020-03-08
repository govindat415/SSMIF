import pandas
import pandas_datareader as dr
import math
import statistics as st
import datetime as dt


def Daily_Returns(df):
    ##from the given stock dataframe, grabs the adjusted close values and returns the series of percent changes
    return df["Adj Close"].pct_change()
    


def Monthly_VaR(ticker, confidenceLevel=0.05):
    ##uses pandas datareader to fetch 2019 data for the given ticker from yahoo finance 
    data = dr.DataReader(ticker, 'yahoo',start = "2019-1-1", end = "2019-12-31")
    ##calculates daily returns for the stock 
    dailyReturns = Daily_Returns(data)
    ##fills in NaN values with 0 to avoid errors during future calculations
    dailyReturns.fillna(0)
    ##sorts dailyReturns in ascending order
    dailyReturns.sort_values(inplace=True, ascending=True)
    ##finds the index at which the daily value at risk is by multiplying the confidence level by the amount of data 
    num = int(round(confidenceLevel*(dailyReturns.count())))

    count = 0 ## used to keep track of the index
    var = 0 ##creates the variable to store the value at risk
    
    for date, dailyReturn in dailyReturns.iteritems():
        ##Once num is calculated, the for loop iterates through the daily returns up to the index at which the daily Value at Risk value is
        if(count == num-1):        
            var = dailyReturn
            break
        count = count + 1
    ##returns daily value at risk multiplied by square root of 21 to get monthly value at risk as there are 21 trading days in a month
    return var*math.sqrt(21)
    
def Monthly_CVaR(ticker, confidenceLevel=0.05):
    ##uses pandas datareader to fetch 2019 data for the given ticker from yahoo finance 
    stock_df = dr.DataReader(ticker, 'yahoo',start = "2019-1-1", end = "2019-12-31")
    ##calculates daily returns for the stock 
    dailyReturns = Daily_Returns(stock_df)
    
    ##fills in NaN values with 0 to avoid errors during future calculations
    dailyReturns.fillna(0)
    
    ##Renamese the daily returns series as it was previously labeled 'Adj Close'
    dailyReturns.rename('Returns', inplace=True)
    
    ##concatenated the stock data with the calculated daily returns
    full_stock = pandas.concat([stock_df,dailyReturns],axis=1)
    
    ##sorts the stock dataframe by Returns in ascending order
    full_stock.sort_values(["Returns"], inplace=True, ascending=True)
    
    ##finds the index at which the daily value at risk is by multiplying the confidence level by the amount of data 
    num = int(round(confidenceLevel*(dailyReturns.count())))
    
    ##uses the statistics package to calculate the mean of the returns
    ##returns the mean multiplied by th square root of 21 to get monthly CVaR
    return st.mean(full_stock['Returns'][:num-1])*math.sqrt(21)
    
def Monthly_Volatility(ticker):
    ##uses pandas datareader to fetch 2019 data for the given ticker from yahoo finance 
    stock_df = dr.DataReader(ticker, 'yahoo',start = "2019-1-1", end = "2019-12-31")

    ##calculates daily returns for the stock 
    dailyReturns = Daily_Returns(stock_df)

    ##fills in NaN values with 0 to avoid errors during future calculations
    dailyReturns.fillna(0)

    ##Renamese the daily returns series as it was previously labeled 'Adj Close'
    dailyReturns.rename('Returns', inplace=True)

    ##concatenated the stock data with the calculated daily returns
    full_stock = pandas.concat([stock_df,dailyReturns],axis=1)

    ##uses the statistics package to calculate the mean of the returns
    daily_returns_mean = st.mean(full_stock['Returns'][1:])

    ##returns the standard deviation of the daily returns multiplied by the square root of 21
    return st.stdev(full_stock['Returns'][1:], daily_returns_mean)*math.sqrt(21)




