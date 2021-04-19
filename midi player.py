import csv
from pysine import sine
from time import sleep

def LeerNotas():
    """LeerNotas Inicia el proceso de lectura de CSV y crea una lista de notas con el formato correcto para su 
                 posterior reproduccion en audio
        Params
        -----
    """
    path  = './' #Para que funcione con los archivos en la misma carpeta

    fname = 'cancion'
    lista_notas = []
    with open( '{}/{}.csv'.format(path,fname) ) as f:
        csvf = csv.reader(f)
        header = next(csvf,None)
        response = ValidarFormato(header)
        if response == "ok":
            for i in csvf:
                lista_notas.append(ConvertirFormato(i))
            ReproduceArchivo(lista_notas)
        else:
            print(response)

def ConvertirFormato(renglon):
    """ConvertirFormato recibe el reglon sin formato para validar que cada dato pueda ser convertido al formato
                        necesario.
        Params
        -----
            renglon
                es el renglon del archivo csv sin formato.
        Return
            nuevo_renglon 
                es el nuevo renglon listo para ser reproducido.
    """
    tipo = type(renglon[0])
    nuevo_renglon = []
    if tipo == str:
        #Formato correcto
        tipo = type(renglon[1])
        if tipo == str:
            #Formato correcto
            tipo = type(renglon[2])
            if tipo != int:
                renglon[2] = VerificarEntero(renglon[2]) #Verifica que se pueda convertir a entero
                if renglon[3] != float:
                    renglon[3] = VerificarFlotante(renglon[3]) #Verifica que se pueda convertir a flotante
                    if renglon[4] == ':' or renglon[4] == '-':
                        nuevo_renglon = [renglon[0],renglon[1],renglon[2],renglon[3],renglon[4]]
                    else:
                        print("Formato de bloque incorrecto")
    return nuevo_renglon

def Frecuencia(octava, nota, accidente):
    """frecuencia obtiene la el valor en Hz dada la octava, nombre de nota y accidente
        Params
        ------
            octava:int
                indica con un entero a que octava (0-8) pertenece la nota             
            nota:str
                indica que tipo de nota es, puede escribirse en ingles o espanol
            accidente:str
                indica si la nota es natural, bemol o sostenida
        Return
        ------
            frec:double
                valor en Hz de la frecuencia
    """
    #1ero se calcula la distancia de la nota respecto a La4
    num_pasos = Pasos(octava, nota, accidente)
    #si no encontro la definicion en el diccionario la frecuencia es cero
    if num_pasos == -100:
        frec = 0
    #Calcula la frecuencia con base en el numero de pasos
    else:
        frec = 440 * pow(pow(2,1/12),num_pasos)
    return frec

def Pasos(octava, nota, accidente):
    """pasos obtiene la distancia de cualquier nota respecto a La4
        Params
        ------
            octava:int
                indica con un entero a que octava (0-8) pertenece la nota             
            nota:str
                indica que tipo de nota es, puede escribirse en ingles o espanol
            accidente:str
                indica si la nota es natural, bemol o sostenida
        Return
        ------
            num_pasos:int
                distancia positiva o negativa de una nota respecto a La4
    """
    #concatena los parametros nota y accidente para buscar la cadena completa en los diccionarios
    nota_real= nota + accidente
    
    #Si la octava es 4 unicamente revisa el diccionario pasos_neutros
    if octava == 4:
        try:
            pasos_neutros   = {'C':-9, 'C#':-8, 'Db':-8, 'D':-7, 'D#':-6, 'Eb':-6, 'E':-5, 'F':-4, 'F#':-3, 'Gb':-3, 'G':-2, 'G#':-1, 'Ab':-1, 'A':0, 'A#':1, 'Bb':1, 'B':2,
                               'Do':-9, 'Do#':-8, 'Reb':-8, 'Re':-7, 'Re#':-6, 'Mib':-6, 'Mi':-5, 'Fa':-4, 'Fa#':-3, 'Solb':-3, 'Sol':-2, 'Sol#':-1, 'Lab':-1, 'La':0, 'La#':1, 'Sib':1, 'Si':2}
            num_pasos = pasos_neutros[nota_real]
        #Si no encuentra la definicion en el diccionario regresa -100
        except:
            num_pasos = -100
    
    #Si la octava es mayor a 4 se cuentan los pasos a la nota similar mas cercana y despues se multiplica por el numero de octavas de diferencia
    if octava > 4:
        try:
            pasos_positivos = {'A':0 , 'A#':1, 'Bb':1, 'B':2, 'C':3, 'C#':4, 'Db':4,'D':5, 'D#':6, 'Eb':6, 'E':7, 'F':8, 'F#':9, 'Gb':9, 'G':10, 'G#':11, 'Ab':11,
                               'La':0 , 'La#':1, 'Sib':1, 'Si':2, 'Do':3, 'Do#':4, 'Reb':4,'Re':5, 'Re#':6, 'Mib':6, 'Mi':7, 'Fa':8, 'Fa#':9, 'Solb':9, 'Sol':10, 'Sol#':11, 'Lab':11}
            num_pasos = pasos_positivos[nota_real]
            distancia_octavas = octava - 5
            num_pasos = (12 * distancia_octavas) + num_pasos
        #Si no encuentra la definicion en el diccionario regresa -100
        except:
            num_pasos = -100
    
    #Si la octava es menor a 4 se cuentan los pasos a la nota similar mas cercana y despues se multiplica por el numero de octavas de diferencia    
    if octava < 4:
        try:
            pasos_negativos = {'A':0, 'Ab':1, 'G#':1, 'G':2, 'Gb':3, 'F#':3, 'F':4, 'E':5, 'Eb':6, 'D#':6, 'D':7, 'Db':8, 'C#':8, 'C':9, 'B':10, 'Bb':11, 'A#':11,
                               'La':0, 'Lab':1, 'Sol#':1, 'Sol':2, 'Solb':3, 'Fa#':3, 'Fa':4, 'Mi':5, 'Mib':6, 'Re#':6, 'Re':7, 'Reb':8, 'Do#':8, 'Do':9, 'Si':10, 'Sib':11, 'La#':11}
            num_pasos = pasos_negativos[nota_real]
            distancia_octavas = 4 - octava
            num_pasos = (-1)*((12 * distancia_octavas) + num_pasos)
        #Si no encuentra la definicion en el diccionario regresa -100
        except:
            num_pasos = -100
        
    return num_pasos

