
import os
import h5py
import pickle as pickle
import json

import LHCMeasurementTools.TimberManager as tm
from LHCMeasurementTools.LHC_FBCT import FBCT
from LHCMeasurementTools.LHC_BCT import BCT
from LHCMeasurementTools.LHC_BQM import blength

import HeatLoadCalculators.FillCalculator as fc
import HeatLoadCalculators.impedance_heatload as ihl
import HeatLoadCalculators.synchrotron_radiation_heatload as srhl

h5folder = 'heatloads_fill_h5s'
#fills_pkl_name = 'fills_and_bmodes.pkl'
fills_json_name = 'fills_and_bmodes.json'

hli_calculator  = ihl.HeatLoadCalculatorImpedanceLHCArc()
hlsr_calculator  = srhl.HeatLoadCalculatorSynchrotronRadiationLHCArc()

# with open(fills_pkl_name, 'rb') as fid:
#     dict_fill_bmodes = pickle.load(fid)
with open(fills_json_name, 'r') as fid:
    dict_fill_bmodes = json.load(fid)

if not os.path.isdir(h5folder):
    os.mkdir(h5folder)

for filln in sorted(dict_fill_bmodes.keys())[::-1]:
    print('Fill %s' %filln)
    h5filename = h5folder+'/imp_and_SR_fill_%s.h5'%filln

    if dict_fill_bmodes[filln]['flag_complete'] is False:
        print("Fill incomplete --> no h5 convesion")
        continue

    if os.path.isfile(h5filename):
        print("Already complete and in h5")
        continue
    try:
        fill_dict = {}
        fill_dict.update(tm.CalsVariables_from_h5(
            'fill_basic_data_h5s/basic_data_fill_%s.h5'%filln))
        fill_dict.update(tm.CalsVariables_from_h5(
            'fill_bunchbybunch_data_h5s/bunchbybunch_data_fill_%s.h5'%filln))

        fbct_bx = {}
        bct_bx = {}
        blength_bx = {}
        for beam_n in (1,2):
            fbct_bx[beam_n] = FBCT(fill_dict, beam=beam_n)
            bct_bx[beam_n] = BCT(fill_dict, beam=beam_n)
            blength_bx[beam_n] = blength(fill_dict, beam = beam_n)

        hl_imped_fill = fc.HeatLoad_calculated_fill(fill_dict, hli_calculator, bct_dict=bct_bx, fbct_dict=fbct_bx, blength_dict=blength_bx)
        hl_sr_fill = fc.HeatLoad_calculated_fill(fill_dict, hlsr_calculator, bct_dict=bct_bx, fbct_dict=fbct_bx, blength_dict=blength_bx)
        dict_to_h5 = {}
        for title, hl in zip(['imp_arc_wm', 'sr_arc_wm'], [hl_imped_fill, hl_sr_fill]):
            dict_to_h5[title+'!t_stamps'] = hl.t_stamps
            dict_to_h5[title+'!values'] = hl.heat_load_calculated_total

        with h5py.File(h5filename, 'w') as fid:
            for key, value in dict_to_h5.items():
                fid[key] = value

    except Exception as e:
        print('Skipped! Error %s' % e)

