# Redis
Redis fundamentals and working with redis through python

## Change default port of redis: 
    Modify /etc/redis/redis.conf file

## Redis is case sensitive for keys,values.
## Check $home/.rediscli_history for redis commands history.

## Important redis commands:

1. `redis-cli`: &emsp; CLI utility to run redis commands
2. `keys *`: &emsp; To get all key-values
3. `SET key value`: &emsp; To store key value
4. `GET key`: &emsp; To get value of a key
5. `redis-benchmark -q -n 1000`: &emsp; to benchmark requests
6. `dbsize`: &emsp; gives number of records
7. `flushall`: &emsp; removes all records
8. `SET course_name:1:chetan "Python, 9999, 4.7" ex 10`: &emsp;
    key= course_name:1:chetan
    value="Python, 9999, 4.7"
    expires in 10 seconds
9. `DEL key_name`: &emsp; Deletes a key
10. `incr key_name`: &emsp; increments a key value by one
11. `mset key value [key value ...]`:&emsp; to set multiple key,values at once
12. `mget key1 key2 ...`: &emsp; to get multiple values for key at once
13. `exists key1 key2 ...`:&emsp;checks if key exists or not
14. `ttl key`: &emsp;            gives time to live for a key until expires
15. `expire key seconds`: &emsp; to set expire for existing key
16. `persist key`: &emsp;        to remove expire
17. `lpush list_name value [value ....]`: &emsp; creates a list of values if not exists else adds values at top
18. `rpush list_name value [value ...]`: &emsp; creates a list of values if not exists else adds values at bottom
19. `lrange list_name 0 -1`: &emsp; gives all values of list from 0 to -1 both included.
20. `llen list_name`:&emsp; gives lenght of list_name.
21. `lpop list_name [count]`: &emsp; pops "count" item from top of a list.
22. `rpop list_name [count]`: &emsp; pops "count" item from bottm of a list.
23. `ltrim list_name start stop`: &emsp; keeps only values form start to stop in a list
24. `hset key field1 value1 [field2 value2 ...]`: creates key if not exist else adds in existing key pairs of key-value.
25. `hget key field`: gives value of a field in a key/hash
26. `hmget key field1 field2 ...`: gives values of fields in a key/hash
27. `hmset key field1 value1 [field2 value2 ...]`: similar to hset, deprecated.
28. `sadd users_ip ip1 ip2 ...`: adds values into set
29. `smembers users_ip`: shows all members of set
30. `scard users_ip`: length of a set
31. `sismember users_ip ip1`: checks if member is in set
31. `sdiff set1 set2`: members of set1-set2
31. `spop setname [count]`: pops one or more random members from a set.
32. `srem setname memeber`: removes a member from a set.
33. `watch key`: watches a key during multi transaction
34. `multi`: to start multiple transaction
35. `exec`: to run all commands in a transaction
36. `discard`: to discard a transaction 