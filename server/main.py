import GrpcServer as srv
import sys

if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 50051
    
    if ((len(sys.argv) != 3) and (len(sys.argv) != 1)):
        print("Help: main.py [ip] [port]")
        exit()
    
    if (len(sys.argv) == 3):
        ip = sys.argv[1]
        port = int(sys.argv[2])

    grpcServer = srv.GrpcServer()
    grpcServer.ServeInsecure(ip, port)