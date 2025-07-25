import { render, screen } from '@testing-library/react';
import App from './App';

global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({ message: 'Hello from Flask!' }),
  })
);

test('renders Frontend React heading', () => {
  render(<App />);
  expect(screen.getByText(/Frontend React/i)).toBeInTheDocument();
});