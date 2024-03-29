# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import peer_pb2 as peer__pb2


class ServerHandlerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.atender_solicitud_archivos = channel.unary_unary(
                '/ServerHandler/atender_solicitud_archivos',
                request_serializer=peer__pb2.listFilesSended.SerializeToString,
                response_deserializer=peer__pb2.confirmation.FromString,
                )


class ServerHandlerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def atender_solicitud_archivos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerHandlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'atender_solicitud_archivos': grpc.unary_unary_rpc_method_handler(
                    servicer.atender_solicitud_archivos,
                    request_deserializer=peer__pb2.listFilesSended.FromString,
                    response_serializer=peer__pb2.confirmation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ServerHandler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServerHandler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def atender_solicitud_archivos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ServerHandler/atender_solicitud_archivos',
            peer__pb2.listFilesSended.SerializeToString,
            peer__pb2.confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
