import LHCMeasurementTools.LHC_FBCT as FBCT
import LHCMeasurementTools.LHC_BQM as BQM
import LHCMeasurementTools.LHC_BSRT as BSRT

import LHCMeasurementTools.LHC_Fills as Fills
from LHCMeasurementTools.LHC_Fill_LDB_Query import save_variables_and_json
from LHCMeasurementTools.LHC_Fill_LDB_Query import load_fill_dict_from_json

import json
import os

h5_folder = 'fill_bunchbybunch_data_h5s'
filepath =  h5_folder+'/bunchbybunch_data_fill'

if not os.path.isdir(h5_folder):
    os.mkdir(h5_folder)

fills_json_name = 'fills_and_bmodes.json'
dict_fill_bmodes = load_fill_dict_from_json(fills_json_name)

saved_json = h5_folder+'/saved_fills.json'

varlist = []
varlist += FBCT.variable_list()
varlist += BQM.variable_list()
varlist += BSRT.variable_list()

# Switch between cals and nxcals
import pytimber
db = pytimber.LoggingDB(source='nxcals')
#db = pytimber.LoggingDB(source='ldb')

scaled_query_config = {
    vv:{'scaleAlgorithm': 'REPEAT', 'scaleInterval': 'SECOND',
        'scaleSize': '10'}
        for vv in FBCT.variable_list() + BQM.variable_list()}

save_variables_and_json(varlist=varlist, file_path_prefix=filepath,
                          save_json=saved_json, fills_dict=dict_fill_bmodes,
                          db=db, scaled_query_config=scaled_query_config
                          )

