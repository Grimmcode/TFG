#from django.test import TestCase


import math
import numpy
from dataprep.clean import clean_lat_long
# Create your tests here.


X =float(input ("\nEnter Degree: "))
Y =float(input ("\nEnter Degree: "))
Z =float(input ("\nEnter Degree: "))


latgor =float(input ("\nEnter Degree: "))
latmor =float(input ("\nEnter Degree: "))
latsor =float(input ("\nEnter Degree: "))
#entradas para grados minutos segundos por separado y convertir a grados
longor=float(input ("\nEnter Degree: "))
lonmor=float(input ("\nEnter Degree: "))
lonsor=float(input ("\nEnter Degree: "))
hor=float(input ("\nEnter Degree: "))



elipsoide="WGS84"
tipo="gms"


elipsoides={
"Hayford":{"a":6378388,"invf":297.0},
"SGR80":{"a":6378137,"invf":298.257222101},
"WGS84":{"a":6378137,"invf":298.257223563}
}


elipsoide=elipsoides.get(elipsoide)




f=(1/elipsoide["invf"])
e2=f*(2-f)



#transformacion=="car2enu":

if tipo=="gms":
    if longor<0:
        lonmor=lonmor*-1
        lonsor=lonsor*-1
    lator=(latgor+latmor/60+latsor/3600)*(math.pi/180)
    lonor=(longor+lonmor/60+lonsor/3600)*(math.pi/180)
if tipo!="gms":
    lator=lator*(math.pi/180)
    lonor=lonor*(math.pi/180)  
#radio de curvatura maximo
n=elipsoide["a"]/(1-e2*math.sin(lator)**2)**(1/2)
#coordenadas Cartesianas
Xo=(n+hor)*math.cos(lator)*math.cos(lonor)
Yo=(n+hor)*math.cos(lator)*math.sin(lonor)
Zo=(n*(1-e2)+hor)*math.sin(lator)

IncX=X-Xo
IncY=Y-Yo
IncZ=Z-Zo

e=-math.sin(lonor)*IncX+math.cos(lonor)*IncY
n=-math.sin(lator)*math.cos(lonor)*IncX-math.sin(lator)*math.sin(lonor)*IncY+math.cos(lator)*IncZ
u=math.cos(lator)*math.cos(lonor)*IncX+math.cos(lator)*math.sin(lonor)*IncY+math.sin(lator)*IncZ

#transformacion=="geo2car":
'''
if long<0:
    lonm=lonm*-1
    lons=lons*-1

lat=(latg+latm/60+lats/3600)*(math.pi/180)
lon=(long+lonm/60+lons/3600)*(math.pi/180)
#lat=clean_lat_long(lat)
#lon=clean_lat_long(lon)
print(lat)
print(lon)
f=(1/elipsoide["invf"])
print(f)
e2=f*(2-f)
n=elipsoide["a"]/(1-e2*math.sin(lat)**2)**(1/2)
cartX=(n+h)*math.cos(lat)*math.cos(lon)
cartY=(n+h)*math.cos(lat)*math.sin(lon)
cartZ=(n*(1-e2)+h)*math.sin(lat)

print(cartX)
print(cartY)
print(cartZ)
'''
#transformacion=="car2geo":
'''
cor1=1
cor2=1
X=lat
print(X)
Y=lon
Z=h
H=0

elipsoide=elipsoides.get(elipsoide)

f=(1/elipsoide["invf"])
print(f)
e2=f*(2-f)
print(e2)
p=math.sqrt(X**2+Y**2)
latt=math.atan(Z/(p*(1-e2)))
per=1e-10
print(per)

while abs(cor1)>1e-10 and abs(cor2)>1e-05:
    #radio de curvatura maximo
    n=elipsoide["a"]/(1-e2*math.sin(latt)**2)**(1/2)
    hn=(Z/math.sin(latt))-n*(1-e2)
    latn=math.atan((Z*(n+hn))/(p*(n*(1-e2)+hn)))
    cor1=latt-latn
    cor2=hn-H
    latt=latn
    H=hn
    
lonn=math.atan2(Y,X)

latt=latt*(180/math.pi)
lonn=lonn*(180/math.pi)
print("-------")
print(latt)
print(lonn)
print(H)
'''