import React from 'react';
import { render, screen } from '@testing-library/react';
import { SoundBoard } from './SoundBoard';

// Text example
describe("SoundBoard component", () => {
  it("renders sounds board placeholder", () => {
    render(<SoundBoard />);
    expect(screen.getByText(/sounds/i)).toBeInTheDocument();
  });
});