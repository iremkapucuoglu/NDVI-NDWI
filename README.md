# NDVI-NDWI Calculations
The test images which are used for this project are downloaded from https://earthexplorer.usgs.gov/
To see the vegetaiton and lake cover near Burdur area in Turkey, NDVI and NDWI calculations are applied with the given codes. 1985 and 2020 are selected as study years and september, october and november are selected as study months for each year. 
Since Landsat5 data starts in 1984 and ends in 2012, it is selected as the sensor for 1985 study area. On the other hand Landsat8 data starts in 2013 and comes today, it is selected as the sensor for 2020 study area. 


## Libraries Used in Jupyter Notebook
- matplotlib
- numpy
- skimage

## Data Collection and Band Selection
- For the year 1985, input bands are downloaded from the given usgs link above. The metadata of the test image is:
https://earthexplorer.usgs.gov/scene/metadata/full/5e83d0a05ee25348/LT51780341985264FUI00/

- For the year 2020, input bands are downloaded from the same page again and the metadata is:
https://earthexplorer.usgs.gov/scene/metadata/full/5e81f14f59432a27/LC81780342020281LGN00/

RGB color images are given above as the left one is 1985 and the right one is 2020 image.
! [RGB](RGB.png)

