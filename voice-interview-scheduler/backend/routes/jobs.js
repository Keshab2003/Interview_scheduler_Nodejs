const express = require('express');
const router = express.Router();
const db = require('../db');

router.post('/', (req, res) => {
  const { title, description, requirements } = req.body;
  const query = 'INSERT INTO jobs (title, description, requirements) VALUES (?, ?, ?)';
  db.query(query, [title, description, requirements], (err, results) => {
    if (err) return res.status(500).send(err);
    res.status(201).json({ id: results.insertId });
  });
});

router.get('/', (req, res) => {
  db.query('SELECT * FROM jobs', (err, results) => {
    if (err) return res.status(500).send(err);
    res.json(results);
  });
});

module.exports = router;
