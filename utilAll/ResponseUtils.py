import json
import datetime
from django.http import HttpResponse

def MakeResponse(modeList):
    obj_arr = []
    for o in modeList:
        obj_arr.append(o.toDict())
    print obj_arr
    return HttpResponse(json.dumps(obj_arr, sort_keys=True, cls=CJsonEncoder), content_type="application/json")


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)