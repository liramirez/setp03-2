
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Nombre    : Lizzie Ramirez
#Fecha     : 19-Mayo-2013
#Actividad : 1 - Busqueda binaria recursiva Lab N°3.2
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funciones
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

def busqueda_binaria_rec(numeros,valor,inicio,largo):

    # i es la posicion de la mitad del arreglo
    i=(inicio+largo)//2
    
    if numeros[i]==valor:
        return True
    else:
        if inicio==largo:
            return False
        
    if numeros[i]< valor:
        return (busqueda_binaria_rec(numeros,valor,i+1,largo))
    else:
        return (busqueda_binaria_rec(numeros,valor,inicio,i-1))
    
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funcion principal
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

def main():

    print("Busqueda binaria recursiva")
    
    valor=input("Ingrese el numero que desea buscar :")

    #con 'eval', obligo a mi variable 'valor' a ser de tipo int
    valor=eval(valor)
    
    #Lista de 20 numeros ordenados de menor a mayor
    numeros=[0,1,8,9,11,13,14,15,20,24,26,36,39,41,45,55,57,63,78,84]
    
    #largo es la cantidad de objetos de la lista
    largo=len(numeros)
    inicio=0

    if (busqueda_binaria_rec(numeros,valor,inicio,largo)):
        print("Se encontro el numero",valor)
    else:
        print("El numero",valor,"no se encuentra")

    return 0
    
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Identificador del main
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':
  main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
