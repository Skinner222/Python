#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    #Lo primero es pedir los datos por teclado.
    espacio=0
    
    
    print "USTED DEBE DE INGRESAR LOS SIGUIENTES DATOS."
    
    marca=raw_input("Introduce la marca de su vehículo: ")
    consumo100km=float(raw_input("Consumo del vehículo a los 100 km: "))
    litrosDeposito=int(raw_input("Litros que le ha puesto en el depósito: "))
    velocidad=float(raw_input("Velocidad a la que ha circulado (formato en km/h): "))
    #Primero de todos pasamos la velocidad a metrso por segundo.
    result2=float((velocidad*1000)/3600)
    #Preguntamos si el consumo es cero ya que si lo es el coche no se mueve.
    if(consumo100km==0):
        print "ERROR: EL COCHE NO SE HA MOVIDO."
    else:
        #Dividimos los litros entre el consumo ya que el resultado seran el espacio.
       result1=float(litrosDeposito/consumo100km)
    #Así averguamos el espacio total que puede recorrer el vehículo.
    espacio=float((result1*100)*1000)
    #Con la formula e=v/t averguaremos el tiempo en horas las cuales luego las pasamos a minutos.
    tiempo=float(espacio/velocidad)
    #El tiempo que esta en horas hay que pasarlo a minutos.
    result3=float(tiempo/60)
    print "Hola tiempo final: "+str(result3)
    
    