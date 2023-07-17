SELECT subjects.subject_name
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
JOIN students ON grades.student_id = students.student_id
WHERE students.first_name = $1::VARCHAR AND students.last_name = $2::VARCHAR;

