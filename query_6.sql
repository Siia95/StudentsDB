SELECT student_id, first_name, last_name
FROM students
WHERE group_id = $1;
