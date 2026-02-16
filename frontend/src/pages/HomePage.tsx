import React from 'react';
import { useQuery } from 'react-query';
import { api } from '../services/api';
import { PlayerCard } from '../components/PlayerCard';

export const HomePage: React.FC = () => {
  const { data: players, isLoading } = useQuery('players', api.getPlayers);

  if (isLoading) return <div className="text-center p-8">Loading...</div>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Top FPL Players</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {players?.map((player: any) => (
          <PlayerCard key={player.id} player={player} />
        ))}
      </div>
    </div>
  );
};