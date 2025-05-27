const express = require('express');
const router = express.Router();
const db = require('../db');

router.post('/', (req, res) => {
  const { name, phone, current_ctc, expected_ctc, notice_period, experience } = req.body;
  const query = 'INSERT INTO candidates (name, phone, current_ctc, expected_ctc, notice_period, experience) VALUES (?, ?, ?, ?, ?, ?)';
  db.query(query, [name, phone, current_ctc, expected_ctc, notice_period, experience], (err, results) => {
    if (err) return res.status(500).send(err);
    res.status(201).json({ id: results.insertId });
  });
});

module.exports = router;
