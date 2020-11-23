import numpy as np
import json, sys

from LHCMeasurementTools.LHC_Fill_LDB_Query import load_fill_dict_from_json

def reconfigure_json(jsonname, fillnumbers):

    fill_dict = load_fill_dict_from_json(jsonname)

    fillnumbers = np.atleast_1d(fillnumbers)
    for fill in fillnumbers:
        fill_dict[int(fill)] = 'incomplete'

    with open(jsonname, 'w') as fid:
        json.dump(fill_dict, fid)

if len(sys.argv)>2:
    jsonname = sys.argv[1]
    fillnumbers = sys.argv[2].split(',')
    reconfigure_json(jsonname, fillnumbers)
else:
    print("Provide jsonname and list of fills!")
