import time
import threadpool
import numpy as np

def add(num1, num2):
    print num1 + num2
    time.sleep(1)


num1 = list(np.random.randint(low=0, high=50, size=100))
num2 = list(np.random.randint(low=0, high=50, size=100))
params = [(item, None)for item in zip(num1, num2)]
start_time = time.time()
pool = threadpool.ThreadPool(10)
requests = threadpool.makeRequests(add2, params)
[pool.putRequest(req) for req in requests] 
pool.wait() 
print '%d second'% (time.time()-start_time)

