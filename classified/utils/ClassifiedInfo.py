# -*- coding: utf-8 -*-
import tushare as ts
from sqlalchemy import create_engine
from utilAll.Constants import *
from utilAll.FormatDate import *
import pandas as pd

class ClassifiedInfo:
    engine_sql = create_engine(SQL_ENG_NAME)

    def setIndustryClassified(self, isSave=False, tableName=CLASSIFIED_INDUSTRY):
        df = ts.get_industry_classified()
        if isSave is True:
            df.to_sql(tableName,self.engine_sql, if_exists='append')
        return df

    def getIndustryClassified(self, tableName=CLASSIFIED_INDUSTRY):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setConceptClassified(self, isSave=False, tableName=CLASSIFIED_CONCEPT):
        df = ts.get_concept_classified()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getConceptClassified(self, tableName=CLASSIFIED_CONCEPT):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setAreaClassified(self, isSave=False, tableName=CLASSIFIED_AREA):
        df = ts.get_area_classified()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getAreaClassified(self, tableName=CLASSIFIED_AREA):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setSmeClassified(self, isSave=False, tableName=CLASSIFIED_SME):
        df = ts.get_sme_classified()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getSmeClassified(self, tableName=CLASSIFIED_SME):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setGmeClassified(self, isSave=False, tableName=CLASSIFIED_GME):
        df = ts.get_gem_classified()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getGmeClassified(self, tableName=CLASSIFIED_GME):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setStClassified(self, isSave=False, tableName=CLASSIFIED_ST):
        df = ts.get_st_classified()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getStClassified(self, tableName=CLASSIFIED_ST):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setHs300sClassified(self, isSave=False, tableName=CLASSIFIED_HS300S):
        df = ts.get_hs300s()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getHs300sClassified(self, tableName=CLASSIFIED_HS300S):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setSz50sClassified(self, isSave=False, tableName=CLASSIFIED_SZ50S):
        df = ts.get_sz50s()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getSz50sClassified(self, tableName=CLASSIFIED_SZ50S):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setZz500sClassified(self, isSave=False, tableName=CLASSIFIED_ZZ500S):
        df = ts.get_zz500s()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getZz500sClassified(self, tableName=CLASSIFIED_ZZ500S):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setTerminatedClassified(self, isSave=False, tableName=CLASSIFIED_TERMINATED):
        df = ts.get_terminated()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getTerminatedClassified(self, tableName=CLASSIFIED_TERMINATED):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setSuspendedClassified(self, isSave=False, tableName=CLASSIFIED_SUSPENDED):
        df = ts.get_suspended()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getSuspendedClassified(self, tableName=CLASSIFIED_SUSPENDED):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def getAllClassified(self):
        self.setIndustryClassified(isSave = True)
        self.setConceptClassified(isSave = True)
        self.setAreaClassified(isSave = True)
        self.setSmeClassified(isSave = True)
        self.setGmeClassified(isSave = True)
        self.setStClassified(isSave = True)
        self.setTerminatedClassified(isSave = True)
        self.setSuspendedClassified(isSave = True)
        # 无法调用
        self.setHs300sClassified(isSave = True)
        self.setSz50sClassified(isSave = True)
        self.setZz500sClassified(isSave = True)


if __name__ == '__main__':
    classifiedInfo = ClassifiedInfo()
    df = classifiedInfo.setZz500sClassified(isSave = True)