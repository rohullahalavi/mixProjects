
import redis
import time


#create a connection to the redis server on localhost port 6379 with db 0
r = redis.StrictRedis(host='localhost', port=6379, db=0)


#create a function to get the current time
def get_time():
    #get the current time from the system
    current_time = time.time()
    #convert the current time to a string
    current_time_string = str(current_time)
    #return the current time string
    return current_time_string


#create a function to get the current date
def get_date():
    #get the current date from the system
    current_date = time.strftime("%Y-%m-%d")
    #return the current date string
    return current_date


#create a function to get the current date and time
def get_date_time():
    #get the current date and time from the system
    current_date_time = time.strftime("%Y-%m-%d %H:%M:%S")
    #return the current date and time string
    return current_date_time


#create a fake db for testing redis data storage
fake_db = {
    'time': get_time(),
    'date': get_date(),
    'date_time': get_date_time()
} 

#store the dict in redis database with key using loop store the values in the list 






#get all redis keys and values and print 
keys = r.keys()
values = r.mget(keys)
print(keys)
print(values)






















