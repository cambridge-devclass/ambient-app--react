import React from 'react';
import { render, screen } from '@testing-library/react';
import { HomePage } from './HomePage';

// Text example
describe("HomePage component", () => {
  it("renders the home page placeholder text", () => {
    render(<HomePage />);
    expect(screen.getByText(/Home page will be here./i)).toBeInTheDocument();
  });
});