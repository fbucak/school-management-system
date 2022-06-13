select subjects.subject_name,students.students_no,students.first_name,students.last_name,teachers.first_name as teacher_name  from teachers
inner join teacher_subject on teacher_subject.teacher_id=teachers.teacher_id
inner join subjects on subjects.subject_id=teacher_subject.subject_id
inner join student_subject on student_subject.subject_id=subjects.subject_id
inner join students on students.student_id=student_subject.student_id
where teachers.username='feyza53'


