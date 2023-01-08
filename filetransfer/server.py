import socket
IP =  "0.0.0.0"
PORT = 12345
SIZE = 1024
FORMAT = "utf-8"

def main():
    print("[STARTING] Server is starting")
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen()
    while True:
        conn,addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connect")
        file = open("data/test.txt","r",encoding=FORMAT)
        data = file.read()
        conn.send("test.txt".encode(FORMAT))
        msg = conn.recv(SIZE).decode(FORMAT)
        print(f"[CLIENT]: {msg}")
        conn.send(data.encode(FORMAT))
        msg = conn.recv(SIZE).decode(FORMAT)
        print(f"[CLIENT] {msg}")
        file.close()
        conn.close()
if __name__ == "__main__":
    main()