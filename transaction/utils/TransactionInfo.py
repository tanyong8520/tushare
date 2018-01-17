# -*- coding: utf-8 -*-
import tushare as ts
from _mysql_exceptions import OperationalError

from base.utils.BaseInfo import *
from sqlalchemy import create_engine

from transaction.models import Transaction
from utilAll.Constants import *
from utilAll.FormatDate import *
import time
import pandas as pd

class TransactionInfo:
    engine_sql = create_engine(SQL_ENG_NAME)
    baseType = Transaction().baseType

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
            endTime = getYseterDay()
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
        if end is None:
            end = '2018-1-9'#getYseterDay()

        baseInfo = BaseInfo()
        stockBasicsInfo = baseInfo.getStockBasics().loc[:,['timeToMarket']]

        for index,row in stockBasicsInfo.iterrows():
            print
            while True:
                try:
                    if start is None:
                        startdate = row['timeToMarket'].to_pydatetime().strftime('%Y-%m-%d')
                        df = ts.get_h_data(index.encode('UTF-8'), start=startdate, end=end)
                    else:
                        index_utf = index.encode('UTF-8')
                        df = ts.get_h_data(index_utf, start=start, end=end)

                    if df is None:
                        print 'get hist data error:%s,starttime:%s'%(index,row['timeToMarket'])
                    if isSave is True:
                        df['code'] = index.encode('UTF-8')
                        df.to_sql(tableName, self.engine_sql, if_exists='append',dtype = self.baseType[tableName])
                    time.sleep(180)
                    break
                except Exception,e:
                    print "get %s details info error"%(index)
                    print e
                    time.sleep(180)

    def test(self):
        pass



if __name__ == '__main__':
    # transactionInfo = TransactionInfo()
    # trans_info =  pd.read_sql_query('select count(*) ,code from `transaction_all_data` group by code',transactionInfo.engine_sql)
    # baseInfo = BaseInfo()
    # print trans_info
    # stockBasicsInfo = baseInfo.getStockBasics().loc[:,['timeToMarket','code']]
    stockBasicsInfo = pd.DataFrame(columns=('time', 'code'))
    stockBasicsInfo.loc[0] = ['1', '10']
    stockBasicsInfo.loc[1] = ['1', '000517']
    stockBasicsInfo.loc[2] = ['1', '12']
    stockBasicsInfo.loc[3] = ['1', '000631']
    stockBasicsInfo.loc[4] = ['1', '14']
    print stockBasicsInfo.count()
    print stockBasicsInfo
    print 'drop'
    df =  stockBasicsInfo.where(-stockBasicsInfo.isin(['10','14']))
    print df

    print 'drop2'
    print stockBasicsInfo
    df2 = stockBasicsInfo[(-stockBasicsInfo['code'].isin(['000517','10']))]
    print df2.count()['code']
    print df2

    print 'drop3'

    # for index, row in isDowned.iterrows():
    #     if row['code'] is True:
    #         stockBasicsInfo.drop(index)

    # print TransactionInfo().getAllDate(isSave=True);