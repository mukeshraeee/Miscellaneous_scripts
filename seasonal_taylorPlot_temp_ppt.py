
"""This code initialy written by Peter A. Rochford 
slight changes has been made by Rai.M"""

import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import skill_metrics as sm
import pandas as pd
from sys import version_info
from matplotlib.pyplot import figure
import matplotlib.gridspec as gridspec

#=== Add cyberpunk effect ==
#import mplcyberpunk
#plt.style.use("cyberpunk")
#mplcyberpunk.add_glow_effects()
#mplcyberpunk.make_lines_glow()
#mplcyberpunk.add_underglow()

#== Arrnge  dataframe
#---For Temp-------------------
#==Monsoon
sd_m_t   = np.array([0,6.25,3.09]) #,5.56])  # [WRF_CRU,WRF_ERA5,ERA5_CRU]
R_m_t    = np.array([0,0.82,0.90]) #,0.73])
MB_m_t   = np.array([0,-2.46,2.32]) #,-4.78])
RMSE_m_t = np.array([0,4.40,9.43,9]) #.40])
#== Non-Monsoon
MB_nm_t   = np.array([0,1.21,12.24]) #,-11.04])
R_nm_t    = np.array([0,0.96,0.93]) #,0.96])
sd_nm_t   = np.array([0,10.77,4.55]) #,13.36])
RMSE_nm_t = np.array([0,4.45,19.43]) #,20.92])
#-- For Precipitation------------------
#==Monsoon
RMSE_m_p =np.array([0,276.53,444.79])  #,522.98])
MB_m_p   =np.array([0,-186.21,307.31]) #,-493.52])
R_m_p    =np.array([0,0.80,0.3])       #,0.23])
sd_m_p   =np.array([0,312.25,87.90])   #,170.53])
#== Non-Monsoon
RMSE_nm_p =np.array([0,285.11,248.99]) #,403.22])
MB_nm_p   =np.array([0,-180.20,120.87]) #,-301.07])
R_nm_p    =np.array([0.7,0.63,0.4]) #,0.33])
sd_nm_p   =np.array([0,208.13,47.60]) #,279.93])


label1 = ['x','WRF_CRU_T[Mon]','WRF_ERA5_T[Mon]']          #,'CRU_ERA5_T[Mon]']
label2 = ['x','WRF_CRU_T[Non-Mon]','WRF_ERA5_T[Non-Mon]']  #,'CRU_ERA5_T[Non-Mon]']
label3 = ['x','WRF_TRMM_P[Mon]','WRF_ERA5_P[Mon]']         #,'TRMM_ERA5_P[Mon]']
label4 = ['x','WRF_TRMM_P[Non-Mon]','WRF_ERA5_P[Non-Mon]'] #,'TRMM_ERA5_P[Non-Mon]']

#label = ['Non-Dimensional Observation', 'M1', 'M2', 'M3']
fig = plt.figure(figsize=(10,10),dpi=200,facecolor='w')
gridspec.GridSpec(2,2)

#==== Plot monsoon temp
plt.subplot2grid((2,2), (0,0))

ax1 = sm.taylor_diagram(sd_m_t,RMSE_m_t, R_m_t,
                      markerLabel = label1,
                      markerLabelColor = 'y',
                      markerColor = 'y', markerLegend = 'on',titleRMSDangle=45,
                      tickRMS = range(0,10,2), tickRMSangle = 55,colRMS = 'tab:blue', styleRMS = '-', widthRMS = 1,titleRMS = 'on', 
                      tickSTD = range(0,9,3),colSTD = 'tab:orange',alpha=1, styleSTD = '-',widthSTD = 1, titleSTD = 'on',
                      colCOR = 'gray', styleCOR = '--', widthCOR = 1,titleCOR = 'on')


plt.text(0.5,7.5,'[a]',fontsize=15)
#==== Plot non-monsoon temp
plt.subplot2grid((2,2), (0,1))

sm.taylor_diagram(sd_nm_t,RMSE_nm_t, R_nm_t,
                      markerLabel = label2,
                      markerLabelColor = 'y',
                      markerColor = 'y', markerLegend = 'on',titleRMSDangle=45,
                      tickRMS = range(0,25,5), tickRMSangle = 55.0,colRMS = 'tab:blue', styleRMS = '-', widthRMS = 1,titleRMS = 'on',
                      tickSTD = range(0,15,3),colSTD = 'tab:orange',alpha=1, styleSTD = '-',widthSTD = 1, titleSTD = 'on',
                      colCOR = 'gray', styleCOR = '--', widthCOR = 1,titleCOR = 'on')

plt.text(0.8,14,'[b]',fontsize=15)

#==== Plot monsoon ppt
plt.subplot2grid((2,2), (1,0))

sm.taylor_diagram(sd_m_p,RMSE_m_p, R_m_p,
                      markerLabel = label3,
                      markerLabelColor = 'y',
                      markerColor = 'y', markerLegend = 'on',titleRMSDangle=45,
                      tickRMS = range(0,550,50), tickRMSangle = 55.0,colRMS = 'tab:blue', styleRMS = '-', widthRMS = 1,titleRMS = 'on',
                      tickSTD = range(0,290,45),colSTD = 'tab:orange',alpha=1, styleSTD = '-',widthSTD = 1, titleSTD = 'on',
                      colCOR = 'gray', styleCOR = '--', widthCOR = 1,titleCOR = 'on')

plt.text(20,370,'[c]',fontsize=15)
#==== Plot non-monsoon ppt
plt.subplot2grid((2,2), (1,1))

sm.taylor_diagram(sd_nm_p,RMSE_nm_p, R_nm_p,
                      markerLabel = label4,
                      markerLabelColor = 'y',
                      markerColor = 'y', markerLegend = 'on',titleRMSDangle=45,
                      tickRMS = range(0,405,45), tickRMSangle = 55,colRMS = 'tab:blue', styleRMS = '-', widthRMS = 1,titleRMS = 'on',
                      tickSTD = range(0,350,50),colSTD = 'tab:orange',alpha=1, styleSTD = '-',widthSTD = 1, titleSTD = 'on',
                      colCOR = 'gray', styleCOR = '--', widthCOR = 1,titleCOR = 'on')

plt.text(20,280,'[d]',fontsize=15)
#---- add text ======



plt.savefig('/mnt/g/Paper_work/Taylor800.png',dpi=800,facecolor='w')

 # Show plot
#plt.show()
