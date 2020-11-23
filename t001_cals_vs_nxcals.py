import time

import numpy as np

varfname = 'hlvarnames.txt'

t_fill_start = 1527662512.98
t_fill_end = 1527704298.4750001

with open(varfname, 'r') as fid:
    varlist = [vv.replace('\n', '') for vv in fid.readlines()]

# Switch between cals and nxcals
import pytimber
nxcals = pytimber.LoggingDB(source='nxcals')
cals = pytimber.LoggingDB(source='ldb')


for ivv, vv in enumerate(varlist):
    t_start_cals = time.time()
    data_cals = cals.get([vv], t_fill_start, t_fill_end)
    t_end_cals = time.time()
    dt_cals = t_end_cals - t_start_cals

    t_start_nxcals = time.time()
    data_nxcals = nxcals.get([vv], t_fill_start, t_fill_end)
    t_end_nxcals = time.time()
    dt_nxcals = t_end_nxcals - t_start_nxcals

    found_in_cals = vv in data_cals.keys()
    found_in_nxcals = vv in data_nxcals.keys()

    if not found_in_cals:
        dt_cals = -1

    if not found_in_nxcals:
        dt_nxcals = -1

    if found_in_cals and found_in_nxcals:
        same_n_entries = len(data_cals[vv][0]) == len(data_nxcals[vv][0])
    else:
        same_n_entries = False

    ## #For test
    ## data_cals[vv][0][10] += -0.2
    ## data_cals[vv][1][10] = data_cals[vv][1][10][:-1]

    if same_n_entries:
        if len(data_cals[vv][0]) == 0:
            max_tstamp_diff = 0
            max_value_diff = 0
        else:
            max_tstamp_diff = np.max(
                    np.abs(data_cals[vv][0] - data_nxcals[vv][0]))
            max_value_diff = 0
            for ii, (vv_cals0, vv_nxcals0) in enumerate(
                    zip(data_cals[vv][1], data_nxcals[vv][1])):
                vv_cals = np.atleast_1d(vv_cals0)
                vv_nxcals = np.atleast_1d(vv_nxcals0)
                same_n_values = len(vv_cals) == len(vv_nxcals)
                if same_n_values:
                    try:
                        max_curr = np.max(np.abs(vv_cals - vv_nxcals))
                    except Exception:
                        max_value_diff = -3
                        break
                    if max_curr > max_value_diff:
                        max_value_diff = max_curr
                else:
                    max_value_diff = -2
                    break

    else:
        max_tstamp_diff = -1
        max_value_diff = -1

    res = (f'{vv},{dt_cals},{dt_nxcals}, '
           f'{max_value_diff},{max_tstamp_diff}')
    print(f'{ivv}/{len(varlist)} - {res}') #, end='\r', flush=True)
    with open('testres.csv', 'a+') as fid:
        fid.write(res + '\n')
