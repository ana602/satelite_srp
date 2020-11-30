from config import *
import math

def cal_cos(n): 
    cosval = 0
    # Converting degrees to radian 
    n = math.radians(n)
    cosval = math.cos(n)
    return cosval

# Function to find third side 
def third_side(a, b, alfa): 
    angle = cal_cos(alfa) 
    return math.sqrt((a * a) + (b * b) - 2 * a * b * angle)

#Function that calculates the angel wich determenates wethwe it is seen or not
def AngleVidljivost (Ra, trd_s, cent_angl):
    angleVidljivost = math.degrees(math.asin(Ra*(math.sin(math.radians(cent_angl)))/trd_s))
    return angleVidljivost

#distance_14 s dodatkom xyz koordinata

stationFiLaXYZ = open(satelites_stationsFiLaXYZ_path, "r")
angle = open(satelites_angle_path, "r")

distance14XYZ = open(satelites_distance14XYZ_path, "w")

distance14XYZ.write("%-11s %-10s %-12s %-16s %-22s %-22s %-22s %-22s %-22s %-22s %-22s %-22s %-22s %-22s\n" % ("Station", "Satellite", "FI_Satellite", "Lamda_Satellite", "Fi_Station", "Lambda_Station", "Distance", "AngleSaStCen", "AngleCenSatSt", "Central angle", "Third side","X", "Y", "Z"))


import pygeodesy as geo

temp = stationFiLaXYZ.readlines()

for i in angle.readlines():
    a = i.split()
    if len(a) == 12:
        FiSa = float(a[10])
        name = a[0]
        if float(a[9]) < 180:
            LambdaSa = float(a[9])
        else:
            LambdaSa = (float(a[9])-180)*(-1.0) 

    for j in temp:
        j = j.split()

        try:
            FiSt= float(j[2])
            LambdaSt= float(j[3])
            rSt= float(j[4])/1000.0

            distance = geo.cosineLaw(FiSa, LambdaSa, FiSt, LambdaSt, rSt)

            #azimuth = geo.bearing(FiSt, LambdaSt, FiSa, LambdaSa)
            #rev_azimuth = geo.bearing(FiSa, LambdaSa, FiSt, LambdaSt)
            alfa = (180*distance)/(rSt*math.pi)

            a = rSt
            b = rSt + 20200.0

            tr_side = third_side(a, b, alfa)

            AngleSaStCen = AngleVidljivost(b, tr_side, alfa)
            angleCenSatSt = 180.0 - AngleSaStCen - alfa

            xKoor = j[5]
            yKoor = j[6]
            zKoor = j[7]

            distance14XYZ.write("%-5s %-5s %-10s %-12f %-16f %-22s %-22s %-22s %-22s %-22s %-22s %-22s %-22s %-22s %-22s\n" % (j[0], j[1], name, FiSa, LambdaSa, str(FiSt), str(LambdaSt), str(distance), str(AngleSaStCen), str(angleCenSatSt), str(alfa), str(tr_side), str(xKoor), str(yKoor), str(zKoor)))
        except:
            l=0

            continue

angle.close()
distance14XYZ.close()
stationFiLaXYZ.close()


#only stations satellite can see
f = open(satelites_distance14XYZ_path, "r")
visibility = open(satellite_visibility_path, "w")
visibility.write("%-16s %-10s %-15s %-18s %-22s %-22s %-22s\n" % ("Station", "Satellite","Fi_Satellite", "Lambda_Satellite", "X", "Y", "Z"))

for line in f:
    a = line.split()
    try: 
        if float(a[12]) >= 90:
            #a,b,c,d,e,f,g,h,i,j = a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[10], a[11], a[12], a[13], a[14]
            visibility.write("%-5s %-10s %-10s %-15s %-18s %-22s %-22s %-22s\n" % (a[0], a[1], a[2], a[3], a[4], a[12], a[13], a[14])) #with or without str
    except:
        l =0 

f.close()
visibility.close()


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



#saving different satellite positions into different files
VisibleStations = open(satellite_visibility_path, "r")

def CheckSameSat(previous, current):
        if str(previous.split()[2]) == str(current.split()[2]):
            return True
        return False


previous_li = VisibleStations.readline()
lst = []
satKoor = []

for x in range(len(open(satellite_visibility_path, "r").readlines())-1):
    try:
        current_li = VisibleStations.readline()
        h = previous_li.split()
        m = float(h[2])
        satellite = h[2]
        do = open("C:/Users/7Administrator/Desktop/satelite_srp/gen_data/coordinates"+str(satellite)+".txt", "w")#close at the end
        nameStationA = h[0]
        nameStationB = h[1]
        xK = h[3]
        yK = h[4]
        zK = h[5]
        #if satellit == h[2] izracunaj koordinate i stavi ih u listu (vadi iz tyt angels gdje se svi sateliti pojavljuju samo jednom!!)
        #put the coordinates of the satellite in a list
        lst.append(str(nameStationA)+"/"+str(nameStationB)+";"+str(yK)+";"+str(xK)+";"+str(zK)+ "\n") #Replace with add to a list  
        if CheckSameSat(previous_li, current_li) is False:
            for line in open(satelites_angle_path, "r").readlines():
                a = line.split()
                if str(a[0]) == str(previous_li.split()[2]):
                    nameSat = a[0]
                    fiPr = float(a[10])
                    lmdPr = float(a[9])
                    fi, lmd = polCoordAngle(fiPr, lmdPr)
                    r = 6372000.0 + 20200000.0
                    yC, xC, zC = pol2car(fi, lmd, r)#kako spremiti zasebno???
                
            satKoor.append(str(nameSat)+";"+str(yC)+";"+str(xC)+";"+str(zC)+ "\n")
            do = open("C:/Users/7Administrator/Desktop/satelite_srp/gen_data/coordinates"+str(satellite)+".txt", "w")#close at the end
            #write coorinates of the satellite in the file 
            do.writelines(satKoor)
            do.writelines(lst)
            #dump list into file with do.writelines()
            do.close()
            lst = []#empty the list
            satKoor = []

            #empti the list with satellites coordinates

    except:
        l=0
    previous_li = current_li





