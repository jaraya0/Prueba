#Autor: Jaime Espinosa Araya

import csv
import datetime

cdate=datetime.date.today()
año_actual=cdate.year
mes_actual=cdate.month
dia_actual=cdate.day
def dia():
    import datetime
    cdate = datetime.date.today()
    dia_actual = cdate.day
    return (str(dia_actual))
def mes():
    import datetime
    cdate = datetime.date.today()
    mes_actual=cdate.month
    return (str(mes_actual))
def año():
    import datetime
    cdate = datetime.date.today()
    año_actual=cdate.year
    return (str(año_actual))

def menu():
    menu = "1. Registrar Reclamo\n2. Listar Reclamos\n3. Respaldar Reclamos\n4. Salir"
    return (menu)

flag = True
print (menu())
rut= []
fecha= []
monto= []
reclamo= []

while flag == True:
    flag_check = True
    while flag_check == True:
        try:
            opt=int(input("Cual es su opción: "))
            if opt not in [1,2,3,4]:
                print("Debes ingresar un número del [1,4]...")
                flag = True
            flag_check = False
        except:
            print("Debes ingresar un número del [1,4]...")
            flag_check = True
    match opt:
        case 1:
            print ("Has escogido [Registrar Reclamo]\n")
            rut.append(input("Ingrese su rut: "))
            flag_check = True
            while flag_check == True:
                try:
                    monto.append(int(input("Ingrese el monto: ")))
                    flag_check = False
                except:
                    print("Debes ingresar un monto en NÚMEROS")
                    flag_check = True
            flag_check = True
            while flag_check == True:
                reclamo_temp=input("Ingrese el reclamo (MÁX 20 CARACTERES): ")
                if len(reclamo_temp) > 20:
                    print ("Porfavor respetar el largo máximo")
                if len (reclamo_temp) < 21:
                    reclamo.append(reclamo_temp)
                    flag_check = False
            fecha.append(dia()+"-"+mes()+"-"+año())
            print (menu())
        case 2:
            if len(reclamo) == 0:
                print ("\nAún no has ingresado nada, prueba con la opción [1] primero\n")
            if len(reclamo) > 0:
                contador = 0
                print ("\nEstos son todos los reclamos:\n")
                while contador<len(reclamo):
                    print (f"Rut: {rut[contador]}\nFecha: {fecha[contador]}\nMonto: {monto[contador]}\nReclamo: {reclamo[contador]}\n")
                    contador+=1
            print(menu())
        case 3:
            fields = ["Estos son todos los reclamos:"]
            with open("Respaldos.csv","w",newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(fields)
                csvwriter.writerow([])
                contador = 0
                while contador < len(reclamo):
                    mini_rut=[[f"Rut: {rut[contador]}"],[f"Fecha: {fecha[contador]}"],[f"Monto: {monto[contador]}"],[f"Reclamo: {reclamo[contador]}"]]
                    csvwriter.writerows(mini_rut)
                    csvwriter.writerow([])
                    contador += 1
            print(menu())
        case 4:
            print ("\nGracias por usar el programa")
            flag = False



