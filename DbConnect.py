from logging import exception
import psycopg2
class DBConnection():

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="school-management-system",
                user="postgres",
                password="Merve3467.")
            self.cur = self.conn.cursor()
            
            # cur.close()
            # conn.commit()
        except (Exception) as error:
            print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()
    def checkStudent(self,students_no,password):
            self.cur.execute("""
            select * from students where students_no={} and student_password='{}' """.format(students_no,password),
            )
        
            student = self.cur.fetchall()
            return student
           
