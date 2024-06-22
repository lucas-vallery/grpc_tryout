import sys
sys.path.append("../interface")

from concurrent import futures

import grpc
import inter_display_interface_pb2 
import inter_display_interface_pb2_grpc

class GrpcClientStub:

    def __init__(self):
        self.__ipAdress = "localhost"
        self.__grpcPort = 50051
        self.__channel  = None
        self.__stub     = None
    
    def ConnectInsecure(self, p_ipAdress, p_grpcPort):
        self.__ipAdress = p_ipAdress
        self.__grpcPort = p_grpcPort
        # Create the connection to the server
        self.__channel = grpc.insecure_channel(self.__ipAdress + ":" + str(self.__grpcPort))
        self.__stub = inter_display_interface_pb2_grpc.InterDisplayCommunicationStub(self.__channel)

    def SetDisplaySettings(self, p_brightness):
        # Check if the brightness is between 0 and 100
        l_brightness = p_brightness if p_brightness <= 100 else 100
        l_brightness = l_brightness if l_brightness >= 0   else 0
        # Send the set request to the grpc server
        l_msg = inter_display_interface_pb2.DisplaySettings(brightness = l_brightness)
        l_ans = self.__stub.SetDisplaySettings(l_msg)
        return l_ans.error

    def GetDisplaySettings(self):
        # Send get request to the grpc server
        l_msg = inter_display_interface_pb2.Empty()
        l_ans = self.__stub.GetDisplaySettings(l_msg)
        print(str(l_ans.brightness))
        

# For test purpose only
if __name__ == '__main__':
    displayStub = GrpcClientStub()
    displayStub.ConnectInsecure("127.0.0.1", 50051)
    displayStub.GetDisplaySettings()
    displayStub.SetDisplaySettings(42)