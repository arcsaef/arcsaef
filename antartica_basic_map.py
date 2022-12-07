import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import shapefile as shp

plt.rcParams.update({'font.size': 14})

fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,2,1, projection=ccrs.SouthPolarStereo())

ax1.coastlines("110m")
ax1.gridlines()
ax1.set_title("Map of Antarctica")
ax1.set_extent([-180, 180, -90, -60], ccrs.PlateCarree())

# Add features
ax1.add_feature(cfeature.LAND, color="white")
ax1.add_feature(cfeature.OCEAN, color="lightblue")

plt.show()
