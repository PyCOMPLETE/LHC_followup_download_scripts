import time

import numpy as np

from pytimber.nxcals import NXCals
db = NXCals()

t1 = time.time()
print('Start query')
dfp = db.DataQuery.byVariables()\
   .system('WINCCOA')\
   .startTime('2018-05-30 06:41:52.000').endTime('2018-05-31 18:18:18.000')\
   .variableLike('QRLAA_13L5_QBS943%')\
   .variable('QRLAA_33L5_QBS947.POSST')\
   .build().sort("nxcals_variable_name","nxcals_timestamp")\
   .na().drop()\
   .select("nxcals_timestamp","nxcals_value", "nxcals_variable_name")

data1=np.fromiter( (tuple(dd.values()) for dd in dfp.collect()),dtype=[('ts',int),('val',float),('var','U32')] )
#data2=db.spark2numpy(dfp) #slower but individual arrays
#data3=db.spark2pandas(dfp) # slower but individual arrays
print('Done query')
t2 = time.time()
print(f'Dt = {t2-t1:.2f}s')

#pytimber-like output...
out={}
for var in set(data1['var']):
  sel=data1['var']==var
  out[var]=(data1['ts'][sel]/1e9,data1['val'][sel])
