export function downloadStrainCsv() {
  fetch('/output/sim_output.json')
    .then(res => {
      if (!res.ok) throw new Error('Failed to fetch sim_output.json');
      return res.json();
    })
    .then(json => {
      const rows = [['timestamp', 'joint', 'strain']];
      json.strain_timeline.forEach(entry => {
        const t = entry.timestamp;
        Object.entries(entry.strained_joints).forEach(([joint, strain]) => {
          rows.push([t, joint, strain]);
        });
      });
      const csvContent = rows.map(r => r.join(',')).join('\n');
      const blob = new Blob([csvContent], { type: 'text/csv' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'strain_timeline.csv';
      a.click();
      URL.revokeObjectURL(url);
    })
    .catch(err => alert(err.message));
}
