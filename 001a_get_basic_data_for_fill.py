import LHCMeasurementTools.LHC_Energy as Energy
import LHCMeasurementTools.LHC_BCT as BCT

import LHCMeasurementTools.LHC_Fills as Fills
from LHCMeasurementTools.LHC_Fill_LDB_Query import save_variables_and_pickle

import pickle
import os

h5_folder = 'fill_basic_data_h5s'
filepath =  h5_folder+'/basic_data_fill'

if not os.path.isdir(h5_folder):
    os.mkdir(h5_folder)

fills_pkl_name = 'fills_and_bmodes.pkl'
with open(fills_pkl_name, 'rb') as fid:
    dict_fill_bmodes = pickle.load(fid)

saved_pkl = h5_folder+'/saved_fills.pkl'

varlist = []
varlist += Energy.variable_list()
varlist += BCT.variable_list()

save_variables_and_pickle(varlist=varlist, file_path_prefix=filepath,
                          save_pkl=saved_pkl, fills_dict=dict_fill_bmodes)
