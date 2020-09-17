import LHCMeasurementTools.TimberManager as tm
data_folder_fill = './'
filln = 6741

varlist = []

data = tm.CalsVariables_from_h5(
        data_folder_fill+'/fill_basic_data_h5s/basic_data_fill_%d.h5'%filln)
varlist += data.keys()

data = tm.CalsVariables_from_h5(
        data_folder_fill+'/fill_bunchbybunch_data_h5s/bunchbybunch_data_fill_%d.h5'%filln)
varlist += data.keys()

data = tm.CalsVariables_from_h5(
        data_folder_fill+'/fill_heatload_data_h5s/heatloads_fill_%d.h5'%filln)
varlist += data.keys()

data = tm.CalsVariables_from_h5(
        data_folder_fill+'/fill_extra_data_h5s/extra_data_fill_%d.h5'%filln)
varlist += data.keys()

import LHCMeasurementTools.LHC_Fills as Fills
varlist += Fills.get_varlist()

# Variables for heat load recalculation
varfiles = [
        '../tools/GasFlowHLCalculator/variable_list_complete.txt',
        '../tools/GasFlowHLCalculator/variable_list_special.txt'
        ]

for vf in varfiles:
    with open(vf, 'r') as f:
        varlist += f.read().splitlines()[0].split(',')



