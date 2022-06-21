from logging import exception
import psycopg2
class DBConnection():

    def __init__(self):
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="school-management-system",
                user="postgres",
                password="Merve3467.")
            self.connection=conn
            # cur.close()
            # conn.commit()
        except (Exception) as error:
            print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()
    def checkStudent(self,students_no,password):
        try:
            cursor=self.connection.cursor()
            cursor.execute("""
            select * from students where students_no={} and student_password='{}' """.format(students_no,password),
            )
            student=cursor.fetchall()
            return len(student)!=0
        except Exception as e:
            print(e)
            return False
    def checkTeacher(self,Tusername,Tpassword):
        try:
            cursor=self.connection.cursor()
            cursor.execute("""
            select * from teachers where username='{}' and teacher_password='{}' """.format(Tusername,Tpassword),
            )
            teacher = cursor.fetchall()
            return len(teacher)!=0
        except Exception as e:
            print(e)
            return False
    def getStudentId(self,studentNo):
        try:
            cursor=self.connection.cursor()
            cursor.execute("""
            select student_id from students where students_no='{}' """.format(studentNo)
            )
            studentId = cursor.fetchone()
            return studentId[0]
        except Exception as e:
            print(e)
            return False
    def getTeacherId(self,username):
        try:
            cursor=self.connection.cursor()
            cursor.execute("""
            select teacher_id from teachers where username='{}' """.format(username)
            )
            teacherId = cursor.fetchone()
            return teacherId[0]
        except Exception as e:
            print(e)
            return False

    def getSubjectId(self,subjectName):
        try:
            cursor=self.connection.cursor()
            cursor.execute("""
            select subject_id from subjects where subject_name='{}' """.format(subjectName)
            )
            subjectId = cursor.fetchone()
            return subjectId[0]
        except Exception as e:
            print(e)
            return False
    

        
            
           
