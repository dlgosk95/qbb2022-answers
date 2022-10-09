#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from bdg_loader import *

# bdg = load_data('cropped_R1.bdg')
# print(bdg)
# {'X': array([35502089.18, 35502189.54, 35502289.9 , 35502390.26, 35502490.62,35502590.98, 35502691.34, 35502791.7 , 35502892.06, 35502992.42,35503092.78, 35503193.14, 35503293.5 , 35503393.86, 35503494.22, 35503594.58, 35503694.94, 35503795.3 , 35503895.66, 35503996.02, 35504096.38, 35504196.74, 35504297.1 , 35504397.46, 35504497.82, 35504598.18, 35504698.54, 35504798.9 , 35504899.26, 35504999.62, 35505099.98, 35505200.34, 35505300.7 , 35505401.06, 35505501.42, 35505601.78, 35505702.14, 35505802.5 , 35505902.86, 35506003.22, 35506103.58, 35506203.94, 35506304.3 , 35506404.66, 35506505.02, 35506605.38, 35506705.74, 35506806.1 , 35506906.46, 35507006.82]), 'Y': array([ 1306.08777244,   687.29029608,   752.7465845 ,   901.20392384, 1299.67715948,  1636.74303315,  1990.00411484,  3252.5669306 , 4447.31159365,  3796.46087474,  2335.84238041,  1368.17007164, 1216.00122113,  1168.42735934,  1313.84813184,  2120.91657792, 3497.18425357,  6174.81613665,  9298.83242579, 11308.06859282, 11068.1748633 ,  7937.74785455,  4321.46028863,  2307.16316264, 1822.98956098,  1901.60454748,  1383.69059844,   775.35244815, 401.8472391 ,    99.53405109,     0.        ,    17.88225598, 43.18753429,    79.9647685 ,   103.92023637,    93.79816914, 273.97140685,   524.32469   ,   921.1106857 ,  1297.65277448, 1094.53600185,  1001.75012832,  1139.74807047,  1048.98652506, 1038.52704254,  1244.34302362,  1278.08332123,  1196.76918316, 1184.28532275,  1517.6396568 ])}

# traces = ['cropped_Sox2.bdg', 'cropped_Klf4.bdg', 'cropped_H3K27ac_Day0.bdg', 'cropped_H3K27ac_Day2.bdg']
traces = ['Sox2', 'Klf4', 'H3K27ac_Day0', 'H3K27ac_Day2']
fig, ax = plt.subplots(4)
for i, trace in enumerate(traces):
    fname = f"cropped_{trace}.bdg"
    data= load_data(fname)
    x=data['X']
    y=data['Y']
    ax[i].plot(x,y)
    ax[i].fill_between(x,y)
    ax[i].set_ylabel(trace, fontsize = 9)
plt.savefig('assignment5.png')
plt.subplots_adjust(hspace = 1)
plt.xlabel("Location along Chromosome 17")
fig.tight_layout(pad=1.0)
plt.show()