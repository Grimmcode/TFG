from django.shortcuts import render

Ksideriac=float(1.00273790935);
Ksideriav=float(0.997269578);



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
