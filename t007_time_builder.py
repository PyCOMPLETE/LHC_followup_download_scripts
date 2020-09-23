import time

import numpy as np

from pytimber.nxcals import NXCals

class NXCalsFastQuery(NXCals):

    def get(self, variables, t1, t2, system):
        '''
            system should be either 'CMW' or 'WINCCOA'
        '''
        query = self.DataQuery.byVariables()\
            .system(system)\
            .startTime(t1)\
            .endTime(t2)

        for vv in variables:
            query = query.variable(vv)

        dfp = query.build()\
                .sort("nxcals_variable_name","nxcals_timestamp")\
                .na().drop()\
                .select("nxcals_timestamp",
                        "nxcals_value", "nxcals_variable_name")

        data1=np.fromiter(
                (tuple(dd.values()) for dd in dfp.collect()),
                dtype=[('ts',int),('val',float),('var','U32')] )

        out={}
        for var in set(data1['var']):
          sel=data1['var']==var
          out[var]=(data1['ts'][sel]/1e9,data1['val'][sel])

        return out

db = NXCalsFastQuery()

varfname = 'hlvarnames.txt'
with open(varfname, 'r') as fid:
    allvarlist = [vv.replace('\n', '') for vv in fid.readlines()]

# Select temperatures and heaters
allvarlist = [vv for vv in allvarlist if ('_TT8' in vv) or ('_EH8' in vv)]

import random

n_test_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
Dt_list = []
for nn in n_test_list:
    random.shuffle(allvarlist)
    varlst = allvarlist[:nn]
    tst = time.time()
    print(f'Start query, {len(varlst)} variables...')
    data = db.get(varlst,
            t1='2018-05-30 06:41:52.000',
            t2='2018-05-31 18:18:18.000',
            system='WINCCOA')
    print('Done query')
    tdone = time.time()

    Dt = tdone - tst

    print(f'Elapsed {Dt}')

    Dt_list.append(Dt)

