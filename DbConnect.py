from logging import exception
import psycopg2
class DBConnection():

    def __init__(self):
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="school-management-system",
                user="postgres",
                password="12345")
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
        
            
           
