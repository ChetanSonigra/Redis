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
24. `hset key field1 value1 [field2 value2 ...]`: &emsp; creates key if not exist else adds in existing key pairs of key-value.
25. `hget key field`: &emsp; gives value of a field in a key/hash
26. `hmget key field1 field2 ...`:&emsp; gives values of fields in a key/hash
27. `hmset key field1 value1 [field2 value2 ...]`:&emsp; similar to hset, deprecated.
28. `sadd users_ip ip1 ip2 ...`:&emsp; adds values into set
29. `smembers users_ip`:&emsp; shows all members of set
30. `scard users_ip`: &emsp;length of a set
31. `sismember users_ip ip1`: &emsp;checks if member is in set
31. `sdiff set1 set2`:&emsp; members of set1-set2
31. `spop setname [count]`:&emsp; pops one or more random members from a set.
32. `srem setname memeber`:&emsp; removes a member from a set.
33. `watch key`:&emsp; watches a key during multi transaction
34. `multi`:&emsp; to start multiple transaction
35. `exec`:&emsp; to run all commands in a transaction
36. `discard`:&emsp; to discard a transaction 
37. `sentinel master master_name`: &emsp; gives master node details.
38. `slaveof ip_address port`: &emsp; makes a redis slave slave of node having given ip and port.
39. `save`: &emsp; saves current data in dump.rdb in redis-server.

## Data Persistence:

1. RDB:&emsp; Performs point in time snapshot of data at specified interval of time. <br/>
&emsp;&emsp; save 60 1000 30 500(if every 60 seconds 1000 keys, or 30 seconds 500 keys) <br/>
&emsp;&emsp; dir path/to/dir/to_save/redis_dump.rdb <br/>
&emsp;&emsp; add above 2 line in redis.conf <br/>
&emsp;&emsp; Advantages: <br/>
&emsp;&emsp; - Compact, single file of redis data<br/>
&emsp;&emsp; - Perfect for backups<br/>
&emsp;&emsp; - Performance is good<br/>
&emsp;&emsp; - Allows faster restarts<br/>
&emsp;&emsp; Disadvantages: <br/>
&emsp;&emsp; - Chances of data loss <br/>
&emsp;&emsp; - Fork process, may impact write operations for few milliseconds.<br/>

2. AOF:&emsp; Append Only File - Keeps log of every write operations in redis. <br/>
&emsp;&emsp; Define fsycn policies, always, everysec <br/>
&emsp;&emsp; appendonly yes <br/>
&emsp;&emsp; Add above line in redis.conf <br/>
&emsp;&emsp; Advantages: <br/>
&emsp;&emsp; - High Durability <br/>
&emsp;&emsp; - Allows different fsync policies <br/>
&emsp;&emsp; - Append only logs, no chances of corruption <br/>
&emsp;&emsp; - Corrupted files can be fixed by redis-check-aof tool <br/>
&emsp;&emsp; - AOF files can be parsed, lines can be removed. <br/>
&emsp;&emsp; Disadvantages: <br/>
&emsp;&emsp; - Size is bigger than RDB <br/>
&emsp;&emsp; - Slower than RDB <br/>

3. Hybrid:&emsp; (RDB+AOF) - Both can work together.:

## Replication:
- Add `replicaof master_ip master_port` in slave's redis.conf file.
- change port, logfilename, dump.rdb file name for slaves in redis.conf file.
- Run redis server for master and slaves.
- slaves can only be used to read data.

## High Availability:
- Install sentinel on minimum 3 servers.
- Quorum (No. of sentinel which needs agree on master down and elect a new master)
- down-after milliseconds
- Redis port = 6379, Sentinel port = 26379
- redis.conf, sentinel.conf 
1. Sentinel Deployment 01: <br>
    - Never do this deployment
    - 2 sentinels, 1 master 1 slave
    - quorum =2 
    - Only works if redis is down but sentinels are working on both servers.
    - if complete box is down,redis will become unavailable.
2. Sentinel Deployment 02: <br>
    - 3 sentinels, 1 master, 2 slaves
    - Quorum = 2
    - Good approach if we have min 3 servers.
    - issues:
    - &emsp; 1. If nodes are seperated by network partition
    - &emsp; Mitigation - min-replica-to-write 1 (stops writes if can't write to replica), min-replicas-max-lag 10
    - &emsp; 2. If two replicas are down, master stops accepting writes.

3. Sentinel Deployment 03: <br>
    - 3 sentinels(on application server), 1 master 1 slave
    - Quorum 2
    - Good approach if we have only 2 redis servers.
    - Issue: 
    - &emsp; Network disconnect issue between redis server and application server.

4. Sentinel Deployment 04: <br>
    - 4 sentinels (2 on application server, 2 on redis server), 1 master, 1 redis
    - Quorum = 3
    - Good approach if we have min 3 servers.

## Redis Cluster:
- minimum 3 masters and 3 slaves needed.
- Multi master architecture
- Data is partitioned into 16k buckets.
- Each bucket are assigned a master.
- Pros:
- &emsp; Scalable
- &emsp; Can scale upto 1000 nodes cluster
- &emsp; Performance is good
- &emsp; Allows multiple masters
- Cons:
- &emsp; Need atleast 6 servers to setup a cluster
- &emsp; Upgrading or downgrading to other topology is difficult.

### Steps: 
1. create n1_redis.conf file with details as below in each node: <br>
&emsp; port 7001/7002/7003/7004/7005/7006 <br>
&emsp; cluster-enabled yes <br>
&emsp; cluster-config-file nodes.conf <br>
&emsp; cluster-node-timeout 5000 <br>
&emsp; appendonly yes <br>

2. Start redis-server on each node<br>
&emsp; redis-server n1_redis.conf & <br>

3. Create a cluster: <br>
&emsp; redis-cli --cluster create 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 
127.0.0.1:7004 127.0.0.1:7005 127.0.0.1:7006 --cluster-replicas 1 <br>

4. Connect to server: <br>
&emsp; redis-cli -c -p 7001

5. Check cluster health: <br>
&emsp; redis-cli --cluster check 127.0.0.1:7001 <br>
&emsp; redis-cli -p 7001 cluster nodes