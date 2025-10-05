import json
import csv

with open('Earthquake.geojson', 'r') as f:
    data = json.load(f)
    features = data['features']
    data_list = []
    for i in features:
        properties = i['properties']
        row_data = []
        for j in properties:
            if j == 'LAT' or j == 'LONG_' or j == 'MAGMB' or j == 'DEPTH_KM':
                row_data.append(properties[j])
        data_list.append(row_data)

with open('earthquake.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['LAT', 'LONG_', 'MAGMB', 'DEPTH_KM'])
    writer.writerows(data_list)