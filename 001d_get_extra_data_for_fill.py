import LHCMeasurementTools.LHC_Fills as Fills
from LHCMeasurementTools.LHC_Fill_LDB_Query import save_variables_and_json
from LHCMeasurementTools.LHC_Fill_LDB_Query import load_fill_dict_from_json

import json
import os

h5_folder = 'fill_extra_data_h5s'
filepath =  h5_folder+'/extra_data_fill'

if not os.path.isdir(h5_folder):
    os.mkdir(h5_folder)

fills_json_name = 'fills_and_bmodes.json'
dict_fill_bmodes = load_fill_dict_from_json(fills_json_name)

saved_json = h5_folder+'/saved_fills.json'

varlist = [
'LHC.BOFSU:TUNE_B1_H',
'LHC.BOFSU:TUNE_B1_V',
'LHC.BOFSU:TUNE_B2_H',
'LHC.BOFSU:TUNE_B2_V',
'LHC.BOFSU:TUNE_TRIM_B1_H',
'LHC.BOFSU:TUNE_TRIM_B1_V',
'LHC.BOFSU:TUNE_TRIM_B2_H',
'LHC.BOFSU:TUNE_TRIM_B2_V',
'LHC.BQBBQ.CONTINUOUS.B1:EIGEN_AMPL_1',
'LHC.BQBBQ.CONTINUOUS.B1:EIGEN_AMPL_2',
'LHC.BQBBQ.CONTINUOUS.B1:EIGEN_FREQ_1',
'LHC.BQBBQ.CONTINUOUS.B1:EIGEN_FREQ_2',
'LHC.BQBBQ.CONTINUOUS.B2:EIGEN_AMPL_1',
'LHC.BQBBQ.CONTINUOUS.B2:EIGEN_AMPL_2',
'LHC.BQBBQ.CONTINUOUS.B2:EIGEN_FREQ_1',
'LHC.BQBBQ.CONTINUOUS.B2:EIGEN_FREQ_2',
'LHC.BQBBQ.CONTINUOUS_HS.B1:EIGEN_AMPL_1',
'LHC.BQBBQ.CONTINUOUS_HS.B1:EIGEN_AMPL_2',
'LHC.BQBBQ.CONTINUOUS_HS.B1:EIGEN_FREQ_1',
'LHC.BQBBQ.CONTINUOUS_HS.B1:EIGEN_FREQ_2',
'LHC.BQBBQ.CONTINUOUS_HS.B2:EIGEN_AMPL_1',
'LHC.BQBBQ.CONTINUOUS_HS.B2:EIGEN_AMPL_2',
'LHC.BQBBQ.CONTINUOUS_HS.B2:EIGEN_FREQ_1',
'LHC.BQBBQ.CONTINUOUS_HS.B2:EIGEN_FREQ_2',
'ALICE:LUMI_TOT_INST',
'ATLAS:LUMI_TOT_INST',
'CMS:LUMI_TOT_INST',
'LHCB:LUMI_TOT_INST',
'HX:BETASTAR_IP1',
'HX:BETASTAR_IP2',
'HX:BETASTAR_IP5',
'HX:BETASTAR_IP8',
'LHC.BQM.B1:NO_BUNCHES',
'LHC.BQM.B2:NO_BUNCHES',
'ADTH.SR4.B1:CLEANING_ISRUNNING',
'ADTH.SR4.B2:CLEANING_ISRUNNING',
'ADTV.SR4.B1:CLEANING_ISRUNNING',
'ADTV.SR4.B2:CLEANING_ISRUNNING']


# Switch between cals and nxcals
import pytimber
#db = pytimber.LoggingDB(source='nxcals')
db = pytimber.LoggingDB(source='ldb')

save_variables_and_json(varlist=varlist, file_path_prefix=filepath,
        save_json=saved_json, fills_dict=dict_fill_bmodes,
        db=db)



