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
import logging
from filereader import comparator

from concurrent import futures


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

logging.basicConfig(filename='master.log', filemode='w', level=logging.DEBUG,
                    format='DB event:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')



def my_decorator(function):
    """Decorator Method"""
    
    def wrapper(*args, **kwargs):
        """Extra Wrapping"""

        # print("wrapping")
        method_type = function.__name__
        if method_type == "put":
            value = args[1].data
            print(value)
            MyReplicatorServicer.key = uuid.uuid4().hex
        elif method_type == "delete":
            value = ""
            MyReplicatorServicer.key = args[1].data
        # elif method_type == "update":
        #     self.key = args[0]
        #     value = args[1]

        # debug_count = MyReplicatorServicer.debug_counter
        MyReplicatorServicer.debug_counter = MyReplicatorServicer.debug_counter + 1


        logging.debug(str(MyReplicatorServicer.debug_counter) + "," + str(method_type) +"," + str(MyReplicatorServicer.key) + "," + str(value))
        return function(*args, **kwargs)

    return wrapper



class MyReplicatorServicer(replicator_pb2.ReplicatorServicer):
    
    debug_counter = 0;
    key = 0;

    def __init__(self):
        self.master_db = rocksdb.DB("master.db", rocksdb.Options(create_if_missing=True))
        # self.debug_count = 0
        # self.key = 0

    # def my_decorator(function):
    #     """Decorator Method"""
       
    #     def wrapper(*args, **kwargs):
    #         """Extra Wrapping"""

    #         print("wrapping")
    #         method_type = function.__name__
    #         if method_type == "put":
    #             value = args[0]
    #             key = uuid.uuid4().hex
    #         elif method_type == "delete":
    #             value = ''
    #             key = args[0]
    #         # elif method_type == "update":
    #         #     self.key = args[0]
    #         #     value = args[1]

    #         debug_count = self.debug_count + 1
    #         logging.debug(str(debug_count) + "," + str(method_type) +"," + key + "," + value)
    #         return function(*args, **kwargs)

    #     return wrapper

    @my_decorator
    def put(self, request, context):
        """Put data in db"""
        # self.key = uuid.uuid4().hex
        value = request.data

        print("BAck to original")

        print(MyReplicatorServicer.key)
        self.master_db.put(MyReplicatorServicer.key.encode(), value.encode())
        return replicator_pb2.Response(data=MyReplicatorServicer.key)

    # @my_decorator
    # def update(self, request, context):
    #     """Get data from DB"""
    #     self.master_db.put(request.key.encode(), request.value.encode())
    #     return replicator_pb2.Response(data=request.key)

    @my_decorator
    def delete(self, request, context):
        """Delet data from DB"""

        self.master_db.delete(request.data.encode())
        return replicator_pb2.Response(data=request.data)

    def get(self, request, context):
        """Get data from DB"""
        return replicator_pb2.Response(data=(self.master_db.get(request.data.encode())).decode())

    def update_slave(self, request, context):


        """Update the Slave"""
        
        print("in master")
        print(request.data)

        data_to_yied = replicator_pb2.Updates(
            method_type = "put",
            key = "key",
            value = "value"
        )

        # for i in range(1, 100):
        #     yield data_to_yied

        
        last_slave = comparator(request.data+".log")

        if last_slave != -1:
            fileop = open("master.log", "r+")
            lines = list(fileop)
            if lines:
                for line in lines:
                    index = (line.split(",")[0]).split(":")[1]
                    if int(index) >= int(last_slave)+1:
                        method_type = line.split(",")[1]
                        key = line.split(",")[2]
                        value = line.split(",")[3]
                        print("Yield to Slave")
                        data_to_yied = replicator_pb2.Updates(
                            method_type = method_type,
                            key = key,
                            value = value
                        )
                        yield data_to_yied


        else:
            print("Slave is Up To Date!")
            data_to_yied = replicator_pb2.Updates(
                method_type = "",
                key = "",
                value = ""
            )
            yield data_to_yied




def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    replicator_pb2_grpc.add_ReplicatorServicer_to_server(MyReplicatorServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()
    try:
        while True:
            print ("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('0.0.0.0', 3000)
