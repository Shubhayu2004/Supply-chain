import React from 'react';
import DetectionForm from './components/DetectionForm';
import ResultsList from './components/ResultsList';
import InventoryManager from './components/InventoryManager';

function App() {
  return (
    <div style={{ maxWidth: 800, margin: '0 auto', padding: 20 }}>
      <h1>Inventory Monitoring</h1>
      <DetectionForm />
      <hr />
      <ResultsList />
      <hr />
      <InventoryManager />
    </div>
  );
}

export default App; 