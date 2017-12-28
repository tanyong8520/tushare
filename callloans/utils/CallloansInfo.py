# -*- coding: utf-8 -*-
import tushare as ts
from sqlalchemy import create_engine
from utilAll.Constants import *
from utilAll.FormatDate import *
import pandas as pd

class CallloansInfo:
    engine_sql = create_engine(SQL_ENG_NAME)

    def setShiborData(self,year = None,number = 1, isSave = False,tableName = CALLLOANS_SHIBOR_DATA):
        yearList = getYearList(year,number)
        for yearItem in yearList:
            df = ts.shibor_data(yearItem)
            if isSave is True:
                df.to_sql(tableName,self.engine_sql, if_exists='append')
        return df

    def getShiborData(self,tableName = CALLLOANS_SHIBOR_DATA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setShiborQuoteData(self,year = None,number = 1, isSave = False,tableName = CALLLOANS_SHIBOR_QUOTE_DATA):
        yearList = getYearList(year,number)
        for yearItem in yearList:
            df = ts.shibor_quote_data(yearItem)
            if isSave is True:
                df.to_sql(tableName,self.engine_sql, if_exists='append')
        return df

    def getShiborQuoteData(self,tableName = CALLLOANS_SHIBOR_QUOTE_DATA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setShiborMaData(self,year = None,number = 1, isSave = False,tableName = CALLLOANS_MA_DATA):
        yearList = getYearList(year,number)
        for yearItem in yearList:
            df = ts.shibor_ma_data(yearItem)
            if isSave is True:
                df.to_sql(tableName,self.engine_sql, if_exists='append')
        return df

    def getShiborMaData(self,tableName = CALLLOANS_MA_DATA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setLprData(self,year = None,number = 1, isSave = False,tableName = CALLLOANS_LPR_DATA):
        yearList = getYearList(year,number)
        for yearItem in yearList:
            df = ts.lpr_data(yearItem)
            if isSave is True:
                df.to_sql(tableName,self.engine_sql, if_exists='append')
        return df

    def getLprData(self,tableName = CALLLOANS_LPR_DATA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setLprMaData(self,year = None,number = 1, isSave = False,tableName = CALLLOANS_LPR_MA_DATA):
        yearList = getYearList(year,number)
        for yearItem in yearList:
            df = ts.lpr_ma_data(yearItem)
            if isSave is True:
                df.to_sql(tableName,self.engine_sql, if_exists='append')
        return df

    def getLprMaData(self,tableName = CALLLOANS_LPR_MA_DATA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def getAllCallloans(self):
        # 无法调用
        self.setShiborData(year=2017,number = 1,isSave = True)
        self.setShiborQuoteData(year=2017, number=1, isSave=True)
        self.setShiborMaData(year=2017, number=1, isSave=True)
        self.setLprData(year=2017, number=1, isSave=True)
        self.setLprMaData(year=2017, number=1, isSave=True)

if __name__ == '__main__':
    callloansInfo = CallloansInfo()
    df = callloansInfo.setLprMaData(year=2016,number = 1,isSave = True)