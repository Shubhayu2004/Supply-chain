import React, { useState, useEffect } from 'react';
import {
  Box,
  Button,
  TextField,
  Typography,
  Paper,
  MenuItem,
  Select,
  FormControl,
  InputLabel,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow
} from '@mui/material';
import axios from 'axios';
import { API_CONFIG } from '../config/api';

interface ItemOption {
  item_id: string;
  Brand: string;
  Description: string;
}

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
  const [itemOptions, setItemOptions] = useState<ItemOption[]>([]);
  const [forecastData, setForecastData] = useState<ForecastData | null>(null);

  useEffect(() => {
    axios.get(`${API_CONFIG.BASE_URL}/items`).then(res => {
      setItemOptions(res.data);
    });
  }, []);

  const getForecast = async () => {
    try {
      const response = await axios.post(`${API_CONFIG.BASE_URL}/predict`, {
        item_id: itemId,
        forecast_days: forecastDays
      });
      setForecastData(response.data);
    } catch (error) {
      alert('Error fetching forecast. Please check your input.');
    }
  };

  return (
    <Box p={3}>
      <Paper elevation={3} sx={{ p: 2, mb: 2 }}>
        <Typography variant="h5" gutterBottom>
          Sales Forecast
        </Typography>
        <Box display="flex" gap={2} mb={2}>
          <FormControl sx={{ minWidth: 220 }}>
            <InputLabel id="item-select-label">Item</InputLabel>
            <Select
              labelId="item-select-label"
              value={itemId}
              label="Item"
              onChange={(e) => setItemId(e.target.value)}
            >
              {itemOptions.map((item) => (
                <MenuItem key={item.item_id} value={item.item_id}>
                  {item.Brand} - {item.Description}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
          <TextField
            label="Forecast Days"
            type="number"
            value={forecastDays}
            onChange={(e) => setForecastDays(parseInt(e.target.value) || 7)}
          />
          <Button variant="contained" onClick={getForecast} disabled={!itemId}>
            Generate Forecast
          </Button>
        </Box>
      </Paper>
      {forecastData && (
        <Paper elevation={3} sx={{ p: 2 }}>
          <Typography variant="h6" gutterBottom>
            Forecast Results (Next {forecastDays} Days)
          </Typography>
          <TableContainer component={Paper}>
            <Table size="small">
              <TableHead>
                <TableRow>
                  <TableCell>Day</TableCell>
                  <TableCell>Ensemble Forecast</TableCell>
                  <TableCell>SARIMA</TableCell>
                  <TableCell>XGBoost</TableCell>
                  <TableCell>Holt-Winters</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {forecastData.forecast.map((ensemble, idx) => (
                  <TableRow key={idx}>
                    <TableCell>{idx + 1}</TableCell>
                    <TableCell>{ensemble.toFixed(2)}</TableCell>
                    <TableCell>{forecastData.individual_forecasts.sarima[idx].toFixed(2)}</TableCell>
                    <TableCell>{forecastData.individual_forecasts.xgboost[idx].toFixed(2)}</TableCell>
                    <TableCell>{forecastData.individual_forecasts.holtwinters[idx].toFixed(2)}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </Paper>
      )}
    </Box>
  );
};

export default SalesForecast;