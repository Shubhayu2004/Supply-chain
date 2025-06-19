import React, { useState, useRef } from 'react';
import { Box, Button, TextField, Typography, Paper } from '@mui/material';
import { Line } from 'react-chartjs-2';
import axios from 'axios';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  ChartData,
  ChartOptions
} from 'chart.js';

// Register Chart.js components
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

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
  const chartRef = useRef<ChartJS<"line">>(null);

  // ...rest of your component code...

  const getForecast = async () => {
    if (!itemId || !forecastDays) return;
    try {
      const response = await axios.post<ForecastData>('/api/forecast', {
        item_id: itemId,
        days: forecastDays
      });
      setForecastData(response.data);
    } catch (error) {
      console.error('Error fetching forecast:', error);
      setForecastData(null);
    }
  };

  const chartOptions: ChartOptions<'line'> = {
    responsive: true,
    scales: {
      x: {
        display: true,
        title: {
          display: true,
          text: 'Days'
        }
      },
      y: {
        display: true,
        title: {
          display: true,
          text: 'Sales Quantity'
        }
      }
    }
  };

  const chartData: ChartData<'line'> | null = forecastData ? {
    labels: Array.from({ length: forecastData.forecast.length }, (_, i) => `Day ${i + 1}`),
    datasets: [
      {
        label: 'Ensemble Forecast',
        data: forecastData.forecast,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      },
      {
        label: 'SARIMA',
        data: forecastData.individual_forecasts.sarima,
        borderColor: 'rgb(255, 99, 132)',
        tension: 0.1,
        borderDash: [5, 5]
      },
      {
        label: 'XGBoost',
        data: forecastData.individual_forecasts.xgboost,
        borderColor: 'rgb(54, 162, 235)',
        tension: 0.1,
        borderDash: [5, 5]
      },
      {
        label: 'Holt-Winters',
        data: forecastData.individual_forecasts.holtwinters,
        borderColor: 'rgb(255, 206, 86)',
        tension: 0.1,
        borderDash: [5, 5]
      }
    ]
  } : null;


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
            onChange={(e) => setForecastDays(parseInt(e.target.value) || 7)}
          />
          <Button variant="contained" onClick={getForecast}>
            Generate Forecast
          </Button>
        </Box>
      </Paper>

      {chartData && (
        <Paper elevation={3} sx={{ p: 2 }}>
          <Line
            ref={chartRef}
            options={chartOptions}
            data={chartData}
          />
        </Paper>
      )}
    </Box>
  );
};

export default SalesForecast;