select student_password,students_no,first_name,last_name,subjects.subject_name from students
inner join student_subject on students.student_id=student_subject.student_id
inner join subjects on student_subject.subject_id=subjects.subject_id
where students_no=123


