from django.shortcuts import render
import math
#Pudiendo entrar como variables de entorno previamente definidas (ahora mismo estan como variables definidas pero podrian cambiar de valor )
Ksideriac=float(1.00273790935);
Ksideriav=float(0.997269578);
elipsoides={
"Hayford":{"a":6378388,"invf":297.0},
"SGR80":{"a":6378137,"invf":298.257222101},
"WGS84":{"a":6378137,"invf":298.257223563}
}

def Tiempos (request):
    if request.method=="POST":            
        ta=request.POST.get("tiempo1")
        lon1=request.POST.get("longT1")
        lon2=request.POST.get("longT2")
        ET1=request.POST.get("Et1")
        ET2=request.POST.get("Et2")
        Tso=request.POST.get("Tsg0")
        op=request.POST.get("Cambio")
        lon1=float(lon1)
        ta=float(ta)
        lon2=float(lon2)
        Tso=float(Tso)
        if op=="Civil2Siderio":
            #Pasamos el tiempo civil a Greewich
            if lon1<float(0):
                TCG=ta+lon1
            else:
                TCG=ta-lon1   
            #Paso de tiempo civil a tiempo siderio en Greenwich
            Is=TCG*Ksideriac
            Tsg=Tso+Is
            if Tsg>float(24):
                Tsg=Tsg-float(24)
            else:
                Tsg=Tsg
            #Calculo el tiempo Siderio en lugar destino
            if lon2<float(0):
                Tss=Tsg+lon2
            else:
                Tss=Tsg-lon2

            return render(request, "calculate/resultTiempos.html",context={"Tss":Tss})


        elif op=="Civil2Verdadero":
            ta=request.POST.get("tiempo1")
            lon1=request.POST.get("longT1")
            lon2=request.POST.get("longT2")
            ET1=request.POST.get("Et1")
            ET2=request.POST.get("Et2")
            #Pasar de tiempo civil a tiempo verdadero
            if lon1<0:
                Tcv=ta-lon1
            else:
                Tcv:ta+lon1
            #Ecuacion del tiempo
            #Incremento
            AEt=ET2-ET1
            X=(Tcv*AEt)/24
            Et=ET1+X
            #Tiempo verdadero en Greenwich
            if (Tcv-Et)>=12:
                Tvg=Tcv-Et-12
            else:
                Tvg=Tcv-Et+12
            #Calculo del tiempo verdadero en el lugar destino
            if lon2<0:
                Tv2=Tvg-lon2
            else:
                Tv2=Tvg+lon2
            return render(request, "",context={"Tiempo Verdadero":Tv2})   
            
    
        elif op=="Siderio2Verdadero":
            ta=request.POST.get("tiempo1")
            lon1=request.POST.get("longT1")
            lon2=request.POST.get("longT2")
            ET1=request.POST.get("Et1")
            ET2=request.POST.get("Et2")
            Tso=request.POST.get("Tsg0")
            #Pasar de tiempo siderio a tiempo civil
            #Tiempo siderio en Greenwich
            if lon1<0:
                Tsg=ta+lon1
            else:
                Tsg:ta-lon1
            #Paso de tiempo siderio a tiempo civil en Greenwich
            #Calculamos el intervalo siderio
            if Tsg<Tso:
                Is=Tsg-Tso+24
            else:
                Is=Tsg-Tso
            #Timepo civil en Greenwich
            TCG=Is*Ksideriav
            #Pasar de tiempo civil a tiempo verdadero
            #Incremento
            AEt=ET2-ET1
            X=(Tcv*AEt)/24
            Et=ET1+X
            if tvg<0:
               tvg=TCG-Et+12 
            else:
                tvg=TCG-Et-12
            if lon2<0:
               Tv2=tvg-lon2
            else:
                Tv2=tvg+lon2
            return render(request, "",context={"Tiempo Verdadero":Tv2})   
            
            
        elif op=="Sidero2Civil":
            ta=request.POST.get("tiempo1")
            lon1=request.POST.get("longT1")
            lon2=request.POST.get("longT2")
            ET1=request.POST.get("Et1")
            ET2=request.POST.get("Et2")
            Tso=request.POST.get("Tsg0")
            #Pasar de tiempo siderio a tiempo civil
            #Tiempo siderio en Greenwich
            if lon1<0:
                Tsg=ta+lon1
            else:
                Tsg:ta-lon1
            #Paso de tiempo siderio a tiempo civil en Greenwich
            #Calculamos el intervalo siderio
            if Tsg<Tso:
                Is=Tsg-Tso+24
            else:
                Is=Tsg-Tso
            TCG=Is/Ksideriac
            #TIempo civil en greenwich
            #tiempo civil en el destino
            if lon2<0:
               Tc2=TCG-lon2
            else:
                Tc2=TCG+lon2
            return render(request, "",context={"Tiempo Civil":Tc2}) 
        
        
        elif op=="Verdadero2Civil":
            ta=request.POST.get("tiempo1")
            lon1=request.POST.get("longT1")
            lon2=request.POST.get("longT2")
            ET1=request.POST.get("Et1")
            ET2=request.POST.get("Et2")
            #calculo tiempo en greenwich
            if lon1<0:
                Tvg=ta+lon1
            else:
                Tvg:ta-lon1
            #Interpolar 
            Tvg1=Tvg+12
            if Tvg1>=24:
                Tvg1=Tvg1-24
            else:
                Tvg1=Tvg1
            #Diferencia
            AEt=ET2-ET1
            X=(Tvg1*AEt)/24
            Et=ET1+X
            #T.greenwich
            TCG=tvg+Et+12;
            if TCG>24:
                TCG=TCG-24 
            else:
                TCG=TCG
            #T civil destino
            if lon2<0:
               Tc2=TCG-lon2
            else:
                Tc2=TCG+lon2
            return render(request, "",context={"Tiempo Civil":Tc2}) 
            
            
        elif op=="Verdadero2Siderio":
            ta=request.POST.get("tiempo1")
            lon1=request.POST.get("longT1")
            lon2=request.POST.get("longT2")
            ET1=request.POST.get("Et1")
            ET2=request.POST.get("Et2")
            Tso=request.POST.get("Tsg0")
            #calculo tiempo en greenwich
            if lon1<0:
                Tvg=ta+lon1
            else:
                Tvg:ta-lon1
            #Interpolar 
            Tvg1=Tvg+12
            if Tvg1>=24:
                Tvg1=Tvg1-24
            else:
                Tvg1=Tvg1
            #Diferencia
            AEt=ET2-ET1
            X=(Tvg1*AEt)/24
            Et=ET1+X
            #T.greenwich
            TCG=tvg+Et+12;
            if TCG>24:
                TCG=TCG-24 
            else:
                TCG=TCG
            Is=TCG*Ksideriac
            #T Siderio destino
            if lon2<0:
               Ts2=TCG-lon2
            else:
                Ts2=TCG+lon2
            return render(request, "",context={"Tiempo Siderio":Ts2}) 
    return render(request, 'calculate/Tiempos.html')
    
    
    
    
    
    
