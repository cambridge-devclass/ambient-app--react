import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

// Text example
test('renders starter page', () => {
  render(<App />);
  const linkElement = screen.getByText(/hello/i);
  expect(linkElement).toBeInTheDocument();
});
