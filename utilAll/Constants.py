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