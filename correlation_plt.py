
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

f1 = xr.open_dataset('sst.DJF.mean.anom.nc')
pre = f1['sst_anom'][:-1, :, :]  # Take all three-dimensional data, time, latitude + longitude
#pre = f1['sst_anom'][:, :, :]
#pre = f1['sst_anom'][0:-1, :, :]  # 
#pd.DataFrame(pre)
pre


lat, lon = f1['lat'], f1['lon']
lat, lon 

# ======== Convert the extracted three-dimensional data of pre into two-dimensional, named pre2d
pre2d = np.array(pre).reshape(pre.shape[0],pre.shape[1]*pre.shape[2])

#==== Add another data ========================
f2 = xr.open_dataset('pc.DJF.sst.nc')

#Then take the required pc data out of f2, take the first pc sequence, that is, all the columns of row 0 [0,:]
pc = f2['pc'][5, :]


#=== Now calculate  correlation =================
pre_pc_cor = np.corrcoef(pre2d.T, pc)[:-1, -1].reshape(len(lat), len(lon))  ## The last one is not available, you can compare the printed results without [:-1, -1]
#pre_pc_cor = np.corrcoef(pre2d.T, pc)[:, :].reshape(len(lat), len(lon))

# pre_pc_cor
# pre_pc_cor = np.corrcoef(pre2d.T, pc)
# pd.DataFrame(pre_pc_cor)
# pre_pc_cor

#=== significance test part, univariate linear regression test f_regression, returns F score, and the p value of F score
pre_cor_sig = f_regression(np.nan_to_num(pre2d), pc)[1].reshape(len(lat), len(lon)) # Use 0 instead of NaN, finite number proxy inf value
area = np.where(pre_cor_sig < 0.05) #area records the p value on each grid point of latitude and longitude, and the size should be 39*lat*lon



#===== Now plot ================
nx, ny = np.meshgrid(lon, lat)
plt.figure(figsize=(16, 8))
#== Set colorbar  ==============
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 20

ax = plt.subplot(projection=ccrs.PlateCarree(central_longitude=179))

ax.coastlines(lw=0.4)
ax.set_global()
#ax.stock_img()

c2 = ax.contourf(nx, ny, pre_pc_cor, cmap=cmaps.MPL_RdBu, transform=ccrs.PlateCarree())
#c2 = ax.contourf(nx, ny, pre_pc_cor, cmap=cmaps.GMT_polar, transform=ccrs.PlateCarree())
#plt.colorbar(c2,fraction=0.05,orientation='horizontal', shrink=0.4, pad=0.06)
plt.colorbar(c2,orientation='horizontal',pad=0.06,shrink=0.6)

#==== Dot the area that passed the 0.05 significance test, using the scatter function ====================================
ax.scatter(nx[area], ny[area], marker='+', s=1, c='k', alpha=0.6, transform=ccrs.PlateCarree())
""" nx and ny are the latitude and longitude after gridding, area is a number, and records the number 
    less than 0.05, so the meaning of nx[area] is to get the latitude and longitude grid points less than 0.05"""

# Set the latitude and longitude lines and their identification
plt.title('Correlation Analysis',pad=20,  fontdict={'family' : 'Times New Roman', 'size'   : 20})
#=====Set the title font and its size, pad is the position of the specific picture of the title==================
ax.set_xticks(np.arange(0, 361, 30),crs=ccrs.PlateCarree())

# ===============
plt.xticks(fontproperties = 'Times New Roman',size=16)
plt.yticks(fontproperties = 'Times New Roman',size=16)

ax.set_yticks(np.arange(-90, 90, 15),crs=ccrs.PlateCarree())

ax.xaxis.set_major_formatter(LongitudeFormatter(zero_direction_label = False)) # Longitude 0 degrees without anything
ax.yaxis.set_major_formatter(LatitudeFormatter())

ax.set_extent([-179, 179+1, -70, 70], crs=ccrs.PlateCarree())

ax.gridlines(color='black', alpha=0.4) # 

ax.tick_params(which='major', direction='out', length=10, width=0.99, pad=0.2, bottom=True, left=True, right=True, top=True)

ax.minorticks_on()  #
ax.tick_params(which='minor', direction='out', length=6, width=0.6, pad=0.1, bottom=True, left=True, right=True, top=True)


plt.show()
