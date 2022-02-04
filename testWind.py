import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import numpy as np
import cmaps
from matplotlib.patches import Patch
from pylab import *
from wrf import (to_np, getvar, interplevel, smooth2d, get_basemap, latlon_coords, ALL_TIMES)
from matplotlib.pyplot import figure
import matplotlib.gridspec as gridspec
import wrf
import scipy as sp
import scipy.ndimage
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import rcParams
import cmaps
#======== read wrf data====
win = [Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-01-01_00_00_00"),
      Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-02-01_00_00_00"),
      Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-12-01_00_00_00")]
spr = [Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-03-01_00_00_00.nc"),
       Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-04-01_00_00_00.nc"),
       Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-05-01_00_00_00.nc")]
mon = [Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-06-01_00_00_00"),
       Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-07-01_00_00_00"),
       Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-08-01_00_00_00")]
aut = [Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-09-01_00_00_00"),
       Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-10-01_00_00_00"),
       Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-11-01_00_00_00")]


"""====  Wind data ========="""
#====== Get WRF data =====================================
p  = getvar(win, "pressure")

u1 = getvar(win, "ua", units="m s-1",timeidx=-1)
v1 = getvar(win, "va", units="m s-1",timeidx=-1)

#u = getvar(win, "ua", units="m s-1",timeidx=-1)[0,:,:]
#v = getvar(win, "va", units="m s-1",timeidx=-1)[0,:,:]
#ws = np.sqrt(u**2+v**2)

#=== Now interpolate at 500 hpa  ==============================
winu1 = interplevel(u1, p, 500)
winv1 = interplevel(v1, p, 500)

#===== Take time average ===========================
#winu = np.average(winu1,axis=0)
#winv = np.average(winv1,axis=0)

#===== calculate seasonal wind speed =============
#ws = np.sqrt(winu**2+winv**2)
ws1 = np.sqrt(winu1**2+winv1**2)

#==== Normalize the data in uniform arrows ============
#win_u_wrf = winu/ws
#win_v_wrf = winv/ws

#========== Get WRF lat lon  ===================
lats, lons = latlon_coords(p)


"""
#===============================================================#
#++++++++++++++++++++++ Now Plot +++++++++++++++++++++++++++++++#
===============================================================#"""

fig = plt.figure(figsize=(5,5),dpi=200)


ax =plt.subplot(1,1,1)
m = Basemap(projection='lcc',width=12000000,height=9000000,area_thresh=1000,\
            lat_1=25,lat_2=25,lat_0=25,lon_0=90,llcrnrlon=45,llcrnrlat=0,\
             urcrnrlon=139,urcrnrlat=55,resolution='h')

x, y = m(to_np(lons), to_np(lats))


q1 = plt.pcolormesh(x,y,ws1,cmap=cmaps.MPL_YlGnBu) #MPL_RdGy_r) #cmaps.WhiteBlue) 
q2 = plt.quiver(x[::5,::5], y[::5,::5], winu1[::5,::5],winv1[::5,::5],cmap='viridis',
		pivot='middle',scale_units='inches',headwidth=4,headlength=8)



m.drawparallels(np.arange(10, 60, 15), linewidth=0.3, dashes=[2, 2],  color='black')
m.drawmeridians(np.arange(45, 125,15), linewidth=0.3, dashes=[2, 2],  color='black')
m.drawcountries(linewidth=0.1)
m.drawcoastlines(linewidth=0.1)
plt.clim(0,20)



#plt.savefig("/mnt/g/2nd_Paper/met.600dpi.png",dpi=600)

plt.show()
