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
            print "Opcion 3. Mostrar quien es el menor de los dos numeros."
            print "Opcion 4. Salir."
            opcion=(int(raw_input("Elije una de las opciones: ")))
            break
        except ValueError:
            print "ERROR: no es un numero lo que se ha introducido."
    
    
    
    def Menu(num,num2,opcion):
        salir=False
        
        while not salir:
            
            if opcion==1: 
                SumaNumeros(num,num2)
                print '\n'
            elif opcion==2:
                NumeroMayor(num,num2)
                print '\n'
            elif opcion==3:
                NumeroMenor(num,num2)
                print '\n'
            elif opcion==4:
                salir=True
                
                
     #Esta va a ser la suma de los dos numeros.       
    def SumaNumeros(num,num2):
        suma=0
        suma=num+num2
        print "El resultado de la suma es: "+str(suma)
    def NumeroMayor(num,num2):
        if num>num2:
            print "El numero mas grande es: "+str(num)
        else:
            print "El numero mas grande es: "+str(num2)
            
    def NumeroMenor(num,num2):
        if num<num2:
            print "El numero mas pequeño es: "+str(num)
        else:
            print "El numero mas pequeño es: "+str(num2)
            
            
    Menu(num,num2,opcion)