const express = require('express');
const path = require('path');
const app = express();
const PORT = '8000';
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000';

app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/templates/index.html'));
});

app.post('/submit', (req, res) => {
    console.log('Data goees to flask');
    
    res.redirect(307, `${BACKEND_URL}/submit`);
});

app.get('/success', (req, res) => {
    res.send("<h1>Data submitted successfully!</h1>");
});

app.listen(PORT, () => {
    console.log(`Frontend: http://localhost:8000`);
});
