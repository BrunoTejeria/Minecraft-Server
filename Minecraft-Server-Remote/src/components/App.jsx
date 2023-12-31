// eslint-disable-next-line no-unused-vars


//Importar constantes

import { API_HTTP_IP, API_SOCKET_IP } from '../js/consts';


import React from 'react';
import axios from 'axios';
import '../styles/App.css';




function App() {
  const socket = new WebSocket(`${API_SOCKET_IP}`);
  socket.onopen = (event) => {
    console.log("Conexión WebSocket abierta:", event);
  };

  socket.onmessage = (event) => {
    console.log("Mensaje recibido:", event.data);
  };

  socket.onclose = (event) => {
    console.log("Conexión WebSocket cerrada:", event);
  };

  socket.onerror = (error) => {
    console.error("Error en la conexión WebSocket:", error);
  };





  const startServer = async () => {
    try {
      const response = await axios.get(`${API_HTTP_IP}/start-server`);
      console.log(response.data);
    } catch (error) {
      console.error('Error al iniciar el servidor:', error);
    }
  };

  const stopServer = async () => {
    try {
      const response = await axios.post('/api/stop_server');
      console.log(response.data);
    } catch (error) {
      console.error('Error al detener el servidor:', error);
    }
  };

  return (
    <div className="container">
      <h1>Gestor de Servidor Minecraft</h1>
      <button onClick={startServer}>Iniciar Servidor</button>
      <button onClick={stopServer}>Detener Servidor</button>
    </div>
  );
}

export default App;
