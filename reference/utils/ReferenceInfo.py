# -*- coding: utf-8 -*-
import tushare as ts
from sqlalchemy import create_engine
from utilAll.Constants import *
from utilAll.FormatDate import *
import pandas as pd


class ReferenceInfo:
    engine_sql = create_engine(SQL_ENG_NAME)

    def setProfitData(self,year = None,topNo=50, isSave = False,tableName = REFERENCE_PROFIT_DATA):
        [yearNow, quarter] = getYearQuarter(year, None)
        df = ts.profit_data(year = yearNow,top=topNo)
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getProfitData(self,tableName = BASE_STOCK_BASICS):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setForecastData(self,year=None,quarter=None, number = 1, isSave = False,tableName = REFERENCE_FORECAST_DATA):
        [year, quarter] = getYearQuarter(year, quarter)
        for i in range(0,number):
            try:
                df = ts.forecast_data(year, quarter)
                df['date'] =str(year) + str(quarter)
                if isSave is True:
                    df.to_sql(tableName,self.engine_sql, if_exists='append')
                quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError,e:
                print e

    def getForecastData(self, tableName = REFERENCE_FORECAST_DATA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setXsgData(self,year=None,month=None, number = 1, isSave = False,tableName = REFERENCE_XSG_DATA):
        [year, month] = getYearMonth(year, month)
        for i in range(0,number):
            try:
                df = ts.xsg_data(year, month)
                if month<10:
                    df['date'] =str(year) +'0'+ str(month)
                else:
                    df['date'] = str(year) + str(month)
                if isSave is True:
                    df.to_sql(tableName,self.engine_sql, if_exists='append')
                    month = month - 1
                if month < 1:
                    month = 12
                    year = year - 1
            except IOError,e:
                print e

    def getXsgData(self, tableName = REFERENCE_XSG_DATA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setFundHoldings(self,year=None,quarter=None, number = 1, isSave = False,tableName = REFERENCE_HUND_HOLDINGS):
        [year, quarter] = getYearQuarter(year, quarter)
        for i in range(0,number):
            try:
                df = ts.fund_holdings(year, quarter)
                df['date'] =str(year) + str(quarter)
                if isSave is True:
                    df.to_sql(tableName,self.engine_sql, if_exists='append')
                    quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError,e:
                print e

    def getFundHoldings(self, tableName = REFERENCE_HUND_HOLDINGS):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setNewStocks(self,  isSave = False,tableName = REFERENCE_NEW_STOCKS):
        try:
            df = ts.new_stocks()
            if isSave is True:
                df.to_sql(tableName,self.engine_sql, if_exists='append')
        except IOError,e:
                print e

    def getNewStocks(self, tableName = REFERENCE_NEW_STOCKS):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setShMargins(self,endTime =None,number =1, isSave = False,tableName = REFERENCE_SH_MARGINS):
        [startTime,endTime] = getStartTime(endTime = endTime, number=number)
        try:
            df = ts.sh_margins(startTime,endTime)
            if isSave is True:
                df.to_sql(tableName,self.engine_sql, if_exists='append')
        except IOError,e:
                print e

    def getShMargins(self, tableName = REFERENCE_SH_MARGINS):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setShMarginDetails(self,endTime =None,number =1, isSave = False,tableName = REFERENCE_SH_MARGINS_DETAILS):
        [startTime,endTime] = getStartTime(endTime = endTime, number=number)
        try:
            df = ts.sh_margin_details(start = startTime,end = endTime)
            if isSave is True:
                df.to_sql(tableName,self.engine_sql, if_exists='append')
        except IOError,e:
                print e

    def getShMarginDetails(self, tableName = REFERENCE_SH_MARGINS_DETAILS):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setSzMargins(self,endTime =None,number =1, isSave = False,tableName = REFERENCE_SH_MARGINS):
        [startTime,endTime] = getStartTime(endTime = endTime, number=number)
        try:
            df = ts.sz_margins(startTime,endTime)
            if isSave is True:
                df.to_sql(tableName,self.engine_sql, if_exists='append')
        except IOError,e:
                print e

    def getSzMargins(self, tableName = REFERENCE_SH_MARGINS):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setSzMarginDetails(self,endTime =None,startTime = None, isSave = False,tableName = REFERENCE_SH_MARGINS_DETAILS):
        dateList = getdatelist(startTime,endTime)
        dfAll = None
        try:
            for dateItem in dateList:
                df = ts.sz_margin_details(dateItem)
                if dfAll is None:
                    dfAll = df.copy()
                else:
                    dfAll = dfAll.append(df)
            dfAll.drop_duplicates()
            if isSave is True:
                df.to_sql(tableName,self.engine_sql, if_exists='append')
        except IOError,e:
                print e

    def getSzMarginDetails(self, tableName = REFERENCE_SH_MARGINS_DETAILS):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def getAllReferenceInfo(self,year = None, isSave = False):
        self.setProfitData(year=2016, topNo=5000, isSave=True)
        self.setForecastData(year=2016, quarter=4, number=1, isSave=True)
        self.setXsgData(year = 2017, month=12, number = 12, isSave = True)
        self.setFundHoldings(year=2017, quarter=4, number=4, isSave=True)
        self.setNewStocks(isSave = True)
        self.setShMargins(endTime = '2017-12-25',number = 365, isSave = True)
        self.setShMarginDetails(endTime = '2015-12-25',number = 365, isSave = True)



if __name__ == '__main__':
    reference =  ReferenceInfo()
    print reference.setShMarginDetails(endTime = '2015-12-25',number = 365, isSave = True)