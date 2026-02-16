import React from 'react';
import { QueryClient, QueryClientProvider } from 'react-query';
import { HomePage } from './pages/HomePage';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="container mx-auto px-4 py-8">
        <HomePage />
      </div>
    </QueryClientProvider>
  );
}

export default App;