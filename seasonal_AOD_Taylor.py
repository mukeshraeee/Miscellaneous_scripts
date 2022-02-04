"""This code initialy written by Peter A. Rochford slight changes has been made by Rai.M"""

import matplotlib.pyplot as plt
import matplotlib 
from matplotlib import rcParams
import numpy as np
import skill_metrics as sm
import pandas as pd
from sys import version_info
from matplotlib.pyplot import figure
import matplotlib.gridspec as gridspec
from pylab import figure, text, scatter, show
from matplotlib import rcParams

"""Control font"""
matplotlib.rcParams['font.family'] = "sans-serif"
matplotlib.rcParams['font.sans-serif'] = "Times New Roman"

#== WRF-CAMS
sd_c    = np.array([0,0.086,0.104,0.077,0.071])  # [winter,spring,summer,autum]
r_c     = np.array([0,0.913,0.728,0.526,0.815])
mb_c    = np.array([0,0.023,-0.076,-0.022,0.079])
rmse_c  = np.array([0,0.042,0.107,0.074,0.102])

#== WRF-MERRA
sd_m   = np.array([0,0.049,0.078,0.052,0.048])
r_m    = np.array([0,0.310,0.490,0.400,0.635])
mb_m   = np.array([0,-0.012,-0.109,-0.028,0.048])
rmse_m = np.array([0,0.076,0.141,0.072,0.099])


#== WRF-VIIRS
sd_v   = np.array([0,0.079,0.101,0.122,0.096])
r_v    = np.array([0,0.243,0.611,0.760,0.623])
mb_v   = np.array([0,0.104,0.182,0.152,0.065])
rmse_v = np.array([0,0.134,0.216,0.234,0.155])



label = ['x','Winter','Spring','Summer','Autumn']

#=== Ceat Figure =====
fig,ax = plt.subplots(figsize=(4,10),dpi=300,facecolor='w')
gridspec.GridSpec(1,2)
#==== Plot monsoon temp
plt.subplot2grid((3,1), (0,0))

sm.taylor_diagram(sd_c,rmse_c, r_c,
		      markerLabel = label,
		      markerLabelColor = 'y',markerLegend = 'on',
                      markerColor = 'y',titleRMSDangle=45, axismax=0.12,
		      tickRMS = (0.02,0.04,0.06,0.08,0.1,0.12), tickSTD=(0.03,0.06,0.09,0.110), 
                      tickRMSangle = 45,colRMS = 'tab:blue', styleRMS = '-', widthRMS = 1,titleRMS = 'on',
                      colSTD = 'tab:orange',alpha=1, styleSTD = '-',widthSTD = 1, titleSTD = 'on',
                      colCOR = 'gray', styleCOR = '--', widthCOR = 1,titleCOR = 'on')



plt.subplot2grid((3,1), (1,0))

sm.taylor_diagram(sd_m,rmse_m, r_m,
                      markerLabel = label,
                      markerLabelColor = 'y',axismax=0.12,
                      markerColor = 'y', markerLegend = 'on',titleRMSDangle=45,tickSTD=(0.03,0.06,0.09,0.110), 
		      tickRMS = (0.02,0.04,0.06,0.08,0.1,0.12),
                      tickRMSangle = 45,colRMS = 'tab:blue', styleRMS = '-', widthRMS = 1,titleRMS = 'on',
                      colSTD = 'tab:orange',alpha=1, styleSTD = '-',widthSTD = 1, titleSTD = 'on',
                      colCOR = 'gray', styleCOR = '--', widthCOR = 1,titleCOR = 'on')





plt.subplot2grid((3,1), (2,0))

sm.taylor_diagram(sd_v,rmse_v, r_v,
                      markerLabel = label,
                      markerLabelColor = 'y',axismax=0.12,
                      markerColor = 'y', markerLegend = 'on',titleRMSDangle=45,tickSTD=(0.03,0.06,0.09,0.110),
                      tickRMS = (0.02,0.04,0.06,0.08,0.1,0.12,0.14),
                      tickRMSangle = 45,colRMS = 'tab:blue', styleRMS = '-', widthRMS = 1,titleRMS = 'on',
                      colSTD = 'tab:orange',alpha=1, styleSTD = '-',widthSTD = 1, titleSTD = 'on',
                      colCOR = 'gray', styleCOR = '--', widthCOR = 1,titleCOR = 'on')






fig.subplots_adjust(top=0.95,
                        bottom=0.03,
                        left=0.015,
                        right=0.99,
                        hspace=0.3,
                        wspace=0.05)


text(1.04, 0.85, '[WRF-Chem vs. CAMS]',    ha='center', va='center', transform=ax.transAxes,rotation=90)
text(1.04, 0.43, '[WRF-Chem vs. MERRA-2]', ha='center', va='center', transform=ax.transAxes,rotation=90)
text(1.04,-0.01, '[WRF-Chem vs. VIIRS]',   ha='center', va='center', transform=ax.transAxes,rotation=90)


plt.savefig("/mnt/g/2nd_Paper/aod_spatial.png",dpi=1200)
#plt.show()
