SELECT st.group_id, g.group_name, AVG(gr.grade) as avg_grade
FROM students st
JOIN grades gr ON st.student_id = gr.student_id
JOIN groups g ON st.group_id = $1
WHERE gr.subject_id = $2
GROUP BY st.group_id, g.group_name;