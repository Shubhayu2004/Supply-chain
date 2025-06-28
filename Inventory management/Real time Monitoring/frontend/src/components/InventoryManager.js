import React, { useEffect, useState } from 'react';

const API_URL = 'http://localhost:8000/inventory';

function InventoryManager() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState('');
  const [quantity, setQuantity] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const fetchItems = () => {
    setLoading(true);
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setItems(data))
      .catch(() => setError('Failed to fetch inventory'))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    fetchItems();
  }, []);

  const addItem = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      const res = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, quantity: Number(quantity) })
      });
      if (!res.ok) throw new Error('Add failed');
      setName('');
      setQuantity(0);
      fetchItems();
    } catch {
      setError('Failed to add item');
    }
    setLoading(false);
  };

  const updateItem = async (id, newQuantity) => {
    setLoading(true);
    setError('');
    try {
      const res = await fetch(`${API_URL}/${id}?quantity=${newQuantity}`, {
        method: 'PUT'
      });
      if (!res.ok) throw new Error('Update failed');
      fetchItems();
    } catch {
      setError('Failed to update item');
    }
    setLoading(false);
  };

  const deleteItem = async (id) => {
    setLoading(true);
    setError('');
    try {
      const res = await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
      if (!res.ok) throw new Error('Delete failed');
      fetchItems();
    } catch {
      setError('Failed to delete item');
    }
    setLoading(false);
  };

  return (
    <div>
      <h2>Inventory</h2>
      <form onSubmit={addItem} style={{ marginBottom: 16 }}>
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={e => setName(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Quantity"
          value={quantity}
          onChange={e => setQuantity(e.target.value)}
          required
          min={0}
          style={{ marginLeft: 8 }}
        />
        <button type="submit" style={{ marginLeft: 8 }}>Add</button>
      </form>
      {loading && <div>Loading...</div>}
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={{ border: '1px solid #ccc' }}>Name</th>
            <th style={{ border: '1px solid #ccc' }}>Quantity</th>
            <th style={{ border: '1px solid #ccc' }}>Last Updated</th>
            <th style={{ border: '1px solid #ccc' }}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {items.map(item => (
            <tr key={item.id}>
              <td style={{ border: '1px solid #ccc' }}>{item.name}</td>
              <td style={{ border: '1px solid #ccc' }}>
                <input
                  type="number"
                  value={item.quantity}
                  min={0}
                  onChange={e => updateItem(item.id, e.target.value)}
                  style={{ width: 60 }}
                />
              </td>
              <td style={{ border: '1px solid #ccc' }}>{new Date(item.last_updated).toLocaleString()}</td>
              <td style={{ border: '1px solid #ccc' }}>
                <button onClick={() => deleteItem(item.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default InventoryManager; 