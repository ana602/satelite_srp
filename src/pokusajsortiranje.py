from config import *
import math
import csv

def polCoordAngle(fiP, lmdP):  
    fi = fiP
    lmd = lmdP
    if lmdP < 180:
        lmd = lmdP
    else:
        lmd = (lmdP-180)*(-1.0)
    return fi, lmd

def pol2car(fi, lmd,r):
    xC = r* math.cos(math.radians(fi))*math.cos(math.radians(lmd))
    yC = r* math.cos(math.radians(fi))*math.sin(math.radians(lmd))
    zC = r* math.sin(math.radians(fi))
    return yC, xC, zC

def CheckSameSat(previous, current):
        if str(previous.split()[2]) == str(current.split()[2]):
            return True
        return False

#saving different satellite positions into different files
VisibleStations = open(satellite_visibility_path, "r")

previous_li = VisibleStations.readline()
lst = []
satKoor = []
lst_sorted = []

for x in range(len(open(satellite_visibility_path, "r").readlines())-1):
    try:
        current_li = VisibleStations.readline()
        h = previous_li.split()
        m = float(h[2])
        satellite = h[2]
        do = open("C:/Users/7Administrator/Desktop/satelite_srp/gen_data/coordinates"+str(satellite)+".txt", "w")#close at the end
        nameStationA = h[0]
        nameStationB = h[1]
        xK = h[5]
        yK = h[6]
        zK = h[7]
        dst = h[8]
        element = [str(nameStationA)+"/"+str(nameStationB),str(yK), str(xK), str(zK), str(dst)]
        lst.append(element)
        if CheckSameSat(previous_li, current_li) is False:
            for line in open(satelites_angle_path, "r").readlines():
                a = line.split()
                if str(a[0]) == str(previous_li.split()[2]):
                    nameSat = a[0]
                    fiPr = float(a[10])
                    lmdPr = float(a[9])
                    fi, lmd = polCoordAngle(fiPr, lmdPr)
                    r = 6372000.0 
                    yC, xC, zC = pol2car(fi, lmd, r)
                
            satKoor.append(str(nameSat)+";"+str(yC)+";"+str(xC)+";"+str(zC)+ "\n")#satKoor.append(str(nameSat)+","+str(yC)+","+str(xC)+","+str(zC)+","+"opis"+ "\n")
            do = open("C:/Users/7Administrator/Desktop/satelite_srp/gen_data/sortirano/coordinates_sort"+str(satellite)+".csv", "w")#close at the end
            do.writelines(satKoor)
            lst_sorted = sorted(lst, key = lambda x: float(x[4]))
            wr = csv.writer(do)
            wr.writerows(lst_sorted)
            #do.writelines(lst)
            do.close()
            lst = []
            satKoor = []
            lst_sorted = []


    except ValueError:
        l=0
    previous_li = current_li



a = [1, 12, 5, 8, 6, 5]
b = [8, 44, 62, 9, 4]
c = [3, 2, 5, 88, 6]
d = [6, 20, 8,5]

lst = []
lst.append(a)
lst.append(b)
lst.append(c)
lst.append(d)

print(lst)

print(sorted(lst, key= lambda x: int(x[1])))

#lst_sorted = sorted(lst, key = lambda x: int(x[4]))