import React, { useState } from 'react';
import axios from 'axios';

const ControlPanel = () => {
  const [isRunning, setIsRunning] = useState(false);

  const startApp = async () => {
    try {
      await axios.post('http://localhost:5000/api/start');
      setIsRunning(true);
    } catch (error) {
      console.error('Failed to start the app:', error);
    }
  };

  const stopApp = async () => {
    try {
      await axios.post('http://localhost:5000/api/stop');
      setIsRunning(false);
    } catch (error) {
      console.error('Failed to stop the app:', error);
    }
  };

  return (
    <div className="control-panel">
      <h2>Control Panel</h2>
      <button onClick={startApp} disabled={isRunning}>
        Start App
      </button>
      <button onClick={stopApp} disabled={!isRunning}>
        Stop App
      </button>
      <p>App Status: {isRunning ? 'Running' : 'Stopped'}</p>
    </div>
  );
};

export default ControlPanel;