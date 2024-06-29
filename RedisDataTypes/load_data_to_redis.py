import redis,string,random
import dotenv,os

dotenv.load_dotenv()

def load_data_to_redis(data):
    r = redis.StrictRedis(host=os.getenv('host'),port=os.getenv('redis_port'))

    for idx, course_data in enumerate(data):
        key = f"course:{idx+1}"
        value = ', '.join(str(val) for val in course_data)
        print(value)
        r.set(key,value,ex=60)

def generate_random_course():
    course_name = ''.join(random.choices(string.ascii_letters, k=random.randint(5,15)))
    instructor = ''.join(random.choices(string.ascii_letters,k=random.randint(5,10)))
    students_enrolled = random.randint(1000,20000)
    price = round(random.uniform(10.0, 99.99),2)
    rating = round(random.uniform(3.0,5.0),1)
    return course_name,instructor,students_enrolled,price,rating

def load_courses_to_redis():
    r = redis.StrictRedis(host=os.getenv('host'),port=os.getenv('redis_port'))
    
    for idx in range(1,1001):
        course_entry = generate_random_course()
    
        key = f"course:{idx}"
        value = ', '.join(str(val) for val in course_entry)
        print(value)
        r.set(key,value,ex=60)

    print("1000 courses loaded into redis.")

def get_data():
    r = redis.StrictRedis(host=os.getenv('host'),port=os.getenv('redis_port'))

    courses_list = r.mget(['course:1','course:2','course:3'])
    courses = []
    for course in courses_list:
        if course:
            course = str(course)[2:-1]
            course = course.split(',')
            courses.append(course)   
    if courses:
        return courses

if __name__=="__main__":
    sample_data = [
        ('Python','Chetan Sonigra',5000,24.99,4.7),
        ('Redis','ABC KFHS',2395,50.00,4.5),
        ('FASTAPI','Chetan Sonigra',4000,49.99, 4.4)
    ]

    # load_courses_to_redis()
    load_data_to_redis(sample_data)