def ReproduceLista(lista):
    """reproduceLista reproduce una lista que contiene un pedazo de la cancion con ayuda de la biblioteca pysine
        Params
        -----
            lista:[]
                pedazo de la cancion
    """
    NOTE= 0
    ACC = 1
    OCTAVE = 2
    TIME = 3
    n = len(lista)
    for i in range(n):
        if lista[i][NOTE] == "Z": #es un silencio
            sleep(lista[i][TIME])
        else:
            freq = Frecuencia(lista[i][OCTAVE],lista[i][NOTE],lista[i][ACC])
            #genera una onda senoidal de determinada frecuencia durante el tiempo indicado
            sine(freq, lista[i][TIME])
            sleep(0.01)
    
def ReproduceArchivo(lista):
    """reproduceArchivo utiliza la lista de la cancion completa para determinar como reproducir notas individuales o bloques
        Params
        -----
            lista:[]
                cancion completa
    """
    bloque = []
    BLOCK = 4
    contador_bloque = 0
    n = len(lista)
    for i in range(n):
        ReproduceLista([lista[i]])
        print([lista[i]])
        if (lista[i][BLOCK] == ':' and contador_bloque == 0):
            #Indica que inicio el bloque
            contador_bloque += 1
            bloque.append(lista[i])
        elif (lista[i][BLOCK] == '-' and contador_bloque == 1):
            #Agregar valor interno del bloque
            bloque.append(lista[i])
        elif (lista[i][BLOCK] == ':' and contador_bloque == 1):
            #Indica fin de bloque
            contador_bloque = 0
            bloque.append(lista[i])
            #Reproduce todo el bloque y limpia la lista para usos posteriores
            ReproduceLista(bloque)
            bloque.clear()

def VerificarFlotante(entrada):
    """VerificarFlotante recibe un valor para convertirlo a flotante de ser posible.
        Params
        -----
            entrada
                es el valor que recibe para realizar la operacion
        Return
            temp 
                es el valor ya modificado
    """
    temp = 'NaN'
    try:
        temp = float(entrada)
    except:
        pass
    
    return temp

def VerificarEntero(entrada):
    """VerificarEntero recibe un valor para convertirlo a entero de ser posible.
        Params
        -----
            entrada
                es el valor que recibe para realizar la operacion
        Return
            temp 
                es el valor ya modificado
    """
    temp = 'NaN'
    try:
        temp = int(entrada)
    except:
        pass
    
    return temp


def ValidarFormato(header):
    """validarFormato recibe un valor para convertirlo a flotante de ser posible.
        Params
        -----
            entrada
                es el valor que recibe para realizar la operacion
        Return
            temp 
                es el valor ya modificado
    """
    if header[0] == "nombre_nota" and header[1] == "accidente" and header[2] == "octava" and header[3] == "duracion" and header[4] == "bloque":
        return "ok"
    else:
        return "Archivo no valido"

def main():
    LeerNotas()

if __name__ == "__main__":
    main()
