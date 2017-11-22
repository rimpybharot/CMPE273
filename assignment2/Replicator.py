# from slave1 import Slave1
# from slave2 import Slave2

import rocksdb
import encodings



# class Replica:

#     def __init__(self):
#         print("Decorator")

#     def decorator(self, rep):
#         def wrapper():

#             key, value = rep()

#             #if((slave1.Slave1.get(key))!=value):
#             slave1.Slave1.put(self, key, value)
#             #if(slave2.Slave2.get(key)!=value):
#             slave1.Slave1.put(self, key, value)

#             print("Something is happening after some_function() is called.")

#         return wrapper

# class Replica:
# def my_decorator(argument):
def put_decorator(function):
    def wrapper(*args, **kwargs):

        key = (args[0])
        value = (args[1])

        print("Put data in Slave1 DB")
        slave1_db = rocksdb.DB("slave_1.db", rocksdb.Options(create_if_missing=True))
        slave1_db.put(key.encode(), value.encode())

        print("Put data in Slave2 DB")
        slave2_db = rocksdb.DB("slave_2.db", rocksdb.Options(create_if_missing=True))
        slave2_db.put(key.encode(), value.encode())

        # slv1 = Slave1()
        # slv2 = Slave2()


        # if((slv1.get(key))!=value):
        # slv1.put(key, value)
        # if(slv2.get(key)!=value):
        # slv2.put(key, value)

        
        # slv1.put(args[0], args[1])

        return function(*args, **kwargs)
    return wrapper

def get_decorator(function):
    def wrapper(*args, **kwargs):

        key = (args[0])

        slave1_db = rocksdb.DB("slave_1.db", rocksdb.Options(create_if_missing=True))
        print("Value of " + args[0] + " in Slave1 DB is " + (slave1_db.get(key.encode())).decode())
        slave2_db = rocksdb.DB("slave_2.db", rocksdb.Options(create_if_missing=True))
        print("Value of " + args[0] + " in Slave1 DB is " + (slave2_db.get(key.encode())).decode())
        return function(*args, **kwargs)

    return wrapper