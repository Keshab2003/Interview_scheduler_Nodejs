const express = require('express');
const router = express.Router();
const db = require('../db');

router.post('/', (req, res) => {
  const { job_id, candidate_id, date_time, status } = req.body;
  const query = 'INSERT INTO appointments (job_id, candidate_id, date_time, status) VALUES (?, ?, ?, ?)';
  db.query(query, [job_id, candidate_id, date_time, status], (err, results) => {
    if (err) return res.status(500).send(err);
    res.status(201).json({ id: results.insertId });
  });
});

module.exports = router;
