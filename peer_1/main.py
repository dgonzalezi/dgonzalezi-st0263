import time
from server import lanzar_servidor  # Cambiado desde start_server
from client import enviarArchivosAObjetivo  # Cambiado desde sendSelectedFiles
from file_management import elegir_archivos  # Cambiado desde select_files

SERVIDOR_PUERTO = 8000
DESTINO_PUERTO = 9000

def main():
    servidor = lanzar_servidor(SERVIDOR_PUERTO)
    print(f"Servidor activo en puerto {SERVIDOR_PUERTO}")

    # Operaciones del cliente
    time.sleep(10)
    archivos_seleccionados_por_usuario = elegir_archivos()
    
    try:
        time.sleep(5)
        enviarArchivosAObjetivo(archivos_seleccionados_por_usuario, f'localhost:{DESTINO_PUERTO}')
        time.sleep(10)
    except KeyboardInterrupt:
        print("Servidor detenido manualmente por el usuario.")
            

if __name__ == '__main__':
    main()

# Desarrollado por David González Idárraga
