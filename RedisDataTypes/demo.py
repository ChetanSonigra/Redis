import redis
import dotenv, os

dotenv.load_dotenv()
r = redis.StrictRedis(host=os.getenv('host'),port=os.getenv('redis_port'))

print(r)

print(r.set("course:1","Python"))
print(r.set("course:2","Redis"))
print(r.set("course:3","Django"))

var1 = r.get('course:1')
var2 = r.get('course:2')
var3 = r.get('course:3')

print(var1,var2,var3)