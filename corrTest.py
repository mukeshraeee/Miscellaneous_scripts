import numpy as np
import xarray as xr
from sklearn.feature_selection import f_regression
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cmaps
import pandas as pd
import xarray as xr
import wrf
from wrf import (to_np, getvar,interplevel, smooth2d, get_basemap, latlon_coords, ALL_TIMES)
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
#======== read wrf data====
win = [Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-01-01_00_00_00"),
      Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-02-01_00_00_00"),
      Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-12-01_00_00_00")]

#=== pm2.5==
pm  = getvar(win, "PM2_5_DRY", timeidx=ALL_TIMES,method='cat')[:,0,:,:]
#====  PBLH  =================
pbl = getvar(win, "PBLH", timeidx=ALL_TIMES,method='cat')[:,:,:]



"""======== Convert the extracted three-dimensional data of pre into two-dimensional, named pre2d"""
pm_2d  = np.array(pm).reshape(pm.shape[0],pm.shape[1]*pm.shape[2])

#pbl_2d = np.array(pbl).reshape(pbl.shape[0],pbl.shape[1]*pbl.shape[2])
#pbl_2d1 = pbl_2d[:,5]

pbl1 = np.average(pbl,axis=1)
pbl2 = np.average(pbl1,axis=1) 
#=== Pressure ==============
lat, lon = latlon_coords(pm)
#=== Now calculate  correlation =================
#corr = np.corrcoef(pm_2d.T, pbl_2d)[:-1, -1].reshape(len(lat), len(lon)) 
corr = np.corrcoef(pm_2d.T, pbl2)[:-1, -1].reshape(len(lat), len(lon))

#pre_cor_sig = f_regression(np.nan_to_num(pre2d), pc)[1].reshape(len(lat), len(lon))
