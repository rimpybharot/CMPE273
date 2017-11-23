'''
################################## server.py #############################
# Assignmnet2 gRPC RocksDB Server
################################## server.py #############################
'''
import time
import grpc
import replicator_pb2
import replicator_pb2_grpc
import uuid
import rocksdb
import encodings
from Replicator import my_decorator
import logging
import filereader

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


logging.basicConfig(filename='master.log', level=logging.DEBUG,
                    format='DB write event:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


# @my_decorator
# def replicator(key, value, debug_count):

#     print("Calling Put Replicator with " + key + " " + value)
#     master_db = rocksdb.DB("master1.db", rocksdb.Options(create_if_missing=True))
#     master_db.put(key.encode(), value.encode())
#     debug_count = debug_count + 1
#     logging.debug(str(debug_count) + "," + key + "," + value)
#     return key


class MyReplicatorServicer(replicator_pb2.ReplicatorServicer):
    def __init__(self):
        self.master_db = rocksdb.DB("master.db", rocksdb.Options(create_if_missing=True))
        self.debug_count = 0
        self.key = 0

    def my_decorator(self, function):
        """Decorator Method"""
        def wrapper(*args, **kwargs):
            """Extra Wrapping"""
            method_type = function.__name__
            if method_type == "put":
                value = args[0]
                self.key = uuid.uuid4().hex
            elif method_type == "delete":
                value = ''
                self.key = args[0]
            # elif method_type == "update":
            #     self.key = args[0]
            #     value = args[1]

            debug_count = self.debug_count + 1
            logging.debug(str(debug_count) + "," + str(method_type) +"," + self.key + "," + value)
            return function(*args, **kwargs)

        return wrapper

    @my_decorator
    def put(self, request, context):
        """Put data in db"""
        value = request.data
        self.master_db.put(self.key.encode(), value.encode())
        return replicator_pb2.Response(data=self.key)

    # @my_decorator
    # def update(self, request, context):
    #     """Get data from DB"""
    #     self.master_db.put(request.key.encode(), request.value.encode())
    #     return replicator_pb2.Response(data=request.key)

    @my_decorator
    def delete(self, request, context):
        """Get data from DB"""
        return replicator_pb2.Response(data=(self.master_db.delete(request.data.encode())).decode())

    def get(self, request, context):
        """Get data from DB"""
        return replicator_pb2.Response(data=(self.master_db.get(request.data.encode())).decode())

    def update_slave(self, request, context):
        """Update the Slave"""
        print(request.data)

        last_slave = filereader.comparator()

        if last_slave != -1:
            fileop = open("master_db.log", "r+")
            lines = list(fileop)
            if lines:
                for line in lines:
                    index = (line.split(",")[0]).split(":")[1]
                    if int(index) >= int(last_slave)+1:
                        method_type = line.split(",")[1]
                        key = line.split(",")[2]
                        value = line.split(",")[3]
                        print("Yield to Slave")
                        yield replicator_pb2.Updates(
                            method_type = method_type,
                            key = key,
                            value = value
                        )

        else:
            print("Slave is Up To Date!")

def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    replicator_pb2_grpc.add_ReplicatorServicer_to_server(MyReplicatorServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()
    print("Server started at...%d" % port)

if __name__ == '__main__':
    run('0.0.0.0', 3000)