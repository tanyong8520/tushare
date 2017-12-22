# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base.utils.BaseInfo as BaseInfo
from utilAll import *

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse(u"hellow work")

def getAllBaseInfo(request):
    baseInfo = BaseInfo()
    stockList = baseInfo.getStockList()
    for i in stockList:
        print i

