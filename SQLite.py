import pandas
import pandas_datareader as dr
import math
import datetime as dt
import sqlite3


##opens connection to SSMIF.db
conn = sqlite3.connect('SSMIF.db')
c = conn.cursor()


'''
Creates a table called Stock_Data if it doesn't exist
Columns are timestamp, open, high, low, close, and adj_closes
Timestamp is the primary key
'''

c.execute("""CREATE TABLE IF NOT EXISTS "Stock_Data" (
            "Timestamp" INTEGER NOT NULL,
            "Open" DECIMAL(10, 2),
            "High" DECIMAL(10, 2),
            "Low" DECIMAL(10, 2),
            "Close" DECIMAL(10, 2),
            "Adj_Close" DECIMAL(10, 2) );""")
conn.commit()
conn.close()


def Fill_Table(ticker):
    ##opens connection to SSMIF.db
    conn = sqlite3.connect('SSMIF.db')
    c = conn.cursor()

    ##uses pandas datareader to fetch 2019 data for the given ticker from yahoo finance 
    data = dr.DataReader(ticker, 'yahoo',start = "2019-1-1", end = "2019-12-31")

    ##iterat through the stocks data
    for date, row in data.iterrows():
        ##create a timestamp from the date index
        timestamp = date.timestamp()

        ##prepare an insertStatemnt with variables that will be provided when the statement is being executed 
        insertStatement = """INSERT INTO Stock_Data (Timestamp, Open, High, Low, Close, Adj_Close) VALUES (?,?,?,?,?, ?);"""
        dataToInsert = (timestamp, row['Open'], row['High'],row['Low'],row['Close'],row['Adj Close'])
        ##execute insert statement
        c.execute(insertStatement, dataToInsert)

    ##commit and close the database connection
    conn.commit()
    conn.close()
    

def Daily_Returns(adjCloseValues):
    ##declares and initializes an array pctChanges to hold percent changes
    pctChanges = []

    ##iterates through adjusted close values starting at index 1
    for i in (list(range(1, len(adjCloseValues)))):
        ##calculates and appends individual percent changes to pctChangess
        pctChanges.append((adjCloseValues[i]-adjCloseValues[i-1])/adjCloseValues[i-1])
        
    return pctChanges

def Monthly_VaR(confidenceLevel=0.05):
    ##opens connection to SSMIF.dbs
    conn = sqlite3.connect('SSMIF.db')
    ##Get a list of field values, not tuples representing rows
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    ##prepare a select statement to get adjusted close values
    selectStatement = "SELECT Adj_Close FROM Stock_Data"
    ##execute select statement
    c.execute(selectStatement)
    ##get data from executed statement
    data = c.fetchall()
    ##close connection
    conn.close()

    ##get daily returns 
    dailyReturns = Daily_Returns(data)
    ##sort daily returns in ascending order
    dailyReturns.sort()
    ##finds the index at which the daily value at risk is by multiplying the confidence level by the amount of data 
    num = int(round(confidenceLevel*(len(dailyReturns))))
    
    return dailyReturns[num-1]*math.sqrt(21)

    
    

