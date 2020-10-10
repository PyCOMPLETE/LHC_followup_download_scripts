import LHCMeasurementTools.LHC_Energy as Energy
import LHCMeasurementTools.LHC_BCT as BCT

import LHCMeasurementTools.LHC_Fills as Fills
from LHCMeasurementTools.LHC_Fill_LDB_Query import save_variables_and_json
from LHCMeasurementTools.LHC_Fill_LDB_Query import load_fill_dict_from_json
from LHCMeasurementTools.TimberManager import NXCalsFastQuery

import json
import os

h5_folder = 'fill_basic_data_h5s'
filepath =  h5_folder+'/basic_data_fill'

if not os.path.isdir(h5_folder):
    os.mkdir(h5_folder)

fills_json_name = 'fills_and_bmodes.json'
dict_fill_bmodes = load_fill_dict_from_json(fills_json_name)

saved_json = h5_folder+'/saved_fills.json'

varlist = []
varlist += Energy.variable_list()
varlist += BCT.variable_list()

# Switch between cals and nxcals
import pytimber
db = pytimber.LoggingDB(source='nxcals')
#db = pytimber.LoggingDB(source='ldb')

#from LHCMeasurementTools.TimberManager import NXCalsFastQuery
#db = NXCalsFastQuery(system='CMW')

save_variables_and_json(varlist=varlist, file_path_prefix=filepath,
                          save_json=saved_json, fills_dict=dict_fill_bmodes,
                          db=db, n_vars_per_extraction=1000)
