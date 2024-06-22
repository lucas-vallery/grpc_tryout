import GrpcClientStub as clt
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
  
    client = clt.GrpcClientStub()
    client.ConnectInsecure(ip, port)

    while(1):
        print(">>", end = " ")
        cmd = input()
        cmd = cmd.split(" ")
        
        if (cmd[0] == "get"):
            client.GetDisplaySettings()
        elif ((cmd[0] == "set") and (len(cmd) == 2)):
            client.SetDisplaySettings(int(cmd[1]))
        else:
            print("Help:  get: returns the backlight value")
            print("       set [0-100]: set the backlight to the desired value")