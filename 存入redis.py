import redis
pool = redis.ConnectionPool(host='127.0.0.1',port=6379,password='',db=0)#创建连接池
redis_conn = redis.Redis(connection_pool=pool)#获取连接对象

redis_conn.set('ywm', 'test1')


# redis_conn.hmset('ywm6', {'k1':'v1', 'k2': 'v2'})


# def read_redis(redis_conn, d_id):
#     redis_key = 'pact-fileparse-%s' % d_id
#     redis_value = eval(redis_conn.get(redis_key).decode("utf-8"))[1][0]
#     json_data = json.loads(redis_value)
#     json.dump(json_data, open(raw_data_path, 'w', encoding='utf-8'), indent=4, ensure_ascii=False)

