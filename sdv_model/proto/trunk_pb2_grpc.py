# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import sdv_model.proto.trunk_pb2 as trunk__pb2


class TrunkStub(object):
    """*
    @brief Example trunk service for controlling the trunks of the vehicle body.
    This definition is designed here according to the draft of the comfort seats
    service definition of the COVESA Vehicle Service Catalog (VSC) (see
    https://github.com/COVESA/vehicle_service_catalog) as a definition of an
    trunk service is currently missing in VSC.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetLockState = channel.unary_unary(
            "/sdv.edge.comfort.trunk.v1.Trunk/SetLockState",
            request_serializer=trunk__pb2.SetLockStateRequest.SerializeToString,
            response_deserializer=trunk__pb2.SetLockStateReply.FromString,
        )
        self.Open = channel.unary_unary(
            "/sdv.edge.comfort.trunk.v1.Trunk/Open",
            request_serializer=trunk__pb2.OpenRequest.SerializeToString,
            response_deserializer=trunk__pb2.OpenReply.FromString,
        )
        self.Close = channel.unary_unary(
            "/sdv.edge.comfort.trunk.v1.Trunk/Close",
            request_serializer=trunk__pb2.CloseRequest.SerializeToString,
            response_deserializer=trunk__pb2.CloseReply.FromString,
        )


class TrunkServicer(object):
    """*
    @brief Example trunk service for controlling the trunks of the vehicle body.
    This definition is designed here according to the draft of the comfort seats
    service definition of the COVESA Vehicle Service Catalog (VSC) (see
    https://github.com/COVESA/vehicle_service_catalog) as a definition of an
    trunk service is currently missing in VSC.
    """

    def SetLockState(self, request, context):
        """* Set the desired lock state of the addressed trunk(s)
        Setting the lock state is possible independently of the open/closed state
        of the respective trunk lid; in particular it is possible to set the state
        to locked during the lid is open.

        Returns gRPC status codes:
        * OK - The lock state was sucessfully set
        * NOT_FOUND - The specified trunk instance is not available in this vehicle
        * UNIMPLEMENTED - Setting the lock state is not supported by this vehicle
        * INTERNAL - A service internal error happened - see error message for details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Open(self, request, context):
        """* Request to open the addressed trunk(s)
        Depending on the underlying vehicle hardware, this
        - could be not supported at all,
        - the request triggers the trunk lid to just "spring open", or
        - the lid is moved to fully open state by a spring or a motor.
        The request to open (if supported) does open the trunk lid, but does not
        change the lock state of the trunk.

        Returns gRPC status codes:
        * OK - The operation to open the trunk was successfully triggered.
        * NOT_FOUND - The specified trunk instance is not available in this vehicle
        * UNIMPLEMENTED - Opening the trunk is not supported by this vehicle
        * INTERNAL - A service internal error happened - see error message for details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Close(self, request, context):
        """* Request to close the addressed trunk(s)
        Depending on the underlying vehicle hardware, this
        - could be not supported at all, or
        - the lid will be moved to closed state, e.g. by a motor.
        This request (if supported) does close the trunk lid, but does not
        change the lock state of the trunk.

        Returns gRPC status codes:
        * OK - The operation to close the trunk(s) was successfully triggered.
        * NOT_FOUND - The specified trunk instance is not available in this vehicle
        * UNIMPLEMENTED - Closing the trunk is not supported by this vehicle
        * INTERNAL - A service internal error happened - see error message for details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TrunkServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SetLockState": grpc.unary_unary_rpc_method_handler(
            servicer.SetLockState,
            request_deserializer=trunk__pb2.SetLockStateRequest.FromString,
            response_serializer=trunk__pb2.SetLockStateReply.SerializeToString,
        ),
        "Open": grpc.unary_unary_rpc_method_handler(
            servicer.Open,
            request_deserializer=trunk__pb2.OpenRequest.FromString,
            response_serializer=trunk__pb2.OpenReply.SerializeToString,
        ),
        "Close": grpc.unary_unary_rpc_method_handler(
            servicer.Close,
            request_deserializer=trunk__pb2.CloseRequest.FromString,
            response_serializer=trunk__pb2.CloseReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "sdv.edge.comfort.trunk.v1.Trunk", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Trunk(object):
    """*
    @brief Example trunk service for controlling the trunks of the vehicle body.
    This definition is designed here according to the draft of the comfort seats
    service definition of the COVESA Vehicle Service Catalog (VSC) (see
    https://github.com/COVESA/vehicle_service_catalog) as a definition of an
    trunk service is currently missing in VSC.
    """

    @staticmethod
    def SetLockState(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sdv.edge.comfort.trunk.v1.Trunk/SetLockState",
            trunk__pb2.SetLockStateRequest.SerializeToString,
            trunk__pb2.SetLockStateReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Open(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sdv.edge.comfort.trunk.v1.Trunk/Open",
            trunk__pb2.OpenRequest.SerializeToString,
            trunk__pb2.OpenReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Close(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sdv.edge.comfort.trunk.v1.Trunk/Close",
            trunk__pb2.CloseRequest.SerializeToString,
            trunk__pb2.CloseReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
