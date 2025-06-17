import React, { useRef, useEffect } from 'react';

export default function VideoOverlay({ videoRef, joints }) {
  const canvasRef = useRef(null);

  // Match canvas size to video
  useEffect(() => {
    const canvas = canvasRef.current;
    const video = videoRef.current;
    if (!canvas || !video) return;

    function resize() {
      canvas.width = video.videoWidth || video.clientWidth;
      canvas.height = video.videoHeight || video.clientHeight;
    }

    resize();
    window.addEventListener('resize', resize);
    video.addEventListener('loadedmetadata', resize);
    return () => {
      window.removeEventListener('resize', resize);
      video.removeEventListener('loadedmetadata', resize);
    };
  }, [videoRef]);

  // Draw joints each time they update
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    joints.forEach(({ x, y, z }, idx) => {
      // Simple orthographic projection: x*width, y*height
      const px = x * canvas.width;
      const py = y * canvas.height;
      const radius = 5 + (z || 0) * 10; // scale radius by depth
      ctx.fillStyle = 'rgba(0, 200, 0, 0.7)';
      ctx.beginPath();
      ctx.arc(px, py, radius, 0, 2 * Math.PI);
      ctx.fill();
    });
  }, [joints]);

  return (
    <canvas
      ref={canvasRef}
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        pointerEvents: 'none',
      }}
    />
  );
}
