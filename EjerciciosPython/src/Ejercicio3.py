#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    #Lo primero que hacemos es pedir los datos.
    salir1=False
    vector=[]
    sumaNumeros=0
    while not salir1:
        try:
            for i in range(5):
                numero=int(raw_input("Introduce un numero: "))
                vector.append(numero)
                sumaNumeros=float(numero+sumaNumeros)
            break
        except ValueError:
            print "ERROR: no es un numero lo que se ha introducido."
    #Ahora averiguaremos cual es mayor numero de la lista, el menor y luego haremos la media 
    result=float(sumaNumeros/5)
    #NUMERO MAYOR.
    maximo=max(vector)
    minimo=min(vector)
    print "El numero mas grande del vector es: %s" %maximo
    print "El numero mas pequeño del vector es: %s" %minimo
    print "La media de todos los numeros es: "+str(result)