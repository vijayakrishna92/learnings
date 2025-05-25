

import rasterio
row, col = 100, 200
with rasterio.open('images/3.tif') as src:
    lon, lat = src.xy(row, col)  # Get geo coordinates of that pixel
    print(f"Lat: {lat}, Lon: {lon}")