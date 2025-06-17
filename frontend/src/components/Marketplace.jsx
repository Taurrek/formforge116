import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function Marketplace() {
  const [packs, setPacks] = useState([]);

  useEffect(() => {
    axios.get('/marketplace/list')
      .then(res => setPacks(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Marketplace</h1>
      {packs.length === 0
        ? <p>No drill packs found.</p>
        : (
          <ul>
            {packs.map(p => (
              <li key={p.id} className="border rounded p-2 mb-2">
                <h2 className="font-semibold">{p.title}</h2>
                <p>Price: ${(p.price_cents/100).toFixed(2)}</p>
                <p>Commission: ${(p.commission_amount/100).toFixed(2)}</p>
                <a href={p.file_url} className="text-blue-500" target="_blank">Download</a>
              </li>
            ))}
          </ul>
        )
      }
    </div>
  );
}
