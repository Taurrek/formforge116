export const fetchReportData = async () => {
  // TODO: replace with real API call or context
  return {
    athleteCount: 5,
    avgFatigue: 0.47,
    peakFatigue: { value: 0.62, timestamp: Date.now() / 1000 },
    feedbackHighlights: [
      'Maintain upright torso',
      'Increase arm drive efficiency',
      'Lift knees higher for stride power'
    ],
  };
};
