import time
import threadpool
import numpy as np
import logging
from logging.handlers import RotatingFileHandler

formatter = logging.Formatter('%(name)-12s %(asctime)-12s [line:%(lineno)d] %(levelname)-8s %(message)s', '%Y-%m-%d %H:%M:%S',)
file_handler = RotatingFileHandler('./app.log', maxBytes=10 * 1024 * 1024, backupCount=5)
file_handler.setFormatter(formatter)

logger = logging.getLogger("Add")
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)



def add(num1, num2):
    print num1+num2
    logger.info(num1+num2)
    time.sleep(1)


num1 = list(np.random.randint(low=0, high=50, size=100))
num2 = list(np.random.randint(low=0, high=50, size=100))
params = [(item, None)for item in zip(num1, num2)]
start_time = time.time()
pool = threadpool.ThreadPool(10)
requests = threadpool.makeRequests(add, params)
[pool.putRequest(req) for req in requests] 
pool.wait() 
print '%d second'% (time.time()-start_time)



