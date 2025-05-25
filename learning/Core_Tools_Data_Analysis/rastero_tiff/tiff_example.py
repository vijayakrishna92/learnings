import rasterio
#https://people.math.sc.edu/Burkardt/data/tif/tif.html
# Open raster file
with rasterio.open('images/3.tif') as src:
    print(src.name)
    print(src.count)       # number of bands
    print(src.width, src.height)
    print(src.crs)         # coordinate reference system
    print(src.transform)   # affine transform (maps pixel to geographic coords)

    # Read the first band
import matplotlib.pyplot as plt

with rasterio.open('images/3.tif') as src:
    band = src.read(1)

plt.imshow(band, cmap='gray')
plt.title('Band 1')
plt.colorbar()
plt.show()

# Get pixel value at specific coordinates
row, col = 100, 200
with rasterio.open('images/3.tif') as src:
    lon, lat = src.xy(row, col)  # Get geo coordinates of that pixel
    print(f"Lat: {lat}, Lon: {lon}") 