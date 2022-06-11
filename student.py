import psycopg2
def connect():
    try:
        """ Connect to the PostgreSQL database server """
        conn = psycopg2.connect(
            host="localhost",
            database="school-management-system",
            user="postgres",
            password="12345")
        cur = conn.cursor()
        cur.execute("""
            select student_password from students
            where students_no=123
            """)
        info = cur.fetchone()
        print(info[0]=='234')
        cur.close()
        conn.commit()
    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

# def student_login():

if __name__ == '__main__':
    connect()