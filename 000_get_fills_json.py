import pickle

import pytimber

#import LHCMeasurementTools.lhc_log_db_query as lldb
import LHCMeasurementTools.TimestampHelpers as th
import LHCMeasurementTools.TimberManager as tm
import LHCMeasurementTools.LHC_Fills as Fills


periods = [
'2018_05_28 00:00:00!2018_05_31 00:00:00',
#'2018_07_23 12:00:00!2018_07_24 20:00:00', #MD3295/MD3300
#'2018_09_12 12:00:00!2018_09_15 00:00:00', #MD3298/MD3300
#'2018_10_25 12:00:00!2018_10_27 12:00:00', #MD4203/MD2484
#'2018_07_22 16:00:00!2018_07_23 16:00:00', #
#'2018_06_13 00:00:00!2018_06_15 00:00:00', #MD3297/MD3296/MD3300
#'2017_09_25 16:00:00!2017_09_26 16:00:00', #
]

#pkl_name = 'fills_and_bmodes.pkl'
json_name = 'fills_and_bmodes.json'

ldb = pytimber.LoggingDB(source='nxcals')
#ldb = pytimber.LoggingDB()


dict_fill_info = {}
for period in periods:

    t_start_string = period.split('!')[0]
    t_stop_string = period.split('!')[1]

    t_start = th.localtime2unixstamp(t_start_string)
    t_stop = th.localtime2unixstamp(t_stop_string)


    # Get data from database
    data_fnum = tm.CalsVariables_from_pytimber(
            ldb.get(['HX:FILLN'], t_start, t_stop))
    list_bmodes = ldb.getLHCFillsByTime(t_start, t_stop)

    # Generate dictionary
    dict_fill_info.update(Fills.make_fill_info_dict(
                            data_fnum, list_bmodes, t_stop))

# with open(pkl_name, 'wb') as fid:
#     pickle.dump(dict_fill_info, fid)

import json
with open(json_name, 'w') as fid:
    json.dump(dict_fill_info, fid)
