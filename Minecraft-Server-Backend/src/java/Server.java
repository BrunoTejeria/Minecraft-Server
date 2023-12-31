import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {

    public static void main(String[] args) {

        // Puerto del servidor
        int puertoSocket = 512;

        // Ruta de server.jar
        String rutaJar = "../../1.20.4/server.jar";

        // Memoria  ram del servidor
        String minecraft_server_ram_inicial = "-Xmx1024M";
        String minecraft_server_ram_constante = "-Xms1024M";

        try (ServerSocket serverSocket = new ServerSocket(puertoSocket)) {
            System.out.println("Esperando conexión en el puerto " + puertoSocket);
            Socket clienteSocket = serverSocket.accept();
            System.out.println("Cliente conectado desde " + clienteSocket.getInetAddress());

            // Obtener flujos de entrada y salida del socket
            OutputStream socketOutputStream = clienteSocket.getOutputStream();
            InputStream socketInputStream = clienteSocket.getInputStream();

            // Redirigir la salida estándar del proceso al socket
            ProcessBuilder processBuilder = new ProcessBuilder(
                "java",
                minecraft_server_ram_inicial,
                minecraft_server_ram_constante,
                "-jar",
                rutaJar,
                "nogui"
            );
            processBuilder.redirectOutput(ProcessBuilder.Redirect.PIPE);
            Process proceso = processBuilder.start();
            InputStream procesoInputStream = proceso.getInputStream();

            // Crear un hilo para enviar la salida del proceso al socket
            new Thread(() -> {
                try {
                    int bytesRead;
                    byte[] buffer = new byte[1024];
                    while ((bytesRead = procesoInputStream.read(buffer)) != -1) {
                        socketOutputStream.write(buffer, 0, bytesRead);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }).start();

            // Crear un hilo para recibir datos del socket y mostrar en la consola
            new Thread(() -> {
                try {
                    int bytesRead;
                    byte[] buffer = new byte[1024];
                    while ((bytesRead = socketInputStream.read(buffer)) != -1) {
                        System.out.write(buffer, 0, bytesRead);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }).start();

            // Esperar a que el proceso termine
            int estado = proceso.waitFor();
            System.out.println("El proceso ha terminado con estado: " + estado);

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
