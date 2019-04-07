# -*- coding: utf-8 -*-

SQL_ENG_NAME = 'postgresql://root:root@127.0.0.1/live?charset=utf8'

# 交易数据
# 所有的数据复权数据
TRANSACTION_ALL_DATA = 'transaction_all_data'
TRANSACTION_ALL_DATA_TEST = 'transaction_all_data_TEST'
#历史数据
TRANSACTION_HIST_DATA = 'transaction_hist_data'
# 历史详情数据。5分钟间隔
TRANSACTION_HIST_DETAILS_DATA = 'transaction_hist_details_data'


# base table
# 基础信息
BASE_STOCK_BASICS = 'base_stockbasics'
# 业绩报告
BASE_REPORT_DATA = 'base_reportdata'
# 盈利能力
BASE_PROFIT_DATA = 'base_profitdata'
# 营运能力
BASE_OPERATION_DATA = 'base_operationdata'
# 成长能力
BASE_GROWTH_DATA = 'base_growthdata'
# 偿债能力
BASE_DEBTPAYINT_DATA = 'base_debtpayingdata'
# 现金流量
BASE_CASHFLOW_DATA = 'base_cashflowdata'

# 参考数据
# 分配预案
REFERENCE_PROFIT_DATA = 'reference_profitdata'
# 业绩预告
REFERENCE_FORECAST_DATA = 'reference_forecastdata'
# 限售股解禁
REFERENCE_XSG_DATA = 'reference_xsgdata'
# 基金持股
REFERENCE_HUND_HOLDINGS = 'reference_fundholdings'
# 新股数据
REFERENCE_NEW_STOCKS= 'reference_newstocks'
# 融资融券（沪市）
REFERENCE_SH_MARGINS= 'reference_shmargins'
# 融资融券明细数据（沪市）
REFERENCE_SH_MARGINS_DETAILS= 'reference_shmargindetails'

# 分类数据
# 行业分类
CLASSIFIED_INDUSTRY = 'classified_industry'
# 概念分类
CLASSIFIED_CONCEPT = 'classified_concept'
# 地域分类
CLASSIFIED_AREA = 'classified_area'
# 中小板分类
CLASSIFIED_SME = 'classified_sme'
# 创业板分类
CLASSIFIED_GME = 'classified_gme'
# 风险警示板分类
CLASSIFIED_ST = 'classified_st'
# 沪深300成份及权重
CLASSIFIED_HS300S = 'classified_hs300s'
# 上证50成份股
CLASSIFIED_SZ50S = 'classified_sz50s'
# 中证500成份股
CLASSIFIED_ZZ500S = 'classified_zz500s'
# 终止上市股票列表
CLASSIFIED_TERMINATED = 'classified_terminated'
# 暂停上市股票列表
CLASSIFIED_SUSPENDED = 'classified_suspended'

# 宏观经济
# 存款利率
MACROECONOMIC_DEPOSIT_RATE = 'macroeconomic_deposit_rate'\
# 贷款利率
MACROECONOMIC_LOAN_RATE = 'macroeconomic_loan_rate'
# 存款准备金率
MACROECONOMIC_RRR = 'macroeconomic_rrr'
# 货币供应量
MACROECONOMIC_MONEY_SUPPLY = 'macroeconomic_money_supply'
# 货币供应量(年底余额)
MACROECONOMIC_MONEY_SUPPLY_BAL = 'macroeconomic_money_supply_bal'
# 国内生产总值(年度)
MACROECONOMIC_GDP_YEAR = 'macroeconomic_gdp_year'
# 国内生产总值(季度)
MACROECONOMIC_GDP_QUARTER = 'macroeconomic_gdp_quarter'
# 三大需求对GDP贡献
MACROECONOMIC_GDP_FOR = 'macroeconomic_gdp_for'
# 三大产业对GDP拉动
MACROECONOMIC_GDP_PULL = 'macroeconomic_gdp_pull'
# 三大产业贡献率
MACROECONOMIC_GDP_CONTRIB = 'macroeconomic_gdp_contrib'
# 居民消费价格指数
MACROECONOMIC_CPI = 'macroeconomic_cpi'
# 工业品出厂价格指数
MACROECONOMIC_PPI = 'macroeconomic_ppi'

# 银行间同业拆放利率
# Shibor拆放利率
CALLLOANS_SHIBOR_DATA = 'callloansInfo_shibor_data'
# 银行报价数据
CALLLOANS_SHIBOR_QUOTE_DATA = 'callloansInfo_shibor_quote_data'
# Shibor均值数据
CALLLOANS_MA_DATA = 'callloansInfo_shibor_ma_data'
# 贷款基础利率
CALLLOANS_LPR_DATA = 'callloansInfo_lpr_data'
# 贷款基础利率均值
CALLLOANS_LPR_MA_DATA = 'callloansInfo_lpr_ma_data'
