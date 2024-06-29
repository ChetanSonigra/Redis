# Redis
Redis fundamentals and working with redis through python

## Change default port of redis: 
    Modify /etc/redis/redis.conf file

## Important redis commands:

1. `redis-cli`: CLI utility to run redis commands
2. `keys *`: To get all key-values
3. `SET key value`: To store key value
4. `GET key`: To get value of a key
5. `redis-benchmark -q -n 1000`: to benchmark requests
6. `dbsize`: gives number of records
7. `flushall`: removes all records
8. `SET course_name:1:chetan "Python, 9999, 4.7" ex 10`: 
    key= course_name:1:chetan
    value="Python, 9999, 4.7"
    expires in 10 seconds