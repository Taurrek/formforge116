import { useParams } from "react-router-dom";

export default function SessionDetail() {
  const { id } = useParams();

  return (
    <div className="min-h-screen p-6">
      <h1 className="text-3xl mb-4">Session Detail: {id}</h1>
      <p>This will show detailed metrics, video playback, and analysis charts.</p>
    </div>
  );
}
