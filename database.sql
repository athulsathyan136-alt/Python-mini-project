CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks INTEGER
);

INSERT INTO students (student_id, name, age, course, marks)
VALUES
(1, 'Amal', 22, 'Computer Engineering', 85),
(2, 'Rahul', 21, 'Computer Science', 78),
(3, 'Anu', 22, 'Data Science', 92),
(4, 'Arjun', 23, 'Computer Engineering', 67),
(5, 'Meera', 21, 'Artificial Intelligence', 88);