def transformacionCoordenadas(request):
    if request.method=="POST":          
        transformacion=request.POST.get("transformacion")
        elipsoide=request.POST.get("elipsoide")
        lon=request.POST.get("lon")
        lat=request.POST.get("lat")
        latg=request.POST.get("latg")
        latm=request.POST.get("latm")
        lats=request.POST.get("lats")
        long=request.POST.get("long")
        lonm=request.POST.get("lonm")
        lons=request.POST.get("lons")
        tipo=request.POST.get("tipo")
        h=request.POST.get("altura")
        #coordenadas origen local
        lonor=request.POST.get("lonor")
        lator=request.POST.get("lator")
        hor=request.POST.get("hor")
        latgor=request.POST.get("latg")
        latmor=request.POST.get("latm")
        latsor=request.POST.get("lats")
        longor=request.POST.get("long")
        lonmor=request.POST.get("lonm")
        lonsor=request.POST.get("lons")
        elipsoide=elipsoides.get(elipsoide)
        #calculamos constantes del elipsoide 
        f=(1/elipsoide["invf"])
        e2=f*(2-f)
        
        if transformacion=="geo2car":
            if tipo=="gms":
                if long<0:
                    lonm=lonm*-1
                    lons=lons*-1
                lat=(latg+latm/60+lats/3600)*(math.pi/180)
                lon=(long+lonm/60+lons/3600)*(math.pi/180)
            if tipo!="gms":
                lat=lat*(math.pi/180)
                lon=lon*(math.pi/180)
            #radio de curvatura maximo
            n=elipsoide["a"]/(1-e2*math.sin(lat)**2)**(1/2)
            #coordenadas Cartesianas
            cartX=(n+h)*math.cos(lat)*math.cos(lon)
            cartY=(n+h)*math.cos(lat)*math.sin(lon)
            cartZ=(n*(1-e2)+h)*math.sin(lat)
            return render()   
        if transformacion=="car2geo":
            cor1=1
            cor2=1
            X=lat
            Y=lon
            Z=h
            H=0
        
            p=math.sqrt(X^2+Y^2)
            latt=math.atan(Z/(p*(1-e2)))
            
            while cor1>1e-45 and cor2>1e-45:
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
            Hf=H
            return render()    
        if transformacion=="car2enu":
            X=lat
            Y=lon
            Z=h
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
            
        return render()
            
            
            
            
            
            
def home(request):
    if request.method == "POST":
        a = request.POST.get('first')
        op = request.POST.get('operation')
        # print(op)
        b = request.POST.get('second')
        a = int(a)
        b = int(b)
        # print("{} {}".format(a, b))
        z = 0
        if op=='+':
            z = a+b
        elif op=='-':
            z = a-b
        elif op=='*':
            z = a*b
        elif op=='/':
            if b==0:
                z = "Error! Division by zero isn't possible"
            else:
                z = a/b

        return render(request, 'calculate/result.html', context={'z':z})

    return render(request, 'calculate/home.html')


def js(request):
    return render(request, 'calculate/js.html');
