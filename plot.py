import simplekml
import csv

filename = "GPSFILE.CSV"

# Add multiple GPS coordinates with height/altitude information
coords_list = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header row
    for row in csvreader:
        if len(row) >= 12 and row[11] == '1':  # check if column L is equal to 1
            coords_list.append((float(row[6]), float(row[7]), float(row[8])))  # save columns G, H, and I as a tuple of coordinates

print(coords_list)

# Create a KML object
kml = simplekml.Kml()

# Add the GPS coordinates as points with altitude information
for lat, lon, alt in coords_list:
    point = kml.newpoint(name='', coords=[(lon, lat, alt)])
    point.altitudemode = simplekml.AltitudeMode.absolute

    # Add a line string element to connect the points
    linestring = kml.newlinestring(name='', coords=[(lon, lat, alt), (lon, lat, 0)])
    linestring.altitudemode = simplekml.AltitudeMode.absolute
    linestring.style.linestyle.width = 3
    linestring.style.linestyle.color = simplekml.Color.red


# Save the KML file
kml.save('coordinates.kml')