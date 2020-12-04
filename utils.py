
import re
import time,datetime
import logging
import sys
import math

# 配置
MPRINT_MAX_COL_SIZE = 200
# 时间字符串转timestamp
def str2timestamp(timestr, format = "%Y-%m-%d %H:%M:%S"): 
    timeArray = time.strptime(timestr, format) 
    return int(time.mktime(timeArray))

# timestamp 转时间字符串
def timestamp2str(ts, format = "%Y-%m-%d %H:%M:%S"):
    return time.strftime(format,time.localtime(ts))
ts2str = timestamp2str