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

def checkSameSatellite(previous, current):
    if float(previous.split()[0]) == float(current.split()[0]):
        return True
    return False
    
def compare_angles(previous_l, current_l, angle):
    if float(previous_l.split()[4]) < 180 and float(current_l.split()[4]) > 180:
        if 180-float(previous_l.split()[4]) < float(current_l.split()[4]) - 180:
            previous_l = previous_l.rstrip('\n')
            previous_l = previous_l + "   midnight"
            previous_l = previous_l + '\n'
            #print(previous_l)
            angle.write(previous_l)
            return True
        else:
            current_l = current_l.rstrip('\n')
            current_l = current_l + "   midnight"
            current_l = current_l + '\n'
            #print(current_l)
            angle.write(current_l)
            return True
    elif float(previous_l.split()[4]) > 300 and float(current_l.split()[4]) < 300:
        if 360-float(previous_l.split()[4]) < float(current_l.split()[4]):
            previous_l = previous_l.rstrip('\n')
            previous_l=previous_l + "   noon"
            previous_l=previous_l + '\n'
            #print(previous_l)
            angle.write(previous_l)
            return True
        else:
            current_l = current_l.rstrip('\n')
            current_l = current_l + "   noon"
            current_l = current_l + '\n'
            #print(current_l)
            angle.write(current_l)
            return True


# Function to calculate cos 
# value of angle c 
def cal_cos(n): 
  
    cosval = 0
  
    # Converting degrees to radian 
    n = math.radians(n)
 
    cosval = math.cos(n) 
    #format(cosval, '.4f')
  
    return cosval
  
# Function to find third side 
def third_side(a, b, alfa): 
    angle = cal_cos(alfa) 
    return math.sqrt((a * a) + (b * b) - 2 * a * b * angle) 
  
 # Valuae


for x in range(len(open(satelites_b14_path, "r").readlines())-1):
    current_line=sateliti14.readline()
    if checkSameSatellite(previous_line, current_line):
        if compare_angles(previous_line, current_line, angle):
            counter14_0 += 1
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

stations=open(mgex_path, "r")
stationsFiLa=open(satelites_stationsFiLa_path, "w")

with open(mgex_path) as myfile:
    head= [next(myfile) for x in range(4)]
linija="NUM"+"  "+"STATION"+"     "+"FI"+"        "+"LAMBDA"+"         "+"r"+'\n'
stationsFiLa.writelines(head)
stationsFiLa.write(linija)

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

        stationsFiLa.write(red[0]+" "+red[1]+" "+str(FiSt)+" "+str(LambdaSt)+" "+str(rSt)+'\n')

stationsFiLa.close()

stationsFiLa=open(satelites_stationsFiLa_path)
satellitsWithIn14=open(satelites_angle_path)
angle=open(satelites_angle_path, "r")

distancies14=open(satelites_distance14_path, "w")


#header= "Station"+"  "+"Satellit"+"  "+"Fi_Satellite"+"  "+"Lambda_Satellite"+" "+"Fi_Station"+"  "+"Lambda Station"+"  "+"Distance"+" "+"Azimuth"+" "+"Azimuth Reverse"+" "+"Sredisnji kut" '\n'
distancies14.write("%-11s %-10s %-12s %-16s %-22s %-22s %-22s %-22s %-22s %-22s %-22s\n" % ("Station", "Satellite", "FI_Satellite", "Lamda_Satellite", "Fi_Station", "Lambda_Station", "Distance", "Azimuth", "Azimuth Reverse", "Central angle", "Third side"))


import pygeodesy as geo

temp = stationsFiLa.readlines()

for i in angle.readlines():
    a=i.split()
    #print(i+"\n")   
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


            rednew=[j[0:2], name, FiSa, LambdaSa, FiSt, LambdaSt, distance, azimuth, rev_azimuth, tr_side]
            #distancies14.write(str(rednew)+'\n')
            distancies14.write("%-5s %-5s %-10s %-12f %-16f %-22s %-22s %-22s %-22s %-22s %-22s %-22s\n" % (j[0], j[1], name, FiSa, LambdaSa, str(FiSt), str(LambdaSt), str(distance), str(azimuth), str(rev_azimuth), str(alfa), str(tr_side)))

        except:
            l=0

            #stationsFiLa.seek(0)


            continue

distancies14.close()




#print(third_side(a, b, c))
#print(cal_cos(c))



           