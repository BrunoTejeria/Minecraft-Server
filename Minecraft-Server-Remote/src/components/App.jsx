// eslint-disable-next-line no-unused-vars
import React from 'react';
import axios from 'axios';
import '../styles/App.css';

function App() {
  const startServer = async () => {
    try {
      const response = await axios.post('/api/start_server');
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
