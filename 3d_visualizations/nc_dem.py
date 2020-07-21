import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import rasterio as rio
from rasterio.mask import mask
from rasterio.plot import show
import geopandas as gpd
import numpy as np
from scipy.interpolate import Rbf
from IPython import embed as II

dem = rio.open("new_res.tif")
states = gpd.read_file("./cb_2018_us_state_500k/cb_2018_us_state_500k.shp")
nc = states[states["STUSPS"] == "NC"]
masked, affine = mask(dem, nc["geometry"], crop=True, all_touched=True, nodata=0)

# data = dem.read()[0]
data = masked[0]
data_h, data_w = data.shape
minx, miny, maxx, maxy = dem.bounds

#! Dont think I actually need these
delx = (maxx - minx)/data_w
dely = (maxy - miny)/data_h

xcoords = np.linspace(maxx, minx, num=data_w)
ycoords = np.linspace(miny, maxy, num=data_h)
xv, yv = np.meshgrid(xcoords, ycoords)
# spline = Rbf(xcoords, ycoords, data, function="thin-plate")
# Z = spline(xv, yv)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(xv, yv, data, cmap="terrain", linewidth=0, vmin=1)
# ax.contour(xv, yv, data, [1], cmap="hsv", zorder=10)
for polygon in nc["geometry"].values[0]:
    xs, ys = polygon.exterior.xy
    ax.plot(xs, ys, color="k", linewidth=2, zorder=100)

plt.show()