from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import urllib.request, csv
url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
response = urllib.request.urlopen(url)
csvfile = csv.reader(response.read().decode('utf-8').splitlines())
map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
map.fillcontinents(color='coral',lake_color='aqua')
map.drawmapboundary(fill_color='aqua')
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))
lons = []
lats = []
mags = []
for row in csvfile:
    if not row[1].isalpha():
        lon = float(row[2])
        lat = float(row[1])
        mag = float(row[4])
        lons.append(lon)
        lats.append(lat)
        mags.append(mag)
x,y = map(lons,lats)
map.plot(x,y, 'go', markersize=5)
for i in range(0, len(lons)):
    if mags[i] >= 3.5:
        x,y=map(lons[i], lats[i])
        map.plot(x,y, 'ro', markersize=4)
for i in range(0, len(lons)):
    if mags[i] >= 6:
        x,y=map(lons[i], lats[i])
        map.plot(x,y, 'kx', markersize=10, markeredgewidth = 2.0)
plt.show()
