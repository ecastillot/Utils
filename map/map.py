import pygmt
import numpy as np
import pandas as pd

reg = [-83, -68, -5, 15]

fig = pygmt.Figure()
stations = pd.read_csv("./stations.csv")

## Mapa
proj = 'M6i'
fig.grdimage(
        '@earth_relief_01m',
        region=reg,
        projection=proj,
        cmap='etopo1',
        shading=True,
        )
fig.coast(
            region=reg,
            projection=proj,
            shorelines=True,
            water='lightblue',
            # water='white',
            borders='1/1p,black',
            frame="afg",
        )


for index,row in stations.iterrows():
    fig.plot(x=row.longitude, y=row.latitude, 
            style="t0.5c", color=row.color, pen="black")


##Mundo
fig.shift_origin(xshift='0i',yshift='0i')  # Shift for next call
proj = 'G-70/0/2.0i'
fig.grdimage(
            '@earth_relief_10m',
            region='g',
            projection=proj,
            cmap='globe',
            shading=True,
          )
fig.coast(
            region='g',
            projection=proj,
            shorelines=True,
            water='white',
            borders='1/1p,black',
            land='grey',
            frame=True,
        )

x_reg = [reg[0], reg[1], reg[1], reg[0], reg[0]]
y_reg = [reg[2], reg[2], reg[3], reg[3], reg[2]]
fig.plot(x_reg,y_reg,
        pen="2p,red")

fig.savefig('./test.png')
fig.show()