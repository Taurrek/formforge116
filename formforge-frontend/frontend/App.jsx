import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Landing from "./src/pages/Landing";
import Upload from "./src/pages/Upload";
import Sessions from "./src/pages/Sessions";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/upload" element={<Upload />} />
        <Route path="/sessions" element={<Sessions />} />
      </Routes>
    </Router>
  );
}

export default App;
