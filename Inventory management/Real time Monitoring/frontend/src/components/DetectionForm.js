import React, { useRef, useState } from 'react';

const API_URL = 'http://localhost:8000/detect/image';

function DetectionForm() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const fileInputRef = useRef();
  const videoRef = useRef();
  const canvasRef = useRef();
  const [cameraActive, setCameraActive] = useState(false);

  const handleFileChange = async (e) => {
    setError('');
    setResult(null);
    const file = e.target.files[0];
    if (!file) return;
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);
    try {
      const res = await fetch(API_URL, { method: 'POST', body: formData });
      if (!res.ok) throw new Error('Detection failed');
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  };

  const startCamera = async () => {
    setCameraActive(true);
    setResult(null);
    setError('');
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      videoRef.current.srcObject = stream;
      videoRef.current.play();
    }
  };

  const captureAndSend = async () => {
    const video = videoRef.current;
    const canvas = canvasRef.current;
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const dataUrl = canvas.toDataURL('image/jpeg');
    const base64 = dataUrl.split(',')[1];
    setLoading(true);
    setError('');
    setResult(null);
    const formData = new FormData();
    formData.append('base64_image', base64);
    try {
      const res = await fetch(API_URL, { method: 'POST', body: formData });
      if (!res.ok) throw new Error('Detection failed');
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  };

  const stopCamera = () => {
    setCameraActive(false);
    if (videoRef.current && videoRef.current.srcObject) {
      videoRef.current.srcObject.getTracks().forEach(track => track.stop());
      videoRef.current.srcObject = null;
    }
  };

  return (
    <div>
      <h2>Detect Product</h2>
      <input type="file" accept="image/*" ref={fileInputRef} onChange={handleFileChange} />
      <div style={{ margin: '10px 0' }}>
        {!cameraActive ? (
          <button onClick={startCamera}>Use Camera</button>
        ) : (
          <>
            <video ref={videoRef} width={320} height={240} autoPlay style={{ border: '1px solid #ccc' }} />
            <br />
            <button onClick={captureAndSend}>Capture & Detect</button>
            <button onClick={stopCamera} style={{ marginLeft: 8 }}>Stop Camera</button>
            <canvas ref={canvasRef} style={{ display: 'none' }} />
          </>
        )}
      </div>
      {loading && <div>Detecting...</div>}
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {result && (
        <div style={{ marginTop: 10 }}>
          <h4>Detection Result</h4>
          <div><b>Detected Classes:</b> {result.detected_classes}</div>
          <div><b>Result Image:</b></div>
          <img src={`http://localhost:8000/${result.result_image_path.replace('..', '')}`} alt="Detected" style={{ maxWidth: 320, border: '1px solid #ccc' }} />
        </div>
      )}
    </div>
  );
}

export default DetectionForm; 