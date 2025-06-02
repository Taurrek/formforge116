import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Sessions from "./Sessions";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/sessions" element={<Sessions />} />
        {/* Add more routes here */}
      </Routes>
    </Router>
  );
}

export default App;
