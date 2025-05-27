const express = require('express');
const router = express.Router();
const db = require('../db');

router.post('/', (req, res) => {
  const { candidate_id, transcript, entities_extracted } = req.body;
  const query = 'INSERT INTO conversations (candidate_id, transcript, entities_extracted) VALUES (?, ?, ?)';
  db.query(query, [candidate_id, transcript, JSON.stringify(entities_extracted)], (err, results) => {
    if (err) return res.status(500).send(err);
    res.status(201).json({ id: results.insertId });
  });
});

module.exports = router;
