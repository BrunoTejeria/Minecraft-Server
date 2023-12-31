

import sys
import asyncio
import subprocess
from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


from ServerScripts import status_server




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Esto permite que todos los dominios accedan (ajusta según tus necesidades)
    allow_credentials=True,
    allow_methods=["*"],  # Puedes limitar los métodos según sea necesario
    allow_headers=["*"],  # Puedes limitar los encabezados según sea necesario
)

websockets_list = []

# Manajador de salida personalizado que envía mensajes a los WebSockets
class WebSocketConsoleHandler:
    def __init__(self, websocket):
        self.websocket = websocket

    def write(self, message):
        asyncio.create_task(self.send_message(message))

    async def send_message(self, message):
        await self.websocket.send_text(message)


# Ruta para la conexión WebSocket
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        websockets_list.append(websocket)

        # Redirigir la salida de la consola a WebSocket
        sys.stdout = WebSocketConsoleHandler(websocket)
        sys.stderr = WebSocketConsoleHandler(websocket)
        try:
            
            while True:
                await asyncio.sleep(1)  # Mantener la conexión abierta
                

        except asyncio.CancelledError:
            pass
    except:
        print("error")
    finally:
        websockets_list.remove(websocket)
        sys.stdout = sys.__stdout__  # Restaurar la salida estándar
        sys.stderr = sys.__stderr__  # Restaurar la salida de error




# Ruta para iniciar el servidor de Minecraft y redirigir la consola al WebSocket
@app.get("/start-server")
async def start_minecraft_server():
    try:
        # Ejecutar el script en un proceso separado y capturar la salida
        process = await asyncio.create_subprocess_exec(
            "python", "ServerScripts/status_server.py",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        # Leer la salida de la consola en tiempo real
        while True:
            stdout, stderr = await process.communicate()
            if not stdout and not stderr:
                break

            # Enviar la salida al WebSocket
            output = stdout.decode("utf-8") if stdout else stderr.decode("utf-8")
            for websocket in websockets_list:
                await websocket.send_text(output)

    except Exception as e:
        print(f"Error al iniciar el servidor de Minecraft: {e}")

    return {"message": "Iniciando el servidor de Minecraft. Verifica la consola para más detalles."}

# Ruta de ejemplo
@app.get("/test")
def read_root():
    print("Mensaje de ejemplo")
    return {"message": "hola"}



