from config import *
import json
from geojson import Feature, Point, FeatureCollection

doc=open(satelites_distance14_path, "r")
colection = []

previous_line=doc.readline()

def CheckSameSat(previous, current):
    if float(previous.split()[2]) == float(current.split()[2]):
        return True
    return False

for x in range(len(open(satelites_distance14_path, "r").readlines())-1):
    try:
        current_line=doc.readline()
        satellite_number = int(previous_line.split()[2])
        f=open("C:/Users/7Administrator/Desktop/satelite_srp/gen_data/coordinates"+str(satellite_number)+".json", "w")#close at the end
        if CheckSameSat(previous_line, current_line):

            my_point = Point((float(previous_line.split()[6]), float(previous_line.split()[5])))
            my_feature = Feature(geometry =my_point, id = previous_line.split()[0:2] )

            colection.append(my_feature)

            my_featurecollection = FeatureCollection(colection)

            json.dump(my_featurecollection, f, indent = 4)
        else:
            colection = []
            f.close()
    except:
        l=0
    previous_line = current_line