import React from 'react';

interface Props {
  player: any;
}

export const PlayerCard: React.FC<Props> = ({ player }) => {
  return (
    <div className="border rounded-lg p-4 hover:shadow-md">
      <h3 className="font-semibold">{player.web_name}</h3>
      <p className="text-sm text-gray-600">{player.team_name}</p>
      <div className="flex justify-between mt-2">
        <span>£{(player.now_cost/10).toFixed(1)}M</span>
        <span>{player.total_points} pts</span>
      </div>
    </div>
  );
};