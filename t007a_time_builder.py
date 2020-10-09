import time

import numpy as np

t_start = '2018-05-30 06:41:52.000',
t_end = '2018-05-31 18:18:18.000',

from LHCMeasurementTools.TimberManager import NXCalsFastQuery
db = NXCalsFastQuery(system='WINCCOA')

varfname = 'hlvarnames.txt'
with open(varfname, 'r') as fid:
    allvarlist = [vv.replace('\n', '') for vv in fid.readlines()]

# Select temperatures and heaters
allvarlist = [vv for vv in allvarlist if ('_TT8' in vv) or ('_EH8' in vv)]

import random

n_test_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
Dt_list = []
for nn in n_test_list:
    random.shuffle(allvarlist)
    varlst = allvarlist[:nn]
    tst = time.time()
    print(f'Start query, {len(varlst)} variables...')
    data = db.get(varlst,
            t1=t_start,
            t2=t_end)
    print('Done query')
    tdone = time.time()

    Dt = tdone - tst

    print(f'Elapsed {Dt}')

    Dt_list.append(Dt)

import scipy.io as sio
sio.savemat('time_build.mat', {
    'Dt': np.array(Dt_list),
    'n_variables': np.array(n_test_list)
    })
