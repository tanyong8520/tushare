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

    TransactionInfo().getTodayAll(isSave=True);
