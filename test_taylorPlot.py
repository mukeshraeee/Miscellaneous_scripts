import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import skill_metrics as sm
import pandas as pd
from sys import version_info
from matplotlib.pyplot import figure
import matplotlib.gridspec as gridspec

#== Arrnge  dataframe
if __name__ == '__main__':

    # Close any previously open graphics windows
    # ToDo: fails to work within Eclipse
    plt.close('all')




rcParams["figure.figsize"] = [8.0, 6.4]
rcParams['lines.linewidth'] = 1 # line width for plots
rcParams.update({'font.size': 10}) # font size of axes text


label1 = ['x','WRF_CRU_T[Mon]','WRF_ERA5_T[Mon]','CRU_ERA5_T[Mon]']
#---For Temp-------------------
#==Monsoon
sdev   = np.array([0,6.25,3.09,5.56])  # [WRF_CRU,WRF_ERA5,ERA5_CRU]
ccoef    = np.array([0,0.82,0.90,0.73])
bias   = np.array([0,-2.46,2.32,-4.78])
crmsd = np.array([0,4.40,9.43,9.40])


sm.taylor_diagram(sdev, crmsd, ccoef, markerLabel = label1,
                      locationColorBar = 'EastOutside',
                      markerDisplayed = 'colorBar', titleColorBar = 'Bias',
                      markerLabelColor='black', markerSize=10,
                      markerLegend='off', cmapzdata=bias,
                      colRMS='g', styleRMS=':', widthRMS=2.0, titleRMS='on',
                      colSTD='b', styleSTD='-.', widthSTD=1.0, titleSTD ='on',
                      colCOR='k', styleCOR='--', widthCOR=1.0, titleCOR='on')



plt.show()

