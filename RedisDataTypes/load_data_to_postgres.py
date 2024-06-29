import psycopg2 as pg
import random,string
import dotenv, os
# cursor = conn.cursor()
dotenv.load_dotenv()
# query = """
#     CREATE TABLE courses (
#         course_name character varying(25) NOT NULL,
#         instructor character varying(100) NOT NULL,
#         students_enrolled integer,
#         price numeric(5,2),
#         rating numeric(2,1),
#         CONSTRAINT courses_pkey primary key (course_name,instructor)
#     )
# """

# cursor.execute(query)

# cursor.close()
# conn.commit()
# conn.close()


def generate_random_course():
    course_name = ''.join(random.choices(string.ascii_letters, k=random.randint(5,15)))
    instructor = ''.join(random.choices(string.ascii_letters,k=random.randint(5,10)))
    students_enrolled = random.randint(1000,20000)
    price = round(random.uniform(10.0, 99.99),2)
    rating = round(random.uniform(3.0,5.0),1)
    return course_name,instructor,students_enrolled,price,rating


def load_data_to_postgres(data,conn):
    cursor = conn.cursor()
    query = f"INSERT INTO courses VALUES "
    for course_data in data:
        query += f"{course_data},"

    query = query[:-1]
    print(query)
    cursor.execute(query)
    cursor.close()
    conn.commit()

def load_course_data_to_postgres(conn):
    cursor = conn.cursor()
    query = f"INSERT INTO courses VALUES "
    for idx in range(1,1001):
        course_entry = generate_random_course()
        query += f"{course_entry},"
    query = query[:-1]
    print(query)
    cursor.execute(query)
    cursor.close()
    conn.commit()

def get_postgres_data():
    conn = pg.connect(host=os.getenv('host'),
                      port=os.getenv('port'),
                      database=os.getenv('database'),
                      user=os.getenv('user'),
                      password=os.getenv('password'))
    cursor = conn.cursor()

    cursor.execute("select * from courses where course_name in ('Python','Redis','FASTAPI')")

    courses = cursor.fetchall()
    cursor.close()
    conn.close()
    return courses



if __name__=="__main__":
    conn = pg.connect(host=os.getenv('host'),
                      port=os.getenv('port'),
                      database=os.getenv('database'),
                      user=os.getenv('user'),
                      password=os.getenv('password'))

    sample_data = [
        ('Python','Chetan Sonigra',5000,24.99,4.7),
        ('Redis','ABC KFHS',2395,50.00,4.5),
        ('FASTAPI','Chetan Sonigra',4000,49.99, 4.4)
    ]

    load_course_data_to_postgres(conn)
    load_data_to_postgres(sample_data,conn)
    conn.close()

        