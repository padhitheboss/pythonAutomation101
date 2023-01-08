import socket
IP =  "127.0.0.1"
PORT = 12345
SIZE = 1024
FORMAT = "utf-8"

def main():
    print("[STARTING] Server is starting")
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((IP,PORT))
    filename = client.recv(SIZE).decode(FORMAT)
    client.send("File Name Received".encode(FORMAT))
    file = open(filename,"w",encoding=FORMAT)
    data = client.recv(SIZE).decode(FORMAT)
    client.send("File Received".encode(FORMAT))
    file.write(data)
    file.close()
    client.close()
if __name__ == "__main__":
    main()