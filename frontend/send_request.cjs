const fs = require('fs');
const fetch = require('node-fetch');
const FormData = require('form-data');

const form = new FormData();
form.append('file', fs.createReadStream('/home/cj2k4211/test_joints.csv'));

fetch('http://localhost:8000/predict_sport_enhanced/', {
  method: 'POST',
  body: form,
  headers: form.getHeaders(),
})
.then(res => res.json())
.then(console.log)
.catch(console.error);
