import sys
sys.path.append("../interface")

from concurrent import futures

import grpc
import camera_interface_pb2 
import camera_interface_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = camera_interface_pb2_grpc.CameraStub(channel)

    camSetting = camera_interface_pb2.CameraSettings(onScreenWidth = 12, onScreenHeight = 25)
    ans = stub.CameraConfiguration(camSetting)

    print(f"Feature name: {ans.error}")

if __name__ == '__main__':
    run()