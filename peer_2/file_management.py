import os
import requests

# Directorio para buscar archivos
CARPETA_ARCHIVOS = os.path.expanduser('./')

# Función para la selección interactiva de archivos
def seleccion_interactiva(archivos):
    eleccion_indices = []
    print("Archivos disponibles para seleccionar:")
    for i, archivo in enumerate(archivos):
        print(f"{i + 1}: {archivo}")

    print("Indica el número del archivo para seleccionarlo, escribe 'terminar' para finalizar.")
    while True:
        seleccion = input("Selecciona un archivo (o 'terminar' para finalizar): ")
        if seleccion == 'terminar':
            break
        else:
            try:
                indice = int(seleccion) - 1
                if indice in range(len(archivos)):
                    eleccion_indices.append(indice + 1)
                else:
                    print("Elige un número de archivo válido.")
            except ValueError:
                print("Por favor, introduce un número.")
    
    return eleccion_indices

# Función para obtener la lista de archivos en un directorio
def obtener_lista_archivos(directorio):
    return [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]

# Función principal para la selección de archivos
def elegir_archivos():
    lista_archivos = obtener_lista_archivos(CARPETA_ARCHIVOS)
    indices = seleccion_interactiva(lista_archivos)
    resultado = requests.post('http://localhost:3000/seleccionar_archivos', json={"listaArchivos": lista_archivos, "indicesElegidos": indices})
    archivos_elegidos = resultado.json()['archivosSeleccionados']
    print("Archivos elegidos:", archivos_elegidos)
    return archivos_elegidos

# Desarrollado por David González Idárraga
