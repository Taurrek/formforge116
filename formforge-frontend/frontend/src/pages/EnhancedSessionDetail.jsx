import React from 'react';
import AnalysisViewer from '../AnalysisViewer';
import AthleteProgressChart from '../AthleteProgressChart';
import QualityScoreCard from '../QualityScoreCard';
import PerformanceRadar from '../PerformanceRadar';
import NoteAI from '../NoteAI';

export default function EnhancedSessionDetail() {
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-bold">Session Deep Dive</h1>
      <AnalysisViewer />
      <AthleteProgressChart />
      <QualityScoreCard />
      <PerformanceRadar />
      <NoteAI />
    </div>
  );
}
