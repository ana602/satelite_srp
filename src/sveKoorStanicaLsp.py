stations = open("C:\\Users\\7Administrator\\Desktop\\satelite_srp\\input_data\\MGEX.txt","r")

lispKoorStanica = open("C:\\Users\\7Administrator\\Desktop\\satelite_srp\\koordinate_stanica\\lispKoorStanica.txt", "w")

for line in stations:
    red=line.split()
    if len(red) == 5 or len(red) == 6 or len(red) == 9:
        try:
            xKoor = float(red[2]) 
            yKoor = float(red[3])
            zKoor = float(red[4])
            broj = red[0]
            oznaka = red[1]
        except:
            xKoor = float(red[3]) 
            yKoor = float(red[4])
            zKoor = float(red[5])
            broj = red[0]
            oznaka = red[1]
        lispKoorStanica.write(str(broj)+"/"+str(oznaka)+";"+str(yKoor)+";"+str(xKoor)+";"+str(zKoor)+"\n")

stations.close()
lispKoorStanica.close()
