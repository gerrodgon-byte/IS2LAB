'''
Created on 22 oct. 2023

@author: Gerard(US)
'''
from __future__ import annotations
from dataclasses import dataclass
from typing import List
from math import sin, cos, atan2, sqrt, radians
from statistics import mean

@dataclass(frozen = True, order = True) # Inmutable, comparable
class Coordenadas2D:
    #Propiedades básicas
    latitud: float
    longitud: float

    #Restricciones
    def __post_init__(self) -> None:
        assert -90 <= self.latitud <= 90, "Latitud incorrecta"
        assert -180 <= self.longitud <= 180, "Longitud incorrecta"
    
    
    @staticmethod
    def of(latitud: float, longitud: float) -> Coordenadas2D:
        return Coordenadas2D(latitud, longitud)
    
    @staticmethod
    def parse(cadena: str)-> Coordenadas2D:
        cadena = cadena[1:-1]
        latitud, longitud = cadena.split(",")
        return Coordenadas2D(float(latitud), float(longitud))
    
    # @staticmethod 
    # def center(coordenadas: List[Coordenadas2D]) -> Coordenadas2D:
    #     sumLatitud:float = 0.0
    #     sumLongitud:float = 0.0
    #     coordenadas = [Coordenadas2D(3.4, 7.8), Coordenadas2D(7.4, 3.0), Coordenadas2D(3.0, 7.8)]
    #     for c in coordenadas:
    #         sumLatitud += c.latitud
    #         sumLongitud += c.longitud
    #     n:int= len(coordenadas)
    #     return Coordenadas2D.of(sumLatitud/n, sumLongitud/n)



    @staticmethod 
    def center(coordenadas:List[Coordenadas2D]) -> Coordenadas2D:
        latMed:float = mean(c.latitud for c in coordenadas)
        longMed:float = mean(c.longitud for c in coordenadas)
        return Coordenadas2D.of(latMed, longMed)
    
    #Propiedades derivadas
    def distancia(self:Coordenadas2D, otra:Coordenadas2D) -> float:
        radio_tierra:float = 6373.0
        lat1, long1 = radians(self.latitud), radians(self.longitud)
        lat2, long2 = radians(otra.latitud), radians(otra.longitud)
        a:float = ((sin((lat2 - lat1)/2))**2) + cos(lat2) * cos(lat1) * ((sin((long2 - long1)/2))**2)
        d:float = radio_tierra + 2*atan2((sqrt(a)), (sqrt(1-a)))
        return d 


    def es_cercana(self:Coordenadas2D, otra:Coordenadas2D, d:float) -> bool:
        return self.distancia(otra) <= d
    
    
    def __str__(self) -> str:
        return f"({self.latitud}, {self.longitud})"
    
    
if __name__ == '__main__':
    c: Coordenadas2D = Coordenadas2D(25.4, 98.2)
    print(c)
    c1: Coordenadas2D = Coordenadas2D.parse('10.5, 9.8')
    print(c1)
    
    print(f"La distancia entre {c} y {c1} es: {c.distancia(c1)}")
