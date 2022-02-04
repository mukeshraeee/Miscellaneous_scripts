from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

fig,ax = plt.subplots()

m = Basemap(projection="mill", #miller est une projection connu
    llcrnrlat =0,#lower left corner latitude
    llcrnrlon =0,
    urcrnrlat =10, #upper right lat
    urcrnrlon =10,
    resolution = "l", ax=ax) #c croud par defaut, l low , h high , f full 
m.drawcoastlines() #dessiner les lignes
m.drawcountries()
m.drawstates()
m.drawcounties(color="b")

x,y=m(3,3)
x2,y2 = m(3,3+2) 
circle1 = plt.Circle((x, y), y2-y, color='black',fill=False)
ax.add_patch(circle1)
plt.show()
