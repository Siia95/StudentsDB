SELECT s.subject_id, s.subject_name
FROM subjects s
JOIN grades g ON s.subject_id = g.subject_id
JOIN teachers t ON s.teacher_id = t.teacher_id
WHERE g.student_id = $1 AND t.teacher_id = $2;
