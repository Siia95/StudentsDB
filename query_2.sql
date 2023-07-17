SELECT AVG(grade) AS average_grade
FROM grades
WHERE subject_id = $1 AND student_id IN (
    SELECT student_id
    FROM grades
    WHERE subject_id = $2
    ORDER BY grade DESC
    LIMIT 5
);
