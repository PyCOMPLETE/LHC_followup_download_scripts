import matplotlib.pyplot as plt

from LHCMeasurementTools import myfilemanager as mfm
from LHCMeasurementTools import mystyle as ms

ob = mfm.myloadmat_to_obj('./time_build.mat')

plt.close('all')
ms.mystyle(fontsz=14)
fig1 = plt.figure(1)
#ax11 = fig1.add_subplot(2,1,1)
ax12 = fig1.add_subplot(111)

#ax11.semilogx(ob.n_variables, ob.Dt, 'o')
ax12.loglog(ob.n_variables, ob.Dt/ob.n_variables, 'o')
ax12.set_xlabel('Number of variables')
ax12.set_ylabel('Extraction time [s/variable]')
ax12.grid(True, linestyle='--')
ax12.set_ylim(bottom=0.1)
fig1.subplots_adjust(bottom=.15, left=.16)

plt.show()
