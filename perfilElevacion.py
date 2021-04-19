import simplejson
import urllib
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from math import radians, sin, cos, acos
import pandas as pd

"""
    ELEVATION_BASE_URL: str
        URL para usar la Elevation API
    API_KEY:str
        llave de la API

"""
ELEVATION_BASE_URL = 'https://maps.google.com/maps/api/elevation/json'
API_KEY = ''

def elevacion(lat1, lon1, lat2, lon2, samples, sensor, **elvtn_args):
    """elevacion obtiene los valores de la API
        Params
        ------
            lat1:str
                latitud inicial
            lon1:str
                longitud inicial
            lat2:str
                latitud final
            lon2:str
                longitud final
            samples:str
                numero de muestras
    """
    #crea una cadena con las coordenadas
    path = lat1 + "," + lon1 + "|" + lat2 + "," + lon2
    elvtn_args.update({
        'path': path,
        'samples': samples,
        'sensor': sensor
    })
    
    #genera la cadena completa para el URL
    url = ELEVATION_BASE_URL + '?' + urllib.parse.urlencode(elvtn_args) + '&key=' + API_KEY
    
    #obten los datos en formato JSON
    response = simplejson.load(urllib.request.urlopen(url))
    
    #obten la distancia entre las coordendas
    dist = getDistancia(float(lat1), float(lon1), float(lat2), float(lon2))
    
    #genera un espacio lineal de 0 a dist con el mismo espaciado del numero de muestras
    muestrasDist = np.linspace(0,dist,int(samples))
    
    elevationArray = []
    
    #manda a un arreglo unicamente los datos de elevacion
    for resultset in response['results']:
      elevationArray.append(resultset['elevation'])
    
    #convierte el arreglo a np.arrat para poder aplicarle la mascara que obtiene los picos
    elevationArray = np.array(elevationArray)
    
    #obtiene los picos con un espaciado de 20 muestras
    peaks, _ = signal.find_peaks(elevationArray, distance = float(samples)/20)
    
    #agrega a los picos el primer y el ultimo dato del arreglo de elevacion
    peaks = np.concatenate(([0], peaks, [np.shape(elevationArray)[-1]-1]))
    
    #grafica todas las muestras
    plt.plot(muestrasDist, elevationArray)
    #grafica los picos
    plt.plot(peaks * (dist/float(samples)), elevationArray[peaks], "x")
    plt.show()
    
    #exporta los datos a un CSV
    exportaCSV(peaks, muestrasDist, elevationArray)
    
def exportaCSV(picos, distancia, elevacion):
    """exportaCSV genera un archivo CSV de los datos mas relevantes
        Params
        ------
            picos:[]
                mascara para filtrar los datos de elevacion
            distancia:np.linspace
                espacio lineal con las muestras de distancia
            elevacion:np.array
                contiene todos los datos de elevacion
    """
    
    #aplica la mascara picos para obtener unicamente los resultados relevantes
    filaElevacion = elevacion[picos]
    filaDistancia = distancia[picos]
    
    #genera encabezados y las filas del CSV
    df = pd.DataFrame({"distancia" : filaDistancia, "elevacion" : filaElevacion})
    
    #exporta como csv
    df.to_csv("test.csv", index=False)
    
def getDistancia(lat1, lon1, lat2, lon2):
    """getDistancia obtiene la distancia entre dos coordenadas
        Params
        ------
            Params
        ------
            lat1:str
                latitud inicial
            lon1:str
                longitud inicial
            lat2:str
                latitud final
            lon2:str
                longitud final
        Return
        ------
            dist:float
                distancia en metros de un punto a otro
    """
    
    #convierte los datos primero a float y despues a radianes
    slat = radians(float(lat1))
    slon = radians(float(lon1))
    elat = radians(float(lat2))
    elon = radians(float(lon2))
    
    #obtiene la distancia total considerando el radio de la Tierra
    dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
    print("La distancia es %.2fkm." % dist)
    
    return dist*1000

def main():
    lat1, lon1, lat2, lon2 = "19.362996", "-99.216594", "19.3700458", "-99.2660732"
    samples = "400"
    sensor="false"
    elevacion(lat1, lon1, lat2, lon2, samples, sensor)
    

if __name__ == "__main__":
    main()