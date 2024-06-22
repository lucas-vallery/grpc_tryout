# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import inter_display_interface_pb2 as inter__display__interface__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in inter_display_interface_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class InterDisplayCommunicationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetDisplaySettings = channel.unary_unary(
                '/InterDisplayCommunication/SetDisplaySettings',
                request_serializer=inter__display__interface__pb2.DisplaySettings.SerializeToString,
                response_deserializer=inter__display__interface__pb2.Answer.FromString,
                _registered_method=True)
        self.GetDisplaySettings = channel.unary_unary(
                '/InterDisplayCommunication/GetDisplaySettings',
                request_serializer=inter__display__interface__pb2.Empty.SerializeToString,
                response_deserializer=inter__display__interface__pb2.DisplaySettings.FromString,
                _registered_method=True)


class InterDisplayCommunicationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetDisplaySettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDisplaySettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InterDisplayCommunicationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetDisplaySettings': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDisplaySettings,
                    request_deserializer=inter__display__interface__pb2.DisplaySettings.FromString,
                    response_serializer=inter__display__interface__pb2.Answer.SerializeToString,
            ),
            'GetDisplaySettings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDisplaySettings,
                    request_deserializer=inter__display__interface__pb2.Empty.FromString,
                    response_serializer=inter__display__interface__pb2.DisplaySettings.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'InterDisplayCommunication', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('InterDisplayCommunication', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class InterDisplayCommunication(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetDisplaySettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/InterDisplayCommunication/SetDisplaySettings',
            inter__display__interface__pb2.DisplaySettings.SerializeToString,
            inter__display__interface__pb2.Answer.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetDisplaySettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/InterDisplayCommunication/GetDisplaySettings',
            inter__display__interface__pb2.Empty.SerializeToString,
            inter__display__interface__pb2.DisplaySettings.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
