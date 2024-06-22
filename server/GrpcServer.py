import sys
sys.path.append("../interface")

from concurrent import futures
import screen_brightness_control as sbc

import grpc
import inter_display_interface_pb2 
import inter_display_interface_pb2_grpc

class InterDisplayCommunicationServicer:
    def SetDisplaySettings(self, p_request, p_context):
        sbc.set_brightness(p_request.brightness, display = 0)
        print("Set brightness to " + str(p_request.brightness))
        return inter_display_interface_pb2.Answer(error = False)
    
    def GetDisplaySettings(self, p_request, p_context):
        l_brightness = sbc.get_brightness(display = 0)[0]
        print("Display brightness requested (current value: " + str(l_brightness) + ")")
        return inter_display_interface_pb2.DisplaySettings(brightness = l_brightness)

class GrpcServer:

    def __init__(self):
        self.__ipAdress = "localhost"
        self.__grpcPort = 50051

    def ServeInsecure(self, p_ipAdress, p_grpcPort):
        self.__ipAdress = p_ipAdress
        self.__grpcPort = p_grpcPort
        l_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        inter_display_interface_pb2_grpc.add_InterDisplayCommunicationServicer_to_server(InterDisplayCommunicationServicer(), l_server)
        l_server.add_insecure_port(self.__ipAdress + ":" + str(self.__grpcPort))
        l_server.start()
        print("Server is listening on " + str(self.__ipAdress) + ":" + str(self.__grpcPort))
        l_server.wait_for_termination()

# For test purpose only
if __name__ == '__main__':
    displayServer = GrpcServer()
    displayServer.ServeInsecure("127.0.0.1", 50051)