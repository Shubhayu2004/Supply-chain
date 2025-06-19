import React from 'react';
import { Container, CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import SalesForecast from './components/SalesForecast';

const theme = createTheme({
  palette: {
    mode: 'light',
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="lg">
        <SalesForecast />
      </Container>
    </ThemeProvider>
  );
}

export default App;