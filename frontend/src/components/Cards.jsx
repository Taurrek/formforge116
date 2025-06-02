import React from 'react';

export default function Cards({ cardsData }) {
  if (!cardsData) return <div>Loading cards...</div>;

  return (
    <div className="cards-container">
      {cardsData.map((card, idx) => (
        <div key={idx} className="card">
          <h4>{card.title}</h4>
          <p>{card.description}</p>
        </div>
      ))}
    </div>
  );
}
