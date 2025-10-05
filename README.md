# Earthquake Detection Model [Only Classifier - Moderate or Strong]

A machine learning model to detect and classify moderate or strong earthquakes in India.

This machine learning model is trained on Official Dataset from [BHUKOSH - Geological Survey of India](https://bhukosh.gsi.gov.in/Bhukosh/Public).

## Dataset

CSV File - [dataset](earthquake.csv)

This CSV File is created by extracting data from [.geojson File](Earthquake.geojson) using this [python script](create_dataset_csv.py).

This [.geojson File](Earthquake.geojson)  is downloaded from [BHUKOSH - Geological Survey of India](https://bhukosh.gsi.gov.in/Bhukosh/Public).

The CSV File only has 4 columns. If you want to create more versatile and better model you can modify [this python script](create_dataset_csv.py) to extract more data.

## Data Dictionary [This is for .geojson file]

OBJECTID - Unique Identifier for every data

SOURCE - Source of the Data (ISC = International Seismological Centre, NEIC = National Earthquake Information Center)

YR - Year when the earthquake occurred

MO - Month when the earthquake occurred

DT - Date when the earthquake occurred

HR - Hour when the earthquake occurred

MN - Minutes when the earthquake occurred

SEC - Seconds when the earthquake occurred

LAT - Latitude of Location where the earthquake occurred

LONG_ - Longitude where the earthquake occurred

MAGMB - Body Wave Magnitude (less accurate but reliable for small scale earthquakes)

DEPTH_KM - Depth from the earth surface (in Kilometers)

MW - Moment Magnitude (more accurate specifically for large scale earthquakes)

## Notebook

This is the [Google Colab Notebook](https://colab.research.google.com/drive/1tIuRzrtZpWHwdHoGxAVVhI9hHvCOpsDg?usp=sharing).

#### Before running this Notebook

Make sure that you have mounted your google drive and the csv file is uploaded to your google drive. Also change the path of the dataset.
