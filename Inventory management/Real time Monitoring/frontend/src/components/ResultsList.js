import React, { useEffect, useState } from 'react';

const API_URL = 'http://localhost:8000/results';

function ResultsList() {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    setLoading(true);
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setResults(data))
      .catch(() => setError('Failed to fetch results'))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div>
      <h2>Detection Results</h2>
      {loading && <div>Loading...</div>}
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 16 }}>
        {results.map(r => (
          <div key={r.id} style={{ border: '1px solid #ccc', padding: 8, width: 200 }}>
            <div><b>Classes:</b> {r.detected_classes}</div>
            <img src={`http://localhost:8000/${r.result_image_path.replace('..', '')}`} alt="Detected" style={{ width: '100%' }} />
            <div style={{ fontSize: 12, color: '#888' }}>{new Date(r.timestamp).toLocaleString()}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ResultsList; 