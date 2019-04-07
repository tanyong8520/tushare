# -*- coding: utf-8 -*-
import tushare as ts

from base.utils.BaseInfo import *
from sqlalchemy import create_engine

from transaction.models import Transaction
from utilAll.Constants import *
from utilAll.FormatDate import *
import os
import time
import pandas as pd

class TransactionInfo:
    engine_sql = create_engine(SQL_ENG_NAME)
    baseType = Transaction().baseType
    TRANSCATION_INFO_PATH = "E:/live/tushare/transaction/stockdatas/"
    stockBasicInfo = None
    baseInfo = None
    def __init__(self):
        self.baseInfo = BaseInfo()
        self.stockBasicInfo = self.baseInfo.getStockBasics()


    def getStockData(self, stock, start, end):
        """获取单个票指定时间范围内的数据,不会更新最新的数据"""
        # return getStockData2(stock,start,end)
        filepath = self.TRANSCATION_INFO_PATH + stock + ".csv"
        if os.path.exists(filepath):
            print("getDataFromDisk:", stock)
            hist_data = pd.read_csv(filepath, index_col="date")
        else:
            print("getDataFromNet:", stock, start, end)
            hist_data = ts.get_h_data(stock, start, end, autype='hfq')
            print("saveData:", stock)
            print(type(hist_data))
            if type(hist_data) == type(None):
                return None

            hist_data.to_csv(filepath)
        return hist_data

    def getStockData2(self, stock, start, end):
        """获取单个票的指定范围内的交易信息，如果最后时间不是最近交易日会补全数据"""
        filepath = self.TRANSCATION_INFO_PATH + stock + ".csv"
        if os.path.exists(filepath):
            print("getDataFromDisk:", stock)
            hist_data = pd.read_csv(filepath, index_col="date")
            hindex = hist_data.index
            print(max(hindex))
            premax = max(hindex)

            if premax == self.baseInfo.lastTradeDay:
                return hist_data

            preCloseP = hist_data.ix[premax]["close"]
            hist_data = hist_data.drop(premax)

            newdata = ts.get_h_data(stock, premax, self.baseInfo.lastTradeDay)
            newCloseP = newdata.ix[premax]["close"][0]
            # print(newdata.ix[premax])
            print("preclose:", preCloseP, "newclose:", newCloseP)
            if abs(preCloseP - newCloseP) > 0.1:
                # todo：两个相减是什么意思
                print("wrong price make new:", stock, start, end)
                hist_data = ts.get_h_data(stock, start, end)
                print("saveData:", stock)
                print(type(hist_data))
                if type(hist_data) == type(None):
                    return None

                hist_data.to_csv(filepath)
            else:
                print("ok price")
                newdata.to_csv(filepath)
                newdata = pd.read_csv(filepath, index_col="date")
                print(newdata)
                # todo：为什么要回写一次文件
                tdata = pd.concat([newdata, hist_data])

                # print(tdata)
                tdata.to_csv(filepath)
                hist_data = pd.read_csv(filepath, index_col="date")

        else:
            print("getDataFromNet:", stock, start, end)
            hist_data = ts.get_h_data(stock, start, end)
            print("saveData:", stock)
            print(type(hist_data))
            if type(hist_data) == type(None):
                return None

            hist_data.to_csv(filepath)
        return hist_data

    def fastUpdateData(self):
        """获取当天所有数据，如果当天不交易，获取最后交易日的所有数据"""
        lastTradeDay = self.baseInfo.lastTradeDay
        global todayData
        getDataSuccess = False
        sameDay = lastTradeDay == DateUtils.getToday()
        print("sameDay:", sameDay)
        while (not getDataSuccess):
            try:
                if sameDay:
                    todayData = ts.get_today_all()
                else:
                    todayData = ts.get_day_all(lastTradeDay)
                getDataSuccess = True
            except Exception as err:
                print("get_today_all fail retry later", err)
                time.sleep(5)

        print("get_today_all datasuccess")
        return todayData
        # fastUpdateStock("600652",0,0)

    def getTodayStockData(self, stock):
        """整理当天交易数据"""
        todayData = self.fastUpdateData()
        todayO = todayData[todayData.code == stock];
        # print(stock,todayO,todayO.size)
        if todayO.size <= 0:
            return None
        todayO = todayO.ix[todayO.index[0]]
        dfO = {}
        dfO["date"] = self.baseInfo.lastTradeDay
        # date,open,high,close,low,volume,amount
        dfO["open"] = todayO["open"]
        dfO["high"] = todayO["high"]
        if "trade" in todayO:
            dfO["close"] = todayO["trade"]
        if "price" in todayO:
            dfO["close"] = todayO["price"]

        dfO["low"] = todayO["low"]
        dfO["volume"] = todayO["volume"]
        dfO["amount"] = todayO["amount"]
        if "settlement" in todayO:
            dfO["prePrice"] = todayO["settlement"]
        if "preprice" in todayO:
            dfO["prePrice"] = todayO["preprice"]

        # dfO["Name"]=getLastTradeDay()
        # print(stock,dfO)

        return dfO

    def fastUpdateStock(self, stock, start, end):
        print("fast update:", stock, start, end)
        filepath = self.TRANSCATION_INFO_PATH + stock + ".csv"
        if os.path.exists(filepath):
            print("getDataFromDisk:", stock)
            hist_data = pd.read_csv(filepath, index_col="date")
            hindex = hist_data.index
            print(max(hindex))
            premax = max(hindex)
            preCloseP = hist_data.ix[premax]["close"]
            lastTradeDay = self.baseInfo.lastTradeDay
            last2TradeDay =  self.baseInfo.last2TradeDay
            print("pinfo:", premax, lastTradeDay, premax >= lastTradeDay)
            if premax >= lastTradeDay:
                return hist_data
            print(premax, last2TradeDay)
            dd = self.getTodayStockData(stock)
            if dd != None and dd["high"] == 0:
                print("not trade:", stock)
                return hist_data
            if premax == last2TradeDay:

                if dd == None or abs(dd["prePrice"] - preCloseP) > 0.1:
                    print("price not ok:")
                    pass
                else:
                    del dd["prePrice"]
                    tdff = pd.DataFrame(
                        [[dd["date"], dd["open"], dd["high"], dd["close"], dd["low"], dd["volume"], dd["amount"]]],
                        columns=["date", "open", "high", "close", "low", "volume", "amount"])
                    tdff = tdff.set_index("date")
                    hist_data = tdff.append(hist_data)
                    # print(hist_data)
                    print("fast success")
                    hist_data.to_csv(filepath)
                    return hist_data

            hist_data = hist_data.drop(premax)

            newdata = ts.get_h_data(stock, premax, lastTradeDay, pause=1)
            newCloseP = newdata.ix[premax]["close"][0]
            print("preclose:", preCloseP, "newclose:", newCloseP)
            if abs(preCloseP - newCloseP) > 0.1:
                print("wrong price make new:", stock, start, end)
                hist_data = ts.get_h_data(stock, start, end, pause=1)
                print("saveData:", stock)
                print(type(hist_data))
                if type(hist_data) == type(None):
                    return None
                hist_data.to_csv(filepath)
            else:
                newdata.to_csv(filepath)
                newdata = pd.read_csv(filepath, index_col="date")
                print(newdata)
                tdata = pd.concat([newdata, hist_data])
                tdata.to_csv(filepath)
                hist_data = pd.read_csv(filepath, index_col="date")

        else:
            print("getDataFromNet:", stock, start, end)
            hist_data = ts.get_h_data(stock, start, end)
            print("saveData:", stock)
            print(type(hist_data))
            if type(hist_data) == type(None):
                return None

            hist_data.to_csv(filepath)
        return hist_data

    def getAllInfo(self,startTime=None, endTime=None ,isSave = False,tableName=TRANSACTION_HIST_DATA):

        stockBasicsInfo = self.baseInfo.getStockBasics()
        for stockCodeItem in stockBasicsInfo.get("code"):
            print stockCodeItem
            df = ts.get_hist_data(code = stockCodeItem,start=startTime,endTime = endTime)
            if isSave is True:
                df.to_sql(tableName, self.engine_sql, if_exists='append')
        return

    def updateStockDataWork(self, stock, updating=False, fast=False):
        start = self.baseInfo.getStockBasics().ix[stock]['timeToMarket']
        end = self.baseInfo.lastTradeDay
        if fast == True:
            self.fastUpdateStock(stock, start, end)
            return

        if updating == False:
            self.getStockData(stock, start, end);
        else:
            self.getStockData2(stock, start, end);
        # getStockData(stock,start,end);

    def updateDataWorkLoop(self, reverse=False, fast=False):
        """跟新所有票的数据到文件中"""
        stocks = list(self.stockBasicInfo.index)
        if reverse:
            stocks.reverse()
        self.updateStocks(stocks, fast)

    def updateStocks(self, stocks, fast=False):
        """跟新传入的票的数据"""
        for stock in stocks:
            try:
                self.updateStockDataWork(stock, True, fast)
            except Exception as err:
                print(err)
                time.sleep(1)

    def fastUpdateData(self):
        """获取最后一天的信息"""
        getDataSuccess = False
        sameDay = self.getLastTradeDay() == self.getToday()
        print("sameDay:", sameDay)
        while (not getDataSuccess):
            try:
                #
                if sameDay:
                    todayData = ts.get_today_all()
                else:
                    todayData = ts.get_day_all(self.baseInfo.lastTradeDay)
                getDataSuccess = True
            except Exception as err:
                print("get_today_all fail retry later", err)
                time.sleep(5)
        return todayData

    def getToday(self):
        now = datetime.datetime.now()
        nowstr = now.strftime("%Y-%m-%d")
        return nowstr

    def getAllDetailsInfo(self,codeList = None, startTime=None, endTime=None, isSave=False, tableName=TRANSACTION_HIST_DETAILS_DATA):
        if codeList is None:
            return None
        for codeItem in codeList:
            try:
                df = self.getOneDetailsInfo(codeItem,startTime,endTime)
                if isSave is True:
                    df.to_sql(tableName+'_'+codeItem, self.engine_sql, if_exists='append')
            except Exception,e:
                print "get %s details info error:%s"%(codeItem,e.message)
        return df

    def getTodayAll(self):
        return ts.get_today_all()

    def getTodayAll(self,isSave=False,tableName=TRANSACTION_ALL_DATA_TEST):
        while True:
            try:
                df = ts.get_today_all()
                date = getNowdate()
                df2 = df.loc[:,['code','open','high','close','low','volume','amount']]
                df2['date']=date
                print df2
                if isSave is True:
                    df2.to_sql(tableName, self.engine_sql, if_exists='append', dtype=self.baseType[tableName])
                return df2
            except Exception, e:
                print "get all details info error,%s"%e.message
                print e
                time.sleep(180)

    def getAllDate(self,start=None,end=None,isSave=False,tableName=TRANSACTION_ALL_DATA):
        if end is None:
            end = '2018-01-09'#getYseterDay()
        trans_info = pd.read_sql_query('select count(*) ,code from `transaction_all_data` group by code',
                                       self.engine_sql)

        baseInfo = BaseInfo()
        stockBasicsInfo = pd.read_sql_query('select timeToMarket ,code from `base_stockbasics`',
                                            baseInfo.engine_sql)
        stocklist = stockBasicsInfo[(-stockBasicsInfo['code'].isin(trans_info['code']))]
        print 'download count:%d, hive count:%d'%(stockBasicsInfo.count()['code'],trans_info.count()['code'])

        for index,row in stocklist.iterrows():
            print
            while True:
                try:
                    codeString = stocklist.loc[index]['code']
                    print "code:%s,startTime:%s"%(codeString,row['timeToMarket'])
                    if start is None:
                        if row['timeToMarket'] is pd.NaT :
                            print "code:%s,startTime is None" % (codeString)
                            break
                        startdate = row['timeToMarket'].to_pydatetime().strftime('%Y-%m-%d')

                        if startdate < '2005-01-01':
                            startdate = '2005-01-01'
                        print "code:%s,startTime:%s" % (codeString, startdate)
                        df = ts.get_h_data(codeString, start=startdate, end=end)
                    else:
                        print "code:%s,startTime:%s" % (codeString, start)
                        df = ts.get_h_data(codeString, start=start, end=end)

                    if df is None:
                        print 'get hist data error:%s,starttime:%s'%(index,row['timeToMarket'])
                    if isSave is True:
                        df['code'] = codeString
                        df.to_sql(tableName, self.engine_sql, if_exists='append',dtype = self.baseType[tableName])
                        print 'get code:%s'%(codeString)
                    time.sleep(120)
                    break
                except Exception,e:
                    print "get %s details info error"%(row['code'])
                    print e
                    time.sleep(180)


    def test(self):
        stockBasicsInfo = pd.DataFrame(columns=('time', 'code'))
        stockBasicsInfo.loc[0] = ['1', '10']
        stockBasicsInfo.loc[1] = ['1', '000517']
        stockBasicsInfo.loc[2] = ['1', '12']
        stockBasicsInfo.loc[3] = ['1', '000631']
        stockBasicsInfo.loc[4] = ['1', '14']
        print stockBasicsInfo.count()
        print stockBasicsInfo
        print 'drop'
        df = stockBasicsInfo.where(-stockBasicsInfo.isin(['10', '14']))
        print df

        print 'drop2'
        print stockBasicsInfo
        df2 = stockBasicsInfo[(-stockBasicsInfo['code'].isin(['000517', '10']))]
        print df2.count()['code']
        print df2

        transactionInfo = TransactionInfo()
        trans_info = pd.read_sql_query('select count(*) ,code from `transaction_all_data` group by code',
                                       transactionInfo.engine_sql)

        print trans_info.count()['code']
        baseInfo = BaseInfo()
        stockBasicsInfo = pd.read_sql_query('select timeToMarket ,code from `base_stockbasics` group by code',
                                            baseInfo.engine_sql)
        print stockBasicsInfo.count()['code']
        stocklist = stockBasicsInfo[(-stockBasicsInfo['code'].isin(trans_info['code']))]
        print stocklist.count()['code']


if __name__ == '__main__':
    # 获取最后一天的数据
    stockData = TransactionInfo().getStockData("000001","2018-01-01", "2019-01-01")
    nearData = stockData["2018-01-01": "2019-01-01"]
    print len(nearData)
    print nearData.tail(10)
    print nearData.head(10)

    print nearData['close'].describe()

    # 循环跟新说有票的数据
    # TransactionInfo().updateDataWorkLoop()
    # 获取单个票的所有数据
    # TransactionInfo().updateStockDataWork('100000')

    # TransactionInfo().getTodayAll(isSave=True);
