#razvrstavanje po udaljenosti
from config import *

doc = open(satelites_distance14_path, "r")

doc_sorted = open(satelites_distance14_sorted_path, "w")
doc_sorted.write("%-11s %-10s %-12s %-16s %-22s %-22s %-22s %-22s %-22s %-22s\n" % ("Station", "Satellite", "FI_Satellite", "Lamda_Satellite", "Fi_Station", "Lambda_Station", "Distance", "Azimuth", "Azimuth Reverse", "Central angle"))

previous_line = doc.readline()
#current_line = doc.readline()

def checkSameS(previous, current):
        if float(previous.split()[2]) == float(current.split()[2]):
            return True
        return False
        

# def Dist (e):
#     try:
#         dist = e.split()[7]
#         return dist
#     except:
#         l=0

same_satellite = []#creat an empty same satellite list for same satellites

for x in doc:
    current_line=doc.readline()
    try:
        if checkSameS (previous_line, current_line):
            same_satellite.append(previous_line) #put previous line in same satellite list, list of only same satellites

        else:
            same_satellite.append(previous_line) #previous line into the same satellite list before sorting the list? 
            sortedSat = same_satellite.sort(x.split()[7])#sort the same satelite list earlier created 
            for line in sortedSat:
                doc_sorted.write("%-5s %-5s %-10s %-12f %-16f %-22s %-22s %-22s %-22s %-22s %-22s\n" % (j[0], j[1], name, FiSa, LambdaSa, str(FiSt), str(LambdaSt), str(distance), str(azimuth), str(rev_azimuth), str(alfa)))
                #appand? "a" will append to the end of the file
                #write sorted same satellite list into file (use loop)
            same_satellite = [] #emty the same satelite list (.clear??) or name = []
            #doc_sorted.write("%-5s %-5s %-10s %-12f %-16f %-22s %-22s %-22s %-22s %-22s %-22s\n" % (j[0], j[1], name, FiSa, LambdaSa, str(FiSt), str(LambdaSt), str(distance), str(azimuth), str(rev_azimuth), str(alfa)))
        previous_line = current_line
    except:
        l=0
doc_sorted.close()