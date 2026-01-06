import socket

# Función que recibe el host y el puerto TCP y devolverá un boolean
def debrScan(host, port):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos un socket TCP IPv4 
    cliente.settimeout(10)

    # Determina si el puerto esta abierto o cerrado mediante la conexión
    try:
        cliente.connect((host,port))
        return True
    except socket.error:
        return False
    finally:
        cliente.close()

# Solicita al usuario el host y puerto a analizar
host = input("Introduce el host a escanear: ")
port = int(input("Introduce el puerto a escanear: "))

if debrScan(host, port):
    print(f"Puerto {port} Abierto")
else:
    print(f"Puerto {port} Cerrado")
