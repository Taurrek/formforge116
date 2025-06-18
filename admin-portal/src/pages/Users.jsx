import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function Users() {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    axios.get('/api/admin/users')
      .then(res => setUsers(res.data))
      .catch(console.error);
  }, []);
  return (
    <div style={{ padding: 20 }}>
      <h2>All Users</h2>
      <table border="1" cellPadding="8">
        <thead><tr><th>ID</th><th>Email</th><th>Name</th><th>Created</th></tr></thead>
        <tbody>
          {users.map(u => (
            <tr key={u.id}>
              <td>{u.id}</td><td>{u.email}</td><td>{u.name}</td><td>{new Date(u.created_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
