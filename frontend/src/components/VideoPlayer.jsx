import React from "react";

const VideoPlayer = () => {
  return (
    <div className="bg-black rounded-xl overflow-hidden shadow">
      <video
        controls
        width="100%"
        className="w-full"
        src="/session1.mp4"
      >
        Your browser does not support the video tag.
      </video>
    </div>
  );
};

export default VideoPlayer;
