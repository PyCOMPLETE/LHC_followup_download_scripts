import LHCMeasurementTools.LHC_Energy as Energy
import LHCMeasurementTools.LHC_BCT as BCT

import LHCMeasurementTools.LHC_Fills as Fills
from LHCMeasurementTools.LHC_Fill_LDB_Query import save_variables_and_pickle

import json
import os

h5_folder = 'fill_basic_data_h5s'
filepath =  h5_folder+'/basic_data_fill'

if not os.path.isdir(h5_folder):
    os.mkdir(h5_folder)

fills_json_name = 'fills_and_bmodes.json'
with open(fills_json_name, 'r') as fid:
    ddd = json.load(fid)
    dict_fill_bmodes = {int(kk): ddd[kk] for kk in ddd.keys()}

saved_pkl = h5_folder+'/saved_fills.pkl'

varlist = []
varlist += Energy.variable_list()
varlist += BCT.variable_list()

# Switch between cals and nxcals
import pytimber
#db = pytimber.LoggingDB(source='nxcals')
db = pytimber.LoggingDB(source='ldb')


save_variables_and_pickle(varlist=varlist, file_path_prefix=filepath,
                          save_pkl=saved_pkl, fills_dict=dict_fill_bmodes,
                          db=db)
