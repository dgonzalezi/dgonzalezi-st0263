import grpc
import peer_pb2
import peer_pb2_grpc

# Esta función se encarga de enviar un conjunto de archivos seleccionados a un peer específico
def enviarArchivosAObjetivo(archivosParaEnviar, nodoDestino):
    canal = grpc.insecure_channel(nodoDestino)
    intermediario = peer_pb2_grpc.ServerHandlerStub(canal)
    resultado = intermediario.atender_solicitud_archivos(peer_pb2.listFilesSended(file=archivosParaEnviar))
    print(f"Código de estado recibido: {resultado.status_code}")

# Desarrollado por David González Idárraga
