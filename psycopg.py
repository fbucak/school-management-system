import psycopg2
def connect():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="school-management-system",
            user="postgres",
            password="981")

        cur = conn.cursor()
        
        table=input("tablo:")
        


        if table=='students':
            student_no=int(input("student_no:"))
            password=input("password:")
            cur.execute("""
            select * from students where student_no={} and password_=MD5('{}')""".format(student_no,password),
            )
            student = cur.fetchall()
            if student==[]:
                print("wrong password or username")
            else:
                print(student)
        


        elif table=='teachers':
            teacher_no=input("teacher_no:")
            password=input("password:")
            cur.execute("""select * from teachers where teacher_no='{}' and password_=MD5('{}')""".format(teacher_no,password),
            )
            teacher = cur.fetchall()
            if teacher==[]:
                print("wrong password or username ")
            else:
                print("öğretmen bilgilerini ekrana basmalı burada artık!!!!!!!!!!")  
                


        cur.close()
        conn.commit()

    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()