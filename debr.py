import socket

# Función que recibe el host y el puerto TCP y devolverá un boolean
def debrScan(host, port):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos un socket TCP IPv4 
    cliente.settimeout(3)

    # Determina si el puerto esta abierto o cerrado mediante la conexión
    try:
        cliente.connect((host,port))
        return True
    except socket.error:
        return False
    finally:
        cliente.close()

# Solicita al usuario el host y define la lista de puertos comunes
host = input("Introduce el host a escanear: ")
while not host or host==" ":
    print(f"")
    print(f"[!]Introduce un host válido ")
    print(f"")
    host = input("Introduce el host a escanear: ")

if not host:
    host = "Introduce un host válido."

port = [21,    # FTP – credenciales en texto claro
        22,    # SSH – fuerza bruta
        23,    # Telnet – inseguro, sin cifrado
        25,    # SMTP – abuso y enumeración
        53,    # DNS – amplificación / enumeración
        80,    # HTTP – servicios web
        110,   # POP3 – credenciales sin cifrar
        139,   # NetBIOS – sistemas Windows antiguos
        143,   # IMAP – correo
        443,   # HTTPS – servicios web
        445,   # SMB – ransomware / EternalBlue
        3306,  # MySQL – bases de datos expuestas
        3389,  # RDP – fuerza bruta en Windows
        5900,  # VNC – acceso remoto
        8080   # HTTP alternativo / paneles admin
    ]


# Llama a la función de escaneo e imprime el resultado
for p in port:
    if debrScan(host, p):
        print(f"[+] Puerto {p} Abierto")
    else:
        print(f"[-] Puerto {p} Cerrado")

# Solicita al usuario el host y puerto a analizar
host = input("Introduce el host a escanear: ")
port = int(input("Introduce el puerto a escanear: "))

