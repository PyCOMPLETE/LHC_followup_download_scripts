from LHCMeasurementTools.LHC_Fill_LDB_Query import save_variables_and_json
from LHCMeasurementTools.LHC_Fill_LDB_Query import load_fill_dict_from_json
import os

import LHCMeasurementTools.LHC_Heatloads as HL

h5_folder = 'fill_cell_by_cell_heatload_data_h5s'
filepath =  h5_folder+'/cell_by_cell_heatloads_fill'

if not os.path.isdir(h5_folder):
    os.mkdir(h5_folder)

fills_json_name = 'fills_and_bmodes.json'
dict_fill_bmodes = load_fill_dict_from_json(fills_json_name)

## HL.arcs_varnames_static has 412 variables, arc_cells_by_sector has 8*52=416
group_varlist = []
for kk in list(HL.arc_cells_by_sector.keys()):
    if kk=='MODEL':
        continue # Not available in in NXCALS
    group_varlist+=HL.arc_cells_by_sector[kk]

saved_json = h5_folder+'/saved_fills.json'

# Switch between cals and nxcals
#import pytimber
#db = pytimber.LoggingDB(source='nxcals')
#db = pytimber.LoggingDB(source='ldb')

from LHCMeasurementTools.TimberManager import NXCalsFastQuery
db = NXCalsFastQuery(system='WINCCOA')

save_variables_and_json(varlist=group_varlist, file_path_prefix=filepath,
                          save_json=saved_json, fills_dict=dict_fill_bmodes,
                          db=db, n_vars_per_extraction=1000)


