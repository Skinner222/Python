# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    
    salir1=False
    while not salir1:
        try:
            opcion=0
            num=int(raw_input("Introduce un numero: "))
            num2=int(raw_input("Introduce otro numero: "))
            print "Opcion 1. Suma ambos numeros."
            print "Opcion 2. Mostrar quien es el mayor de los dos numeros."
            opcion=(int(raw_input("Elije una de las opciones: ")))
            break
        except ValueError:
            print "ERROR: no es un numero lo que se ha introducido."
    def Menu(num,num2,opcion):
        resultado=0
        if opcion==1:
            resultado = SumaNumeros(num,num2)
            print "La suma de ambos numeros es: "+str(resultado)
        elif opcion==2:
            NumeroMayor(num,num2)
    def SumaNumeros(numero,numero2):
        suma=0
        suma=numero+numero2
        return suma
    def NumeroMayor(numero,numero2):
        if numero>numero2:
            print "El "+str(numero)+" es mas grande que "+str(numero2)
        else:
            print "El "+str(numero2)+" es mas grande que "+str(numero)         
    Menu(num,num2,opcion)