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

#ldb = pytimber.LoggingDB(source='nxcals')
ldb = pytimber.LoggingDB()


dict_fill_info = {}
for period in periods:

    t_start_string = period.split('!')[0]
    t_stop_string = period.split('!')[1]

    t_start = th.localtime2unixstamp(t_start_string)
    t_stop = th.localtime2unixstamp(t_stop_string)


    # Get data from database
#    varlist = Fills.get_varlist()
#    data = tm.CalsVariables_from_pytimber(
#            ldb.get(varlist, t_start, t_stop))

    data_fnum = tm.CalsVariables_from_pytimber(
            ldb.get(['HX:FILLN'], t_start, t_stop))
    list_bmodes = ldb.getLHCFillsByTime(t_start, t_stop)

    # Make dictionary

    ##### I develop here
    filln_obj = Fills.fillnumber(data_fnum)
    dict_bmodes = {int(ff['fillNumber']): ff for ff in list_bmodes}
    fill_n_list = list(map(int, filln_obj.filln[filln_obj.filln > 0]))

    dict_fill_bmodes = {}
    for ii in range(len(fill_n_list)):
        filln = fill_n_list[ii]
        print('filln = %d'%filln)
        dict_fill_bmodes[filln] = {}

        t_startfill, t_endfill, flag_complete = filln_obj.fill_start_end(filln, t_stop)
        dict_fill_bmodes[filln]['t_startfill'] = t_startfill
        dict_fill_bmodes[filln]['t_endfill'] = t_endfill
        dict_fill_bmodes[filln]['flag_complete'] = flag_complete

        if filln in dict_bmodes.keys():
            for mm in dict_bmodes[filln]['beamModes']:
                bmode = mm['mode']
                dict_fill_bmodes[filln]['t_start_'+bmode] = mm['startTime']
                dict_fill_bmodes[filln]['t_stop_'+bmode] = mm['endTime']
        else:
            print(f'Warning! No beam mode info for fill {filln}')

    #####
    prrrr



    dict_fill_info.update(Fills.make_dict(data, t_stop))

# with open(pkl_name, 'wb') as fid:
#     pickle.dump(dict_fill_info, fid)

import json
with open(json_name, 'w') as fid:
    json.dump(dict_fill_info, fid)
