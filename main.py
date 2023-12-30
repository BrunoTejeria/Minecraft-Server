import subprocess
import socket
import sys
import time



# Ruta al archivo ejecutable del servidor de Minecraft
minecraft_server_path = ""



def start_minecraft_server():
    # Comando para iniciar el servidor
    command = ["java", "-Xmx1024M", "-Xms1024M", "-jar", minecraft_server_path, "nogui"]

    # Inicia el servidor de Minecraft en un proceso separado
    subprocess.Popen(command, stdout=sys.stdout, stderr=sys.stderr)

def check_server_status(host, port):
    # Intenta conectarse al servidor
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))

    # Si la conexión tiene éxito, el servidor está en línea
    if result == 0:
        print("El servidor de Minecraft está en línea.")
    else:
        print("El servidor de Minecraft no está en línea.")

if __name__ == "__main__":
    # Inicia el servidor de Minecraft
    start_minecraft_server()

    # Espera un tiempo para que el servidor se inicie completamente (ajusta según sea necesario)
    time.sleep(30)

    # Verifica el estado del servidor
    server_host = "127.0.0.1"  # Cambia esto a la IP del servidor si es necesario
    server_port = 25565  # Puerto predeterminado de Minecraft

    check_server_status(server_host, server_port)
