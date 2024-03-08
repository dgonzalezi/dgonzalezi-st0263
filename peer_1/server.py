import grpc
from concurrent import futures
import peer_pb2
import peer_pb2_grpc

# Clase para gestionar las peticiones al servidor
class ServerHandler(peer_pb2_grpc.ServerHandlerServicer):
    def atender_solicitud_archivos(self, request, context):
        print(f"Archivos disponibles en peer remoto: {request.file}")
        return peer_pb2.confirmation(status_code="Archivos enviados correctamente")

# Método para lanzar el servidor en un puerto dado
def lanzar_servidor(numero_puerto):
    servidor_grpc = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    peer_pb2_grpc.add_ServerHandlerServicer_to_server(ServerHandler(), servidor_grpc)
    servidor_grpc.add_insecure_port(f'[::]:{numero_puerto}')
    servidor_grpc.start()
    return servidor_grpc

# Desarrollado por David González Idárraga
