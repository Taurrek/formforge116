import React from 'react';

const ValuationBrief = ({ data }) => (
  <div id="valuation-content" className="p-4 bg-white">
    <h1 className="text-2xl font-bold mb-4">{data.projectName} Valuation Brief</h1>
    <p><strong>Completed Phases:</strong> {data.completedPhases}</p>
    <p><strong>Estimated Value:</strong> {data.estimatedValue}</p>
    <h2 className="text-xl font-semibold mt-4 mb-2">Comparable Valuations</h2>
    <ul className="list-disc list-inside">
      {data.comparable.map((c, i) => (
        <li key={i}>{c.name}: {c.valuation} — {c.notes}</li>
      ))}
    </ul>
    <h2 className="text-xl font-semibold mt-4 mb-2">Key Metrics</h2>
    <ul className="list-disc list-inside">
      {data.keyMetrics.map((m, i) => (
        <li key={i}>{m.label}: {m.value}</li>
      ))}
    </ul>
    <h2 className="text-xl font-semibold mt-4 mb-2">Investor Takeaways</h2>
    <ul className="list-disc list-inside">
      {data.investorTakeaways.map((t, i) => (
        <li key={i}>{t}</li>
      ))}
    </ul>
  </div>
);

export default ValuationBrief;
