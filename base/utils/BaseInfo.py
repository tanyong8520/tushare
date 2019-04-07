# -*- coding: utf-8 -*-
import tushare as ts
from sqlalchemy import create_engine

from utilAll import DateUtils
from utilAll.FormatDate import *
from base.models import *
import pandas as pd


class BaseInfo:
    engine_sql = create_engine(SQL_ENG_NAME)
    baseType =StockBasics().baseType
    BASE_INFO_PATH = 'E:/live/tushare/base/stockdates/'

    lastTradeDay = None
    last2TradeDay = None
    def initStockBasics(self,  useNet = False, tableName = BASE_STOCK_BASICS):
        if not useNet:
            stockBasicInfo = pd.read_csv(tableName + ".csv", index_col="code")
        else:
            stockBasicInfo = ts.get_stock_basics();

        if stockBasicInfo is None:
            print 'get stock basice info error'
            return
        stockBasicInfo.to_csv(self.BASE_INFO_PATH +tableName + ".csv", encoding="utf8")

    def getLastTradeDay(self):
        """获取最后一天的交易时间"""
        # todo：后期改为从redis中获取，每天晚上刷新信息的是也要更新此信息
        startDay = DateUtils.getDDayStr(-25);
        data = ts.get_hist_data('sh', startDay)
        indexList = list(data.index)
        indexList.sort()
        indexList.reverse()
        offsetDay = 0
        # offsetDay=1
        self.lastTradeDay = indexList[0 + offsetDay]
        print("lastTradeDay", self.lastTradeDay)
        self.last2TradeDay = data.index[1 + offsetDay]
        print("last2TradeDay", self.last2TradeDay)


    def getStockBasics(self, useNet = False ,tableName = BASE_STOCK_BASICS):
        """获取股票的所有基础信息"""
        if not useNet:
            stockBasicInfo = pd.read_csv(self.BASE_INFO_PATH +tableName +".csv", index_col="code")
        else:
            stockBasicInfo = ts.get_stock_basics();
        stockBasicInfo.to_csv(self.BASE_INFO_PATH +tableName +".csv",encoding="utf8")
        if stockBasicInfo is None:
            print 'get stock basice info error'
            return
        return stockBasicInfo

    def initReportData(self,year=None,quarter=None, number = 1, isSave = False,tableName = BASE_REPORT_DATA):
        """获取制定年份指定季度的业绩报告
        year :那一年
        quarter：那个季度
        number：后续几个季度的数据
        """
        [year, quarter] = getYearQuarter(year, quarter)
        for i in range(0,number):
            try:
                df = ts.get_report_data(year, quarter)
                if df is None:
                    print 'get base report data error'
                    return
                df['date'] =str(year) + str(quarter)
                if isSave is True:
                    df.to_csv(self.BASE_INFO_PATH +tableName + ".csv", encoding="utf8",mode='a')
                    # df.to_sql(tableName,self.engine_sql, if_exists='append',dtype=self.baseType[tableName])
                quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError,e:
                print e

    def getReportData(self, tableName = BASE_REPORT_DATA):
        df = pd.read_csv(self.BASE_INFO_PATH +tableName +".csv", index_col="code")
        return df

    def initProfitData(self, year=None, quarter=None, number=1, isSave=False, tableName=BASE_PROFIT_DATA):
        """获取制定年份指定季度的盈利能力
                year :那一年
                quarter：那个季度
                number：后续几个季度的数据
                """
        [year, quarter] = getYearQuarter(year, quarter)
        for i in range(0, number):
            try:
                df = ts.get_profit_data(year, quarter)
                if df is None:
                    print 'get base profit info error'
                    return
                df['date'] = str(year) + str(quarter)
                if isSave is True:
                    df.to_csv(self.BASE_INFO_PATH +tableName + ".csv", encoding="utf8", mode='a')
                    # df.to_sql(tableName, self.engine_sql, if_exists='append',dtype=self.baseType[tableName])
                quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError, e:
                print e

    def getProfitData(self, tableName=BASE_PROFIT_DATA):
        df = pd.read_csv(self.BASE_INFO_PATH +tableName +".csv", index_col="code")
        return df

    def intiOperationData(self,year=None,quarter=None, number = 1,isSave = False,tableName = BASE_OPERATION_DATA):
        """获取制定年份指定季度的营运能力
                        year :那一年
                        quarter：那个季度
                        number：后续几个季度的数据
                        """
        [year, quarter] = getYearQuarter(year, quarter)
        for i in range(0, number):
            try:
                df = ts.get_operation_data(year,quarter)
                if df is None:
                    print 'get base operation info error'
                    return
                df['date'] = str(year) + str(quarter)
                if isSave is True:
                    df.to_csv(self.BASE_INFO_PATH +tableName + ".csv", encoding="utf8", mode='a')
                    # df.to_sql(tableName, self.engine_sql, if_exists='append',dtype=self.baseType[tableName])
                quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError, e:
                print e

    def getOperationData(self, tableName = BASE_OPERATION_DATA):
        df = pd.read_csv(self.BASE_INFO_PATH +tableName + ".csv", index_col="code")
        return df

    def setGrowthData(self,year=None,quarter=None, number = 1,isSave = False,tableName = BASE_GROWTH_DATA):
        """获取制定年份指定季度的成长能力
                                year :那一年
                                quarter：那个季度
                                number：后续几个季度的数据
                                """
        [year,quarter] = getYearQuarter(year,quarter)
        for i in range(0, number):
            try:
                df = ts.get_growth_data(year,quarter)
                if df is None:
                    print 'get base growth info error'
                    return
                df['date'] = str(year) + str(quarter)
                if isSave is True:
                    df.to_csv(self.BASE_INFO_PATH +tableName + ".csv", encoding="utf8", mode='a')
                    # df.to_sql(tableName, self.engine_sql, if_exists='append',dtype=self.baseType[tableName])
                quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError, e:
                print e

    def getGrowthData(self, tableName = BASE_GROWTH_DATA):
        df = pd.read_csv(self.BASE_INFO_PATH +tableName + ".csv", index_col="code")
        # df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setDebtpayingData(self,year=None,quarter=None, number = 1,isSave = False,tableName = BASE_DEBTPAYINT_DATA):
        """获取制定年份指定季度的偿债能力
        year :那一年
        quarter：那个季度
        number：后续几个季度的数据
        """
        [year,quarter] = getYearQuarter(year,quarter)
        for i in range(0, number):
            try:
                df = ts.get_debtpaying_data(year,quarter)
                if df is None:
                    print 'get base debtpaying info error'
                    return
                df['date'] = str(year) + str(quarter)
                if isSave is True:
                    df.to_csv(self.BASE_INFO_PATH +tableName + ".csv", encoding="utf8", mode='a')
                    # df.to_sql(tableName, self.engine_sql, if_exists='append',dtype=self.baseType[tableName])
                quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError, e:
                print e

    def getDebtpayingData(self, tableName = BASE_DEBTPAYINT_DATA):
        df = pd.read_csv(self.BASE_INFO_PATH +tableName + ".csv", index_col="code")
        # df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setCashflowData(self,year=None,quarter=None, number = 1,isSave = False,tableName = BASE_CASHFLOW_DATA):
        """获取制定年份指定季度的现金流量
                year :那一年
                quarter：那个季度
                number：后续几个季度的数据
                """
        [year,quarter] = getYearQuarter(year,quarter)
        for i in range(0, number):
            try:
                df = ts.get_cashflow_data(year,quarter)
                if df is None:
                    print 'get base cashflow info error'
                    return
                df['date'] = str(year) + str(quarter)
                if isSave is True:
                    df.to_csv(self.BASE_INFO_PATH +tableName + ".csv", encoding="utf8", mode='a')
                    # df.to_sql(tableName, self.engine_sql, if_exists='append',dtype=self.baseType[tableName])
                quarter = quarter - 1
                if quarter < 1:
                    quarter = 4
                    year = year - 1
            except IOError, e:
                print e

    def getCashflowData(self, tableName = BASE_CASHFLOW_DATA):
        df = pd.read_csv(self.BASE_INFO_PATH +tableName + ".csv", index_col="code")
        # df = pd.read_sql(tableName, self.engine_sql)
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

    def getOKStockCode(code):
        """
        判断一个股票代码是否为有效的，无效会补全为有效
        """
        code = str(code)
        for i in range(0, 6):
            if len(code) < 6:
                code = "0" + code
        return code


if __name__ == '__main__':
    baseeng = BaseInfo()
    baseeng.setStockBasics(isSave = True)
    # df = baseeng.setDebtpayingData(year= 2016,quarter = 4,number=16,isSave = True)






