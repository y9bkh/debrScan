import socket

def debrScan(host, port):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(10)
    try:
        cliente.connect((host,port))
        cliente.close
        return True
    except socket.error:
        socket.close
        return False
    
host = input("Introduce el host a escanear: ")
port = int(input("Introduce el puerto a escanear: "))

if debrScan(host, port):
    print(f"Puerto {port} Abierto")
else:
    print(f"Puerto {port} Cerrado")
