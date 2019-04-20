# -*- coding:utf-8 -*-

from datetime import datetime
import numpy as np
import pandas as pd

'''

Converting between datetime.datetime、numpy.datetime64 and pandas.tslib.Timestamp

'''

# dt = datetime.datetime(2018, 9, 18)
dt = datetime.now()
# ts = pd.DatetimeIndex([dt])[0]
ts=pd.Timestamp(dt)
dt64 = np.datetime64(dt)

# datetime.datetime type:
print dt
print type(dt)

# Timestamp type:
print ts
print type(ts)

# numpy.datetime64 type:
print dt64
print type(dt64)

# extract datetime.datetime from Timestamp type:
print ts.to_pydatetime()
print type(ts.to_pydatetime())

# extract datetime.datetime from numpy.datetime64 type:
print pd.Timestamp(dt64).to_pydatetime()
print type(pd.Timestamp(dt64).to_pydatetime())

# extract Timestamp from numpy.datetime64 type:
print pd.Timestamp(dt64)
print type(pd.Timestamp(dt64))

# extract numpy.datetime64 from Timestamp type:
print np.datetime64(ts)
print type(np.datetime64(ts))






