import os
import pickle as pickle

import LHCMeasurementTools.TimberManager as tm
import LHCMeasurementTools.pytimber_interface as pti
import LHCMeasurementTools.LHC_Energy as Energy
import LHCMeasurementTools.LHC_BCT as BCT

import pytimber

db = pytimber.LoggingDB()

test_fill = 5885

varlist = Energy.variable_list() + BCT.variable_list()

with open('./fills_and_bmodes.pkl') as f:
    fills_and_bmodes = pickle.load(f)


t_begin, t_end = fills_and_bmodes[test_fill]['t_startfill'], fills_and_bmodes[test_fill]['t_endfill']

pti.save_variables_to_h5('./test.h5', varlist, t_begin, t_end, db)

fill_dict = tm.timber_variables_from_h5('./test.h5')

os.remove('./test.h5')
