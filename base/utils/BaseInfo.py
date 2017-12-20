import tushare as ts
from sqlalchemy import create_engine
from utilAll.Constants import *
from utilAll.FormatDate import *
import pandas as pd
import datetime


class BaseInfo:
    engine_sql = create_engine(SQL_ENG_NAME)


    def setStockBasics(self,isSave = False,tableName = BASE_STOCK_BASICS):
        df = ts.get_stock_basics()
        if isSave is True:
            df.to_sql(tableName,self.engine_sql, if_exists='append')
        return df

    def getStockBasics(self,tableName = BASE_STOCK_BASICS):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setReportData(self,year=None,quarter=None, number = 1, isSave = False,tableName = BASE_REPORT_DATA):
        [year, quarter] = getYearQuarter(year, quarter)
        for i in range(0,number):
            try:
                df = ts.get_report_data(year, quarter)
                df['date'] =str(year) + str(quarter)
                if isSave is True:
                    df.to_sql(tableName,self.engine_sql, if_exists='append')
                quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError,e:
                print e

    def getReportData(self, tableName = BASE_REPORT_DATA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setProfitData(self, year=None, quarter=None, number=1, isSave=False, tableName=BASE_PROFIT_DATA):
        [year, quarter] = getYearQuarter(year, quarter)
        for i in range(0, number):
            try:
                df = ts.get_profit_data(year, quarter)
                df['date'] = str(year) + str(quarter)
                if isSave is True:
                    df.to_sql(tableName, self.engine_sql, if_exists='append')
                quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError, e:
                print e

    def getProfitData(self, tableName=BASE_PROFIT_DATA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setOperationData(self,year=None,quarter=None, number = 1,isSave = False,tableName = BASE_OPERATION_DATA):
        [year, quarter] = getYearQuarter(year, quarter)
        for i in range(0, number):
            try:
                df = ts.get_profit_data(year,quarter)
                df['date'] = str(year) + str(quarter)
                if isSave is True:
                    df.to_sql(tableName, self.engine_sql, if_exists='append')
                quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError, e:
                print e

    def getOperationData(self, tableName = BASE_OPERATION_DATA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setGrowthData(self,year=None,quarter=None, number = 1,isSave = False,tableName = BASE_GROWTH_DATA):
        [year,quarter] = getYearQuarter(year,quarter)
        for i in range(0, number):
            try:
                df = ts.get_profit_data(year,quarter)
                df['date'] = str(year) + str(quarter)
                if isSave is True:
                    df.to_sql(tableName, self.engine_sql, if_exists='append')
                quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError, e:
                print e

    def getGrowthData(self, tableName = BASE_GROWTH_DATA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setDebtpayingData(self,year=None,quarter=None, number = 1,isSave = False,tableName = BASE_DEBTPAYINT_DATA):
        [year,quarter] = getYearQuarter(year,quarter)
        for i in range(0, number):
            try:
                df = ts.get_profit_data(year,quarter)
                df['date'] = str(year) + str(quarter)
                if isSave is True:
                    df.to_sql(tableName, self.engine_sql, if_exists='append')
                quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError, e:
                print e

    def getDebtpayingData(self, tableName = BASE_DEBTPAYINT_DATA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setCashflowData(self,year=None,quarter=None, number = 1,isSave = False,tableName = BASE_CASHFLOW_DATA):
        [year,quarter] = getYearQuarter(year,quarter)
        for i in range(0, number):
            try:
                df = ts.get_profit_data(year,quarter)
                df['date'] = str(year) + str(quarter)
                if isSave is True:
                    df.to_sql(tableName, self.engine_sql, if_exists='append')
                quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError, e:
                print e

    def getCashflowData(self, tableName = BASE_CASHFLOW_DATA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def getAllBaseInfo(self,year=None,quarter=None, number = 1,isSave = False):
        [year, quarter] = getYearQuarter(year, quarter)
        self.setStockBasics(isSave = isSave)
        self.setReportData(year= year,quarter = quarter,number=number,isSave = isSave)
        self.setProfitData(year=year, quarter=quarter, number=number, isSave=isSave)
        self.setOperationData(year=year, quarter=quarter, number=number, isSave=isSave)
        self.setGrowthData(year=year, quarter=quarter, number=number, isSave=isSave)
        self.setDebtpayingData(year=year, quarter=quarter, number=number, isSave=isSave)
        self.setCashflowData(year=year, quarter=quarter, number=number, isSave=isSave)


if __name__ == '__main__':
    baseeng = BaseInfo()
    df = baseeng.setCashflowData(year= 2016,quarter = 4,number=12,isSave = True)






