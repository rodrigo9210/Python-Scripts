# -*- coding: utf-8 -*-
"""
Problema 2 - Examen 2

@author: Rodrigo Arce
"""

from os import listdir, rename
import time
from os.path import isfile, join, getmtime
from datetime import datetime

def leerArchivos(ruta):
    """leerArchivos obtiene la ruta completa de todos los archivos de una carpeta
        Params
        ------
            ruta:str
                carpeta de archivos
        Return
        ------
            archivos:[]
                arreglo con el nombre de los archivos de la ruta
    """
    archivos = []
    for f in listdir(ruta):
        ruta_completa = join(ruta, f)
        if isfile(ruta_completa):
            archivos.append(ruta_completa)
    return archivos

def obtenFechas(archivos):
    """obtenFechas obtiene las fechas diferentes de una lista de archivos
        Params
        ------
            archivos:[]
                arreglo con nombres de archivos
        Return
        ------
            fechas:[]
                arreglo ordenado con fechas no repetidas
    """
    fechas = []
    for i in archivos:
        fecha = obtenFecha(i)
        if fecha not in fechas:
            fechas.append(fecha)
        
    fechas.sort()
                
    return fechas

def obtenFecha(archivo):
    """obtenFecha obtiene la fecha de un archivo
        Params
        ------
            archivo:str
                ruta de un archivo
        Return
        ------
            fecha:[]
                regresa la fecha de un archivo (MM - DD - YYYY)
    """
    try:
        fecha = datetime.strptime(time.ctime(getmtime(archivo)), "%a %b %d %H:%M:%S %Y").date()
    except FileNotFoundError:
            print("no fecha")
    return fecha

def nombraArchivos(archivos, fechas, ruta):
    """nombraArchivos renombra todos los archivos de una carpeta
        Params
        ------
            archivos:[]
                arreglo con nombres de archivos
            fechas:[]
                arreglo con las fechas no repetidas de la lista de archivos
            ruta:str
                carpeta de archivos
        Return
        ------
    """
    contador_ams = 0
    contador_ber = 0
    contador_vie = 0
    contador_bar = 0
    contador_par = 0
    for i in archivos:
        fecha = obtenFecha(i)
        ciudad = obtenCiudad(fecha, fechas)
        if ciudad == 'ams':
            contador_ams += 1
            nombre = generaNombre(ciudad, contador_ams)
        elif ciudad == 'ber':
            contador_ber += 1
            nombre = generaNombre(ciudad, contador_ber)
        elif ciudad == 'vie':
            contador_vie += 1
            nombre = generaNombre(ciudad, contador_vie)
        elif ciudad == 'bar':
            contador_bar += 1
            nombre = generaNombre(ciudad, contador_bar)
        elif ciudad == 'par':
            contador_par += 1
            nombre = generaNombre(ciudad, contador_par)
        nombraArchivo(i, nombre, ruta)
    
def obtenCiudad(fecha, arregloFechas):
    """obtenCiudad con base en una fecha y un arreglo de fechas unicas determina una ciudad
        Params
        ------
            fecha:str
                fecha de creacion de un archivo
            arregloFechas:[]
                arreglo con fechas no repetidas y ordenadas
        Return
        ------
            ciudad:str
                primeras tres letras de una ciudad
    """
    ciudades = ['ams', 'ber', 'vie', 'bar', 'par']
    indice = 0
    
    if fecha in arregloFechas:
        indice = arregloFechas.index(fecha)
    
    ciudad = ciudades[indice]
    
    return ciudad

def generaNombre(ciudad, contador):
    """generaNombre genera el nombre de un archivo con el formato CCC-0000.jpg
        Params
        ------
            ciudad:str
                primeras tres letras de una ciudad
            contador:int
                numero que lleva la cuenta para nombrar diferentes archivos
        Return
        ------
            nombre:[]
                nombre nuevo del archivo
    """
    num = str(contador).zfill(4)
    nombre = ciudad + "-" + num + ".jpg"
    return nombre
    
def nombraArchivo(archivo, nombre, ruta):
    """nombraArchivo renombra un archivo existente
        Params
        ------
            archivo:str
                nombre actual del archivo
            nombre:str
                nuevo nombre del archivo
            ruta:str
                direccion del archivo
        Return
        ------
    """
    try:
        rename(join(ruta, archivo), join(ruta, nombre))
    except OSError:
        print("El archivo: ", nombre, "ya existe")
        
    
    return 0

def main():
    ruta = r'''C:\Users\Rodrigo\Desktop\Examen 2'''
    archivos = leerArchivos(ruta)
    fechas = obtenFechas(archivos)
    nombraArchivos(archivos, fechas, ruta)
    

if __name__ == "__main__":
    main()

