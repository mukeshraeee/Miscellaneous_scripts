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
import matplotlib.patches as mpatches
#======== read wrf data====
win = [Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-01-01_00_00_00"),
      Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-02-01_00_00_00"),
      Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-12-01_00_00_00")]
#win = [Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-03-01_00_00_00.nc"),
#       Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-04-01_00_00_00.nc"),
#       Dataset("/mnt/g/WRF_All/WRF_Output/WRF_output_new/all_output/wrfout_d01_2017-05-01_00_00_00.nc")]


#===== get OC,PM2.5 and PM10 data from WRF data =====================
#=== pm2.5==
p = getvar(win,"pressure")


#=== at surface==
#win_pm25 = getvar(win, "PM2_5_DRY", timeidx=ALL_TIMES,method='cat')[:,0,:,:]
#win_p25 = np.average(win_pm25,axis=0)
#=== interpolation at pressure ht. =====================================
win_pm25  = getvar(win, "PM2_5_DRY", timeidx=-1,method='cat')[:,:,:]
win_p25 = interplevel(win_pm25, p, 700)

#=== Geo-potenatial ht. ==========================================
z1 = getvar(win, "z", units="m",timeidx=-1,method='cat')
z = interplevel(z1, p, 700)

#=== plot ============================
lats, lons = latlon_coords(win_pm25)

fig = plt.figure(figsize=(5,5),dpi=200)
ax =plt.subplot(1,1,1)

m = Basemap(projection='lcc',width=12000000,height=9000000,area_thresh=1000,\
            lat_1=25,lat_2=25,lat_0=25,lon_0=90,llcrnrlon=45,llcrnrlat=0,\
             urcrnrlon=139,urcrnrlat=55,resolution='h')
x, y = m(to_np(lons), to_np(lats))
s1 = m.pcolormesh(x,y,win_p25,cmap=cmaps.temp_diff_18lev)  #CBR_coldhot) #BlueWhiteOrangeRed) #amwg_blueyellowred) #BlueWhiteOrangeRed) #MP>


#s2 = plt.contour(x, y, z,  10, linestyles="dashed",linewidths=0.5)
#plt.clabel(contours, inline=True, fontsize=8,inline_spacing=0,fmt='%1.0f')

m.drawparallels(np.arange(10, 60, 15), linewidth=0.3, dashes=[2, 2],  color='black')
m.drawmeridians(np.arange(45, 125,15), linewidth=0.3, dashes=[2, 2],  color='black')
m.drawcountries(linewidth=0.3)
m.drawcoastlines(linewidth=0.3)
plt.ylabel('Winter', labelpad=5,fontsize=12)
plt.clim(0,130)

cb1 = plt.colorbar(s1, ax=ax,  ticks=[0,20,40,60,80,100,120,140], orientation='horizontal')

s2 = plt.contour(x, y, z,  10, linestyles="dashed",linewidths=0.5)
plt.clabel(s2, inline=True, fontsize=5,inline_spacing=0,fmt='%1.0f')

plt.show()

