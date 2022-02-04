import pygmt
import pandas as pd


#==== Load data ============
data = pd.read_csv('fire1.csv')

""" start"""
fig = pygmt.Figure()

#==== subplot
#fig.subplot(directive="begin", row=1, col=2, dimensions="f6c/3c")
#fig.subplot(directive="set", row=0, col=0)

#=== plot Fire count ==================
topo_data = '@earth_relief_30s'
minlon, maxlon = 45, 120
minlat, maxlat = 10, 55
fig.grdimage(grid=topo_data,region=[minlon, maxlon, minlat, maxlat],projection='L85/27/45/27/12c',frame="ag",shading=True)
fig.coast(borders="1/0.5p,black",land="#4F4F4F",area_thresh=1000,shorelines=True, frame=True)
fig.plot(x=data.longitude,y=data.latitude,sizes=0.01*data.longitude,style="c0.16c",color="#A4D3EE",pen="black")
#fig.legend()

#fig.subplot(directive="set", row=0, col=1)
fig.shift_origin(xshift="w+0.8c")
#=== plot FRP ===================
topo_data = '@earth_relief_30s'
minlon, maxlon = 45, 120
minlat, maxlat = 10, 55
fig.grdimage(grid=topo_data,region=[minlon, maxlon, minlat, maxlat], projection='L85/27/45/27/12c',frame="ag",shading=True)
fig.coast(borders="1/0.5p,black",land="#4F4F4F",area_thresh=1000,shorelines=True, frame=True)
	# colorbar colorma
pygmt.makecpt(cmap="jet", series=[data.frp.min(), data.frp.max()])
fig.plot(x=data.longitude,y=data.latitude, sizes=0.01*data.frp,color=data.frp / data.frp.max(), cmap="viridis", style="cc", pen="black")
fig.colorbar(frame='af+l"Fire Radiative Power"',position="JMR+o0.5c/0c+w8c")

#fig.text(text="Langtang", x=86, y=27)

#fig.savefig('frp_200dpi.png',dpi=200)
fig.show(method="external")
