import pytimber

varlist = [
'QRLEC_06R5_QBS947.POSST',
'QRLFC_04L5_QBS947.POSST',
'QRLFC_04R1_QBS947.POSST',
'QRLFD_04L1_QBS947.POSST',
'QRLFD_04R5_QBS947.POSST',
'QRLFE_04L2_QBS947.POSST',
 ]

db = pytimber.LoggingDB(source='ldb')

data = db.get(varlist, '2018-05-30 06:41:52.000', '2018-05-31 18:18:18.000')

import matplotlib.pyplot as plt
vars_to_plot = ['QRLFC_04L5_QBS947.POSST', 'QRLFD_04L1_QBS947.POSST']
for vv in vars_to_plot:
    t_stamps = data[vv][0]
    values = data[vv][1]

    plt.plot(t_stamps, values)

plt.show()
