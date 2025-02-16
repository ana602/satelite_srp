from config import *

print(satelite_data_path)

##saving satelites that have beta between -14 and 14
f=open(satelite_data_path, "r")
sateliti14=open(satelites_b14_path, "w")
counter14=0 ##counter for how many satelites there are that are with beta between -2 and 2


for line in f:
    a=line.split()
    if len(a)==11:
        if float(a[2])>=-14 and float(a[2])<=14:
            counter14 += 1
            sateliti14.write(line)

sateliti14.close()

##listing satelites that are closest to 0 and 180 (beta between -14 and 14)
sateliti14=open(satelites_b14_path, "r")

##file where it saves
angle=open(satelites_angle_path, "w")

previous_line=sateliti14.readline()

#counter for how many times satelit passes 0 and 180 wit beta between -14 and 14
counter14_0=0 
#counter naming of the satellites
cnt = 0

def checkSameSatellite(previous, current):
    # print("previous")
    # print(previous.split())
    # print("current")
    # print(current.split())
    if float(previous.split()[0]) == float(current.split()[0]):
        return True
    return False
    
def compare_angles(previous_l, current_l, angle, counter=0):
    if float(previous_l.split()[4]) < 180 and float(current_l.split()[4]) > 180:
        if 180-float(previous_l.split()[4]) < float(current_l.split()[4]) - 180:
            previous_l1 = previous_l.split()
            previous_l1[0] = previous_l1[0] + "_"+ str(counter)
            previous_l1.append("midnight")
            # previous_l = previous_l.rstrip('\n')
            # previous_l = previous_l + "   midnight"
            # previous_l = previous_l + '\n'
            #print(previous_l)
            a, b, c, d, e, f, g, h, i, j, k, l = previous_l1[0], previous_l1[1], previous_l1[2], previous_l1[3], previous_l1[4], previous_l1[5], previous_l1[6], previous_l1[7], previous_l1[8], previous_l1[9], previous_l1[10], previous_l1[11]
            angle.write("%-5s %-20s %-7s %-7s %-7s %-7s %-5s %-5s %-9s %-7s %-7s %-10s\n" % (previous_l1[0], previous_l1[1], previous_l1[2], previous_l1[3], previous_l1[4], previous_l1[5], previous_l1[6], previous_l1[7], previous_l1[8], previous_l1[9], previous_l1[10], previous_l1[11]))
            #angle.write(str(previous_l1))
            return True
        else:
            current_l1 = current_l.split()
            current_l1[0] = current_l1[0] + "_"+ str(counter)
            current_l1.append("midnight")
            # current_l = current_l.rstrip('\n')
            # current_l = current_l + "   midnight"
            # current_l = current_l + '\n'
            #print(current_l)
            #angle.write(str(current_l1))
            a, b, c, d, e, f, g, h, i, j, k, l = current_l1[0], current_l1[1], current_l1[2], current_l1[3], current_l1[4], current_l1[5], current_l1[6], current_l1[7], current_l1[8], current_l1[9], current_l1[10], current_l1[11]
            angle.write("%-5s %-20s %-7s %-7s %-7s %-7s %-5s %-5s %-9s %-7s %-7s %-10s\n" % (current_l1[0], current_l1[1], current_l1[2], current_l1[3], current_l1[4], current_l1[5], current_l1[6], current_l1[7], current_l1[8], current_l1[9], current_l1[10], current_l1[11]))
            return True
    elif float(previous_l.split()[4]) > 300 and float(current_l.split()[4]) < 300:
        if 360-float(previous_l.split()[4]) < float(current_l.split()[4]):
            previous_l2 = previous_l.split()
            previous_l2[0] = previous_l2[0] +"_"+ str(counter)
            previous_l2.append("noon")
            # previous_l = previous_l.rstrip('\n')
            # previous_l=previous_l + "   noon"
            # previous_l=previous_l + '\n'
            #print(previous_l)
            a, b, c, d, e, f, g, h, i, j, k, l = previous_l2[0], previous_l2[1], previous_l2[2], previous_l2[3], previous_l2[4], previous_l2[5], previous_l2[6], previous_l2[7], previous_l2[8], previous_l2[9],previous_l2[10], previous_l2[11]
            angle.write("%-5s %-20s %-7s %-7s %-7s %-7s %-5s %-5s %-9s %-7s %-7s %-10s\n" % (previous_l2[0], previous_l2[1], previous_l2[2], previous_l2[3], previous_l2[4], previous_l2[5], previous_l2[6], previous_l2[7], previous_l2[8], previous_l2[9],previous_l2[10], previous_l2[11]))
            #angle.write(str(previous_l2))
            return True
        else:
            current_l2 = current_l.split()
            current_l2[0] = current_l2[0] + "_"+ str(counter)
            current_l2.append("noon")
            # current_l = current_l.rstrip('\n')
            # current_l = current_l + "   noon"
            # current_l = current_l + '\n'
            #print(current_l)
            a, b, c, d, e, f, g, h, i, j, k, l = current_l2[0], current_l2[1], current_l2[2], current_l2[3], current_l2[4], current_l2[5], current_l2[6], current_l2[7], current_l2[8], current_l2[9], current_l2[10], current_l2[11]
            angle.write("%-5s %-20s %-7s %-7s %-7s %-7s %-5s %-5s %-9s %-7s %-7s %-10s\n" % (current_l2[0], current_l2[1], current_l2[2], current_l2[3], current_l2[4], current_l2[5], current_l2[6], current_l2[7], current_l2[8], current_l2[9], current_l2[10], current_l2[11]))
            #angle.write(str(current_l2))
            return True
    else:
        return False

