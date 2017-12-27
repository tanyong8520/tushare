# -*- coding: utf-8 -*-
import tushare as ts
from sqlalchemy import create_engine
from utilAll.Constants import *
from utilAll.FormatDate import *
import pandas as pd


class MacroeconomicInfo:
    engine_sql = create_engine(SQL_ENG_NAME)

    def setDepositRate(self,isSave = False,tableName = MACROECONOMIC_DEPOSIT_RATE):
        df = ts.get_deposit_rate()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getDepositRate(self,tableName = MACROECONOMIC_DEPOSIT_RATE):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setLoanRate(self,isSave = False,tableName = MACROECONOMIC_LOAN_RATE):
        df = ts.get_loan_rate()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getLoanRate(self,tableName = MACROECONOMIC_LOAN_RATE):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setRRR(self,isSave = False,tableName = MACROECONOMIC_RRR):
        df = ts.get_rrr()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getRRR(self,tableName = MACROECONOMIC_RRR):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setMoneySupply(self,isSave = False,tableName = MACROECONOMIC_MONEY_SUPPLY):
        df = ts.get_money_supply()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getMoneySupply(self,tableName = MACROECONOMIC_MONEY_SUPPLY):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setMoneySupplyBal(self,isSave = False,tableName = MACROECONOMIC_MONEY_SUPPLY_BAL):
        df = ts.get_money_supply_bal()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getMoneySupplyBal(self,tableName = MACROECONOMIC_MONEY_SUPPLY_BAL):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setGdpYear(self,isSave = False,tableName = MACROECONOMIC_GDP_YEAR):
        df = ts.get_gdp_year()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getGdpYear(self,tableName = MACROECONOMIC_GDP_YEAR):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setGdpQuarter(self,isSave = False,tableName = MACROECONOMIC_GDP_QUARTER):
        df = ts.get_gdp_quarter()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getGdpQuarter(self,tableName = MACROECONOMIC_GDP_QUARTER):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setGdpFor(self,isSave = False,tableName = MACROECONOMIC_GDP_FOR):
        df = ts.get_gdp_for()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getGdpFor(self,tableName = MACROECONOMIC_GDP_FOR):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setGdpPull(self,isSave = False,tableName = MACROECONOMIC_GDP_PULL):
        df = ts.get_gdp_pull()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getGdpPull(self,tableName = MACROECONOMIC_GDP_PULL):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setGdpContrib(self,isSave = False,tableName = MACROECONOMIC_GDP_CONTRIB):
        df = ts.get_gdp_contrib()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getGdpContrib(self,tableName = MACROECONOMIC_GDP_CONTRIB):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setCpi(self,isSave = False,tableName = MACROECONOMIC_CPI):
        df = ts.get_cpi()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getCpi(self,tableName = MACROECONOMIC_CPI):
        df = pd.read_sql(tableName, self.engine_sql)
        return df

    def setPpi(self,isSave = False,tableName = MACROECONOMIC_PPI):
        df = ts.get_cpi()
        if isSave is True:
            df.to_sql(tableName, self.engine_sql, if_exists='append')
        return df

    def getPpi(self,tableName = MACROECONOMIC_PPI):
        df = pd.read_sql(tableName, self.engine_sql)
        return df


    def getAllMacroeconomic(self):
        self.setDepositRate(isSave = True)
        self.setLoanRate(isSave = True)
        self.setRRR(isSave = True)
        self.setMoneySupply(isSave = True)
        self.setMoneySupplyBal(isSave = True)
        self.setGdpYear(isSave = True)
        self.setGdpQuarter(isSave = True)
        self.setGdpFor(isSave=True)
        self.setGdpPull(isSave = True)
        self.setGdpContrib(isSave = True)
        self.setCpi(isSave = True)
        self.setPpi(isSave = True)


if __name__ == '__main__':
    macroeconomicInfo = MacroeconomicInfo()
    df = macroeconomicInfo.setPpi(isSave = True)