import React, { useEffect, useState } from 'react';

const Marketplace = () => {
  const [drills, setDrills] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8002/marketplace/list')
      .then(res => res.json())
      .then(data => setDrills(data));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">🏪 Marketplace</h2>
      {drills.length === 0 ? (
        <p>No drill packs found.</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
          {drills.map((drill, index) => (
            <div key={index} className="bg-white shadow-md p-4 rounded-lg border border-gray-200">
              <h3 className="text-xl font-semibold">{drill.title}</h3>
              <p className="text-gray-600 my-1">{drill.description}</p>
              <p className="text-sm text-gray-500">Coach: {drill.coach}</p>
              <div className="flex flex-wrap gap-2 my-2">
                {drill.tags.map((tag, i) => (
                  <span key={i} className="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-full">{tag}</span>
                ))}
              </div>
              <p className="font-bold text-green-600">${drill.price}</p>
              <button className="mt-2 px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 transition">
                View Details
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Marketplace;
