export const fetchValuationData = async () => {
  // TODO: replace with real API or context
  return {
    projectName: 'FormForge',
    completedPhases: 8,
    estimatedValue: '$75M',
    comparable: [
      { name: 'CoachAI', valuation: '$50M', notes: 'Similar fatigue analytics' },
      { name: 'FitInsight', valuation: '$100M', notes: 'Broader market reach' }
    ],
    keyMetrics: [
      { label: 'API Endpoints', value: 12 },
      { label: 'React Components', value: 25 },
      { label: 'Total LOC', value: 15000 }
    ],
    investorTakeaways: [
      'Proprietary DTW-based fatigue detection algorithm',
      'Fully offline & online investor demo modes',
      'Modular, extensible React/FastAPI architecture'
    ],
  };
};
