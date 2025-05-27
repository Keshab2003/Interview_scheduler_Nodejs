const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const jobs = require('./routes/jobs');
const candidate = require('./routes/candidates');
const appointment =  require('./routes/appointments');
const convo =  require('./routes/conversations');

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.use('/api/jobs', jobs);
app.use('/api/candidates', candidate);
app.use('/api/appointments',appointment);
app.use('/api/conversations',convo);
app.post('/api/response', (req, res) => {
    const { question, intent } = req.body;
    console.log(`Question: ${question}`);
    console.log(`Intent: ${JSON.stringify(intent)}`);
    // Process the intent as needed
    res.sendStatus(200);
});

const PORT = 5000;
app.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`));





