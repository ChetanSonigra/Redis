import redis,string,random


def load_data_to_redis(data):
    r = redis.StrictRedis("localhost",6379)

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
    r = redis.StrictRedis('localhost',6379)
    
    for idx in range(1,1001):
        course_entry = generate_random_course()
    
        key = f"course:{idx}"
        value = ', '.join(str(val) for val in course_entry)
        print(value)
        r.set(key,value,ex=60)

    print("1000 courses loaded into redis.")

if __name__=="__main__":
    sample_data = [
        ('Python','Chetan Sonigra',5000,24.99,4.7),
        ('Redis','ABC KFHS',2395,50.00,4.5),
        ('FASTAPI','Chetan Sonigra',4000,49.99, 4.4)
    ]

    load_courses_to_redis()
    load_data_to_redis(sample_data)