t_cnt = 1
for x in range(len(open(satelites_b14_path, "r").readlines())-1):
    current_line=sateliti14.readline()
    if checkSameSatellite(previous_line, current_line):
        if compare_angles(previous_line, current_line, angle, t_cnt):
            counter14_0 += 1
            t_cnt += 1
    else:
        t_cnt = 1
    previous_line=current_line

angle.close()

f.seek(0)

##saving satelates with beta between -2 and 2
sateliti2=open(satelites_2_path, "w")
counter2=0 ##counter for how many satelites there are that are with beta between -2 and 2

for line in f:
    a=line.split()
    if len(a)==11:
        if float(a[2])>=-2 and float(a[2])<=2:
            counter2 += 1
            sateliti2.write(line)

sateliti2.close()
##listing satelites that are closest to 0/180 with beta between -2 and 2
sateliti2=open(satelites_2_path, "r")
##file where it saves 
angle2=open(satelites_angle2_path, "w")

#counter for how many times satelit passes 0 and 180 wit beta between -2 and 2
counter2_0=0

previous_line=sateliti2.readline()

for x in range(len(open(satelites_2_path, "r").readlines())-1):
    current_line=sateliti2.readline()
    if checkSameSatellite(previous_line, current_line):
        if compare_angles(previous_line, current_line, angle2):
            counter2_0 += 1
    previous_line=current_line

angle2.close()

#caclulating fi. lambda coordinates of stations
import math

# Function to calculate cos 
# value of angle c 
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

stations = open(mgex_path, "r")
stationsFiLa = open(satelites_stationsFiLa_path, "w")
stationsFiLaXYZ = open(satelites_stationsFiLaXYZ_path, "w")

with open(mgex_path) as myfile:
    head= [next(myfile) for x in range(4)]
#linija="NUM"+"  "+"STATION"+"     "+"FI"+"        "+"LAMBDA"+"         "+"r"+'\n'

stationsFiLa.writelines(head)
stationsFiLa.write("%-8s %-8s %-22s %-22s %-20s \n" % ("NUM", "STATION", "FI_Station", "Lamda_Station", "r_station"))

stationsFiLaXYZ.writelines(head)
stationsFiLaXYZ.write("%-8s %-8s %-22s %-22s %-20s %-22s %-22s %-22s \n" % ("NUM", "STATION", "FI_Station", "Lamda_Station", "r_station", "X", "Y", "Z"))

for line in stations:
    red=line.split()
    if len(red) == 5 or len(red) == 6 or len(red) == 9:
        try:
            xKoor = float(red[2]) 
            yKoor = float(red[3])
            zKoor = float(red[4])
        except:
            xKoor = float(red[3]) 
            yKoor = float(red[4])
            zKoor = float(red[5])
        #print(xKoor,yKoor,zKoor)


        LambdaSt= math.degrees(math.atan2(yKoor,xKoor))
        FiSt= math.degrees(math.atan2(zKoor,(math.sqrt((xKoor**2)+(yKoor**2)))))
        rSt= math.sqrt((xKoor**2)+(yKoor**2)+(zKoor**2))

        #stationsFiLa.write(red[0]+" "+red[1]+" "+str(FiSt)+" "+str(LambdaSt)+" "+str(rSt)+'\n')
        stationsFiLa.write("%-8s %-8s %-22s %-22s %-20s\n" % (red[0], red[1], str(FiSt), str(LambdaSt), str(rSt)))
        stationsFiLaXYZ.write("%-8s %-8s %-22s %-22s %-20s %-22s %-22s %-22s \n" % (red[0], red[1], str(FiSt), str(LambdaSt), str(rSt), str(xKoor), str(yKoor), str(zKoor)))

stationsFiLa.close()
stationsFiLaXYZ.close()

stationsFiLa=open(satelites_stationsFiLa_path)
angle=open(satelites_angle_path, "r")

distancies14=open(satelites_distance14_path, "w")

distancies14.write("%-11s %-10s %-12s %-16s %-22s %-22s %-22s %-22s %-22s %-22s %-22s\n" % ("Station", "Satellite", "FI_Satellite", "Lamda_Satellite", "Fi_Station", "Lambda_Station", "Distance", "Azimuth", "Azimuth Reverse", "Central angle", "Third side"))#add titels for angels


import pygeodesy as geo

temp = stationsFiLa.readlines()

for i in angle.readlines():
    a=i.split()   
    if len(a) == 12:
        FiSa = float(a[10])
        name=a[0]
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

            azimuth = geo.bearing(FiSt, LambdaSt, FiSa, LambdaSa)
            rev_azimuth = geo.bearing(FiSa, LambdaSa, FiSt, LambdaSt)
            alfa = (180*distance)/(rSt*math.pi)

            a = rSt
            b = rSt + 20200.0

            tr_side = third_side(a, b, alfa)

            #izracun kuta
            #AngleSaStCen = AngleVidljivost (b, tr_side, alfa)
            #angleCenSatSt = 180 - AngleSaStCen - alfa

            rednew=[j[0:2], name, FiSa, LambdaSa, FiSt, LambdaSt, distance, azimuth, rev_azimuth, tr_side]
            #distancies14.write(str(rednew)+'\n')
            distancies14.write("%-5s %-5s %-10s %-12f %-16f %-22s %-22s %-22s %-22s %-22s %-22s %-22s\n" % (j[0], j[1], name, FiSa, LambdaSa, str(FiSt), str(LambdaSt), str(distance), str(azimuth), str(rev_azimuth), str(alfa), str(tr_side)))#add names for angels

        except:
            l=0


            continue

distancies14.close()
angle.close()




