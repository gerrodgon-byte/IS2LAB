from _datetime import date, timedelta

#1. Dado un número real, implemente una función que devuelva su parte fraccionaria



def parte_fraccionaria(compuesto: float) -> float:
    compuesto = float(input("Ingrese un número con decimales: "))
    return compuesto - int(compuesto)
    
#---------------------------------------------------------------------------------------------------------------

#7. Dada una cadena de texto, implemente una función que reemplace todas las vocales por guiones. 

def reemplazar_vocales(cad: str) ->str:
    """
    Esta función sustituye todas las vocales por guiones
    """
    cad = input("Escriba una frase: ")
    res:str = " "
    vocales:str = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    for letra in cad:
        if letra in vocales:
            res+= "-"
        else:
            res = res+letra
    return res

#el operador += se usa así: n=n+2 ---> n+=2

#print(reemplazar_vocales(""))



#------------------------------------------------------------------------------------------------------------------

#11. Dada una lista de números reales, implemente una función que devuelva la suma de sus elementos. 

def suma_lista(lista: list[float])->float:
    """
    Esta función suma todos los números que hay en una lista
    """
    res = 0.0
    for n in lista:
        res += n 
    return res

#print(suma_lista([3.0, 4.0, 7.0]))



#------------------------------------------------------------------------------------------------------------------------

#12. Dada una lista de números reales, implemente una función que calcule su media. 

def media_lista(lista: list[float])->float:
    """
    Esta función hace la media de los números en una lista
    """
    num_elem = len(lista)
    assert num_elem > 0, "La lista no puede estar vacía"
    s = suma_lista(lista)
    return s/num_elem

#print(media_lista([3.0, 4.0, 7.0]))


#--------------------------------------------------------------------------------------------------------------------------

#17. Dada una lista de enteros y un umbral, implemente una función que filtre los elementos mayores que el umbral.

def filtrar_umbral(lista: list[int],umbral:int)->list[int]:
    res: list[int] = []
    for elemento in lista:
        if elemento>umbral:
            res.append(elemento)
    return res

#print(filtrar_umbral([2, 7, 3, 9, 3, 5, 1, 4, 7, 3, 8, 3, 2, 9], 5))
    
#---------------------------------------------------------------------------------------------------------------------------------

#2. Dado un número real y un número entero n, implemente una función que redondee el número a n decimales. 

def redondeo_n_decimales(número: float)-> float:
    #número = float(input("Ingrese el número que quiere aproximar: "))
    n = int(input("Ingrese el número de decimales para el que quiere redondear: "))
    redondeo: float = round(número, n+1)
    return redondeo

#print(redondeo_n_decimales(273.39402))

#-----------------------------------------------------------------------------------------------------------------------------------

def eliminación_espacios(frase: str)->str:
    """
    Esta función toma una cadena de carácteres y elimina todos aquellos que son espacios
    """
    res: str =" "
    espacio: str =" "
    for e in frase:
        if e in espacio:
            res+=""
        else:
            res=res+e 
    return res

#print(eliminación_espacios("No quiero tomar cafe. Porque el cafe quita el sueño. Lo que quiero es tomar te. Pues tomando te me duermo. Y una vez que te tomé. Yo tan suave te encontré. Que todo el tiempo quiero estar. Tomándote, tomándote"))
        
#------------------------------------------------------------------------------------------------------------------------------------

#19. Dado un número entero positivo, implemente una función que devuelva la lista de sus divisores. 

def divisores_de_número(n: int)->list[int]:
    res: list[int]= []
    #lista: list[int]= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
    assert n>0, "n tiene que ser mayor que 0"
    for e in range(1, n+1):
        if n%e == 0:
            res.append(e)
    return res

#print(divisores_de_número(75))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#15. Dada una lista de enteros, implemente una función que devuelva las diferencias entre elementos consecutivos. 

def resta_consecutivos(l:list[int])->list[int]:
    ret: list[int]= []
    for i in range(1, len(l)):
        ret.append(l[i]-l[i-1])
    return ret

#print(resta_consecutivos([1,645,235,86,235,782]))  

#------------------------------------------------------------------------------------------------------------------------------------------

def dias_laborables_entre(f1:date, f2:date, festivos:set[date])->int:
    """Cuenta los días laborables entre dos fechas indicadas"""
    assert f1 <= f2, "la fecha final debe ser posterior a la inicial"
    res: int = 0
    i: date = f1
    while i <= f2:
        if i.weekday() < 5 and i not in festivos:
            res+=1
        i=i+timedelta(days = 1)
    return res 

print(dias_laborables_entre(date(2025,10,8), date(2025,12,19), {date(2025, 12, 6)}))
