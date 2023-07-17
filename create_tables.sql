-- Таблиця груп
CREATE TABLE groups (
    group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL
);

-- Таблиця студентів
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES groups(group_id)
);

-- Таблиця викладачів
CREATE TABLE teachers (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);
-- Таблиця предметів
CREATE TABLE subjects (
    subject_id SERIAL PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

-- Таблиця оцінок
CREATE TABLE grades (
    grade_id SERIAL PRIMARY KEY,
    student_id INT,
    subject_id INT,
    grade FLOAT NOT NULL,
    date_received DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);