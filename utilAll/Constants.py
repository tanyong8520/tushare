# -*- coding: utf-8 -*-

SQL_ENG_NAME = 'mysql://root:root@127.0.0.1/live?charset=utf8'

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
