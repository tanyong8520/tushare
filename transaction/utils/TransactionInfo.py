import tushare as ts
from _mysql_exceptions import OperationalError

from base.utils.BaseInfo import *
from sqlalchemy import create_engine
from utilAll.Constants import *
from utilAll.FormatDate import *
import time
import pandas as pd

class TransactionInfo:
    engine_sql = create_engine(SQL_ENG_NAME)

    def getOneInfo(self, code ,startTime, endTime):
        if code is None:
            return
        if startTime is None:
            startTime = getNowdate()
        if endTime is None:
            endTime = getNowdate()
        return ts.get_hist_data(code,ktype='D',start=startTime, end=endTime)

    def getOneDetailsInfo(self, code=None, startTime=None, endTime=None):
        if code is None:
            return
        if startTime is None:
            startTime = getNowdate()
        if endTime is None:
            endTime = getNowdate()
        return ts.get_hist_data(code, ktype='60', start=startTime, end=endTime)

    def getAllInfo(self,startTime=None, endTime=None ,isSave = False,tableName=TRANSACTION_HIST_DATA):
        baseInfo = BaseInfo()
        stockBasicsInfo = baseInfo.getStockBasics()
        for stockCodeItem in stockBasicsInfo.get("code"):
            print stockCodeItem
            df = ts.get_hist_data(code = stockCodeItem,start=startTime,endTime = endTime)
            if isSave is True:
                df.to_sql(tableName, self.engine_sql, if_exists='append')
        return

    def getAllDetailsInfo(self,codeList = None, startTime=None, endTime=None, isSave=False, tableName=TRANSACTION_HIST_DETAILS_DATA):
        if codeList is None:
            return None
        for codeItem in codeList:
            try:
                df = self.getOneDetailsInfo(codeItem,startTime,endTime)
                if isSave is True:
                    df.to_sql(tableName+'_'+codeItem, self.engine_sql, if_exists='append')
            except OperationalError,e:
                df.to_sql(tableName + '_' + codeItem, self.engine_sql, if_exists='append')
            except Exception,e:
                print "get %s details info error:%s"%(codeItem,e.message)
        return df

    def getTodayAll(self):
        return ts.get_today_all()

    def getAllDate(self,start=None,end=None,isSave=False,tableName=TRANSACTION_ALL_DATA):
        baseInfo = BaseInfo()
        stockBasicsInfo = baseInfo.getStockBasics().loc[:,['timeToMarket']]

        for index,row in stockBasicsInfo.iterrows():
            print index
            print "test!!!!!!!"
            print row['timeToMarket'].__class__

            try:
                if start is None:
                    a = time.strftime('YYYY-mm-dd',row['timeToMarket'])
                    df = ts.get_h_data(index, start=row['timeToMarket'], end=end)
                else:
                    df = ts.get_h_data(index, start=start, end=end)

                if df is None:
                    print 'get hist data error:%s,starttime:%s'%(index,row['timeToMarket'])
                if isSave is True:
                    df.to_sql(tableName, self.engine_sql, if_exists='append')
            except Exception,e:
                print "get %s details info error:%s"%(index, e.message)

    def test(self):
        baseInfo = BaseInfo()
        stockBasicsInfo = baseInfo.getStockBasics().loc[:, ['code', 'timeToMarket']]
        for index,row in stockBasicsInfo.iterrows():

            print row['code'], row['timeToMarket']
            # for col_name in stockBasicsInfo.columns:
            #     print 'get date'
            #     print row[col_name]


if __name__ == '__main__':

    transactionInfo = TransactionInfo()
    print TransactionInfo().getAllDate(isSave=True);