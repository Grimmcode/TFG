#from django.test import TestCase


import math
import numpy
from dataprep.clean import clean_lat_long
# Create your tests here.

latg =float(input ("\nEnter Degree: "))
latm =float(input ("\nEnter Degree: "))
lats =float(input ("\nEnter Degree: "))
#entradas para grados minutos segundos por separado y convertir a grados
long=float(input ("\nEnter Degree: "))
lonm=float(input ("\nEnter Degree: "))
lons=float(input ("\nEnter Degree: "))
print(long)
if long<0:
    lonm=lonm*-1
    lons=lons*-1
h=float(input ("\nEnter Degree: "))
lat=(latg+latm/60+lats/3600)*(math.pi/180)
lon=(long+lonm/60+lons/3600)*(math.pi/180)
elipsoide="WGS84"

elipsoides={
"Hayford":{"a":6378388,"invf":297.0},
"SGR80":{"a":6378137,"invf":298.257222101},
"WGS84":{"a":6378137,"invf":298.257223563}
}


elipsoide=elipsoides.get(elipsoide)

#transformacion=="geo2car":
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