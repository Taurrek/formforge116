import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Landing from "./pages/Landing";
import Upload from "./pages/Upload";
import Sessions from "./pages/Sessions";

export default function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <nav className="bg-blue-600 text-white p-4 flex space-x-6">
          <Link to="/" className="hover:underline">Home</Link>
          <Link to="/upload" className="hover:underline">Upload Video</Link>
          <Link to="/sessions" className="hover:underline">Sessions</Link>
        </nav>

        <main className="max-w-4xl mx-auto p-4">
          <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/upload" element={<Upload />} />
            <Route path="/sessions" element={<Sessions />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}
