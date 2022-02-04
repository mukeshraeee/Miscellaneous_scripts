from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
import numpy as np
import wrf
from wrf import (to_np, getvar,interplevel, smooth2d, get_basemap, latlon_coords, ALL_TIMES)
from matplotlib.cm import get_cmap
import matplotlib.pyplot as plt
import cmaps
from pylab import *
import scipy as sp
import scipy.ndimage
import matplotlib.gridspec as gridspec
import cartopy.crs as crs
from cartopy.feature import NaturalEarthFeature
from matplotlib.patches import FancyArrowPatch
from matplotlib.legend_handler import HandlerLine2D
from matplotlib import rcParams

#====== read merra-2 dust data ======
dust = Dataset("/mnt/g/2nd_Paper/merra2_bc_oc_dust/winter1.nc")
#====== read merra-2 GPH data ======
win_gph1 = Dataset("/mnt/g/2nd_Paper/merra_2_Geopotential_Height/winter.nc")


#===== get dust data from merra-2===
win_dust1 = dust.variables['DUSMASS'][:]
z1        = win_gph1.variables['H'][:,7,:,:]

win_dust  = np.mean(win_dust1[:,:,:],axis=0)*1000000000
z         = np.mean(z1,axis=0)

""" plot DUST """
lat1   = dust.variables['lat'][:]
lon1   = dust.variables['lon'][:]

"""winter"""
ax =plt.subplot(1,1,1)
m = Basemap(projection='lcc',width=12000000,height=9000000,area_thresh=1000,\
            lat_1=25,lat_2=25,lat_0=25,lon_0=90,llcrnrlon=45,llcrnrlat=0,\
             urcrnrlon=139,urcrnrlat=55,resolution='h')
lons,lats = np.meshgrid(lon1,lat1)
x,y = m(lons, lats)
s = m.pcolormesh(x,y,win_dust,cmap=cmaps.temp_diff_18lev)

#=== add GPH contour
contours = plt.contour(x, y, z, 10, linestyles="dashed",linewidths=0.5)
plt.clabel(contours, inline=True, fontsize=8,inline_spacing=0,fmt='%1.0f')



m.drawparallels(np.arange(10, 60, 15), linewidth=0.3, labels=[0,1,0,0],dashes=[2, 2],  fontsize=12,color='black')
m.drawmeridians(np.arange(45, 125,15), linewidth=0.3, dashes=[2, 2],  color='black')
m.drawcountries(linewidth=0.1)
m.drawcoastlines(linewidth=0.1)
#plt.clim(0,600)

plt.show()
