from LHCMeasurementTools.LHC_Fill_LDB_Query import save_variables_and_pickle
import pickle
import os

import LHCMeasurementTools.LHC_Heatloads as HL

h5_folder = 'fill_heatload_data_h5s'

if not os.path.isdir(h5_folder):
    os.mkdir(h5_folder)

fills_pkl_name = 'fills_and_bmodes.pkl'
with open(fills_pkl_name, 'rb') as fid:
    dict_fill_bmodes = pickle.load(fid)


group_varlist = [] 

for kk in list(HL.variable_lists_heatloads.keys()):
	group_varlist+=HL.variable_lists_heatloads[kk]


saved_pkl = h5_folder+'/saved_fills.pkl'
filepath =  h5_folder+'/heatloads_fill'


save_variables_and_pickle(varlist=group_varlist, file_path_prefix=filepath, 
                          save_pkl=saved_pkl, fills_dict=dict_fill_bmodes)
    

