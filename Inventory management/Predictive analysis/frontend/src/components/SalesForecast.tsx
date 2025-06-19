import React, { useState } from 'react';
import { Box, Button, TextField, Typography, Paper } from '@mui/material';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

interface ForecastData {
  forecast: number[];
  individual_forecasts: {
    sarima: number[];
    xgboost: number[];
    holtwinters: number[];
  };
}

const SalesForecast: React.FC = () => {
  const [itemId, setItemId] = useState('');
  const [forecastDays, setForecastDays] = useState(7);
  const [forecastData, setForecastData] = useState<ForecastData | null>(null);

  const getForecast = async () => {
    try {
      const response = await axios.post('http://localhost:5000/api/v1/predict', {
        item_id: itemId,
        forecast_days: forecastDays
      });
      setForecastData(response.data);
    } catch (error) {
      console.error('Error fetching forecast:', error);
    }
  };

  return (
    <Box p={3}>
      <Paper elevation={3} sx={{ p: 2, mb: 2 }}>
        <Typography variant="h5" gutterBottom>
          Sales Forecast
        </Typography>
        <Box display="flex" gap={2} mb={2}>
          <TextField
            label="Item ID"
            value={itemId}
            onChange={(e) => setItemId(e.target.value)}
          />
          <TextField
            label="Forecast Days"
            type="number"
            value={forecastDays}
            onChange={(e) => setForecastDays(parseInt(e.target.value))}
          />
          <Button variant="contained" onClick={getForecast}>
            Generate Forecast
          </Button>
        </Box>
      </Paper>

      {forecastData && (
        <Paper elevation={3} sx={{ p: 2 }}>
          <Line
            data={{
              labels: Array.from({ length: forecastData.forecast.length }, (_, i) => `Day ${i + 1}`),
              datasets: [
                {
                  label: 'Ensemble Forecast',
                  data: forecastData.forecast,
                  borderColor: 'rgb(75, 192, 192)',
                  tension: 0.1
                }
              ]
            }}
          />
        </Paper>
      )}
    </Box>
  );
};

export default SalesForecast;