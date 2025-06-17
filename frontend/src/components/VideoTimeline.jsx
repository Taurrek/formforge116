import React from 'react';
import VideoPlayer from './VideoPlayer';
import RiskOverlay from './RiskOverlay';

export default function VideoTimeline({ session }) {
  const jointData = session?.frames[0]?.joints || [];

  return (
    <div className="relative w-full h-full">
      <VideoPlayer session={session} />
      <RiskOverlay jointData={jointData} />
    </div>
  );
}
