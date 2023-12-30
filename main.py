import subprocess
import socket
import sys
import time



# Dirección ip del server.
minecraft_server_host = "127.0.0.1"  # Cambia esto a la IP del servidor si es necesario

# Puerto del  servidor.
minecraft_server_port = 25565  # Puerto predeterminado de Minecraft

# Ruta al archivo ejecutable del servidor de Minecraft
minecraft_server_path = "1.20.4/server.jar" # Poner path del servidor


# Memoria  ram del servidor
minecraft_server_ram_inicial = "-Xmx1024M"
minecraft_server_ram_constante = "-Xms1024M"

# Inicializado de interfaz gráfica
gui = True # Cambiar si quieres interfaz o no



def start_minecraft_server():
	# Comando para iniciar el servidor
	if gui == True:
		command = ["java", minecraft_server_ram_inicial, minecraft_server_ram_constante, "-jar", minecraft_server_path]
	else:
		command = ["java", minecraft_server_ram_inicial, minecraft_server_ram_constante, "-jar", minecraft_server_path, "nogui"]

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


	check_server_status(minecraft_server_host, minecraft_server_port)
