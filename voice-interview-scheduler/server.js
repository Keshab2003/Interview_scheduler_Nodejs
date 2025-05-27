// const express = require('express');
// const bodyParser = require('body-parser');
// const cors = require('cors');
// const { body, validationResult } = require('express-validator');
// const mysql = require('mysql2/promise');

// const app = express();
// app.use(cors());
// app.use(bodyParser.json());

// // MySQL connection pool
// const pool = mysql.createPool({
//   host: 'localhost',
//   user: 'root',
//   password: 'yourpassword',
//   database: 'interview_scheduler',
// });

// // Utility: validate phone numbers (basic)
// const isPhone = (value) => /^\+?\d{7,15}$/.test(value);

// // Create Job
// app.post('/jobs', [
//   body('title').notEmpty(),
//   body('description').notEmpty(),
//   body('requirements').notEmpty(),
// ], async (req, res) => {
//   const errors = validationResult(req);
//   if(!errors.isEmpty()) return res.status(400).json({ errors: errors.array() });

//   const { title, description, requirements } = req.body;
//   try {
//     const [result] = await pool.query(
//       'INSERT INTO jobs (title, description, requirements, created_at) VALUES (?, ?, ?, NOW())',
//       [title, description, requirements]
//     );
//     res.json({ id: result.insertId, message: 'Job created' });
//   } catch (err) {
//     res.status(500).json({ error: err.message });
//   }
// });

// // Read Jobs
// app.get('/jobs', async (req, res) => {
//   try {
//     const [rows] = await pool.query('SELECT * FROM jobs ORDER BY created_at DESC');
//     res.json(rows);
//   } catch (err) {
//     res.status(500).json({ error: err.message });
//   }
// });

// // Candidate Management - Create Candidate
// app.post('/candidates', [
//   body('name').notEmpty(),
//   body('phone').custom(isPhone).withMessage('Invalid phone number'),
//   body('current_ctc').isFloat({ min: 0 }),
//   body('expected_ctc').isFloat({ min: 0 }),
//   body('notice_period').notEmpty(),
//   body('experience').isInt({ min: 0 }),
// ], async (req, res) => {
//   const errors = validationResult(req);
//   if(!errors.isEmpty()) return res.status(400).json({ errors: errors.array() });

//   const { name, phone, current_ctc, expected_ctc, notice_period, experience } = req.body;
//   try {
//     const [result] = await pool.query(
//       `INSERT INTO candidates 
//       (name, phone, current_ctc, expected_ctc, notice_period, experience) 
//       VALUES (?, ?, ?, ?, ?, ?)`,
//       [name, phone, current_ctc, expected_ctc, notice_period, experience]
//     );
//     res.json({ id: result.insertId, message: 'Candidate created' });
//   } catch (err) {
//     res.status(500).json({ error: err.message });
//   }
// });

// // Appointment Booking
// app.post('/appointments', [
//   body('job_id').isInt(),
//   body('candidate_id').isInt(),
//   body('date_time').notEmpty(),
// ], async (req, res) => {
//   const errors = validationResult(req);
//   if(!errors.isEmpty()) return res.status(400).json({ errors: errors.array() });

//   const { job_id, candidate_id, date_time } = req.body;
//   try {
//     // Basic availability check
//     const [existing] = await pool.query(
//       'SELECT * FROM appointments WHERE job_id = ? AND date_time = ? AND status = "confirmed"',
//       [job_id, date_time]
//     );
//     if(existing.length > 0) return res.status(409).json({ error: 'Slot already booked' });

//     const [result] = await pool.query(
//       'INSERT INTO appointments (job_id, candidate_id, date_time, status) VALUES (?, ?, ?, ?)',
//       [job_id, candidate_id, date_time, 'confirmed']
//     );
//     res.json({ id: result.insertId, message: 'Appointment booked' });
//   } catch (err) {
//     res.status(500).json({ error: err.message });
//   }
// });

// // Conversation logs (append transcript)
// app.post('/conversations', [
//   body('candidate_id').isInt(),
//   body('transcript').notEmpty(),
//   body('entities_extracted').optional(),
// ], async (req, res) => {
//   const { candidate_id, transcript, entities_extracted } = req.body;
//   try {
//     const [result] = await pool.query(
//       'INSERT INTO conversations (candidate_id, transcript, entities_extracted) VALUES (?, ?, ?)',
//       [candidate_id, transcript, entities_extracted || null]
//     );
//     res.json({ id: result.insertId, message: 'Conversation logged' });
//   } catch (err) {
//     res.status(500).json({ error: err.message });
//   }
// });

// // Start server
// const PORT = process.env.PORT || 4000;
// app.listen(PORT, () => {
//   console.log(`Server running on port ${PORT}`);
// });
