import React from 'react';
import { render, screen } from '@testing-library/react';
import { Icon } from './Icon';

// Text example
describe('Icon component', () => {
  it("renders icon", () => {
    render(<Icon name="toggle_on" />);
    const span = screen.getByText("toggle_on");
    expect(span).toHaveClass("material-symbols-rounded");
  });
});
