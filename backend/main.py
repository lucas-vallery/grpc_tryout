import sys
sys.path.append("../interface")

from concurrent import futures

import grpc
import camera_interface_pb2 
import camera_interface_pb2_grpc

class CameraServicer(camera_interface_pb2_grpc.CameraServicer):
    def CameraConfiguration(self, request, context):
        print(request.onScreenWidth)
        print(request.onScreenHeight)
        print("Send answer")
        return camera_interface_pb2.Answer(error = 0)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    camera_interface_pb2_grpc.add_CameraServicer_to_server(CameraServicer(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    print("Server started. Listening on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()