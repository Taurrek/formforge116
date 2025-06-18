import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Users from './pages/Users';
import Reports from './pages/Reports';

export default function App() {
  return (
    <Router>
      <nav style={{ padding: '1rem', borderBottom: '1px solid #ccc' }}>
        <Link to="/users" style={{ marginRight: 10 }}>Users</Link>
        <Link to="/reports">Performance</Link>
      </nav>
      <Routes>
        <Route path="/users" element={<Users />} />
        <Route path="/reports" element={<Reports />} />
      </Routes>
    </Router>
  );
}
