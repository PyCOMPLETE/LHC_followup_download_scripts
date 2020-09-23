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

varlst = ['QBBI_A31L2_TT824.POSST',
 'QQBI_13L5_TT824.POSST',
 'QBBI_B13R4_TT826.POSST',
 'QBBI_A34L5_TT826.POSST']

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

