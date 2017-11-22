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
from Replicator import put_decorator
from Replicator import get_decorator
import logging
import filereader

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


slave_port = 3000


#debug_count=0
logging.basicConfig(filename='master.log', level=logging.DEBUG,
                    format='DB write event:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


@put_decorator
def put_replicator(key, value, debug_count):

    print("Calling Put Replicator with " + key + " " + value)
    master_db = rocksdb.DB("master1.db", rocksdb.Options(create_if_missing=True))
    master_db.put(key.encode(), value.encode())
    debug_count = debug_count + 1
    logging.debug(str(debug_count) + "," + key + "," + value)
    return key

# @get_decorator
# def get_replicator(key):

#     print("Calling Get Replicator with " + key + " ")

#     master_db = rocksdb.DB("master1.db", rocksdb.Options(create_if_missing=True))
#     value = (master_db.get(key.encode())).decode()
#     print("Value of " + key + " in Master DB is " + value)
#     return value


class MyReplicatorServicer(replicator_pb2.ReplicatorServicer):
    def __init__(self):
        # self.master_db = rocksdb.DB("master1.db", rocksdb.Options(create_if_missing=True))
        self.debug_count = 0

    def put(self, request, context):

        # print("put")
        key = uuid.uuid4().hex
        value = request.data
        # self.master_db.put(key.encode(), value.encode())
        # m.replicator()
        return replicator_pb2.Response(data=put_replicator(key, value, self.debug_count))

    def get(self, request, context):
        print("get")

        master_db = rocksdb.DB("master1.db", rocksdb.Options(create_if_missing=True))

        return replicator_pb2.Response(data=(master_db.get(request.data.encode())).decode())


def check_difference(server, slave1):
    try:
        while True:
            filereader.comparator()
            time.sleep(5*60)
    except KeyboardInterrupt:
        server.stop(0)
        slave1.stop(0)





def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    replicator_pb2_grpc.add_ReplicatorServicer_to_server(MyReplicatorServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()
    print("Server started at...%d" % port)

    slave_channel = grpc.insecure_channel('%s:%d' % (host, slave_port))
    slave_stub = replicator_pb2.ReplicatorStub(slave_channel)



    slave1 = grpc.slave1(futures.ThreadPoolExecutor(max_workers=1))
    replicator_pb2_grpc.add_ReplicatorServicer_to_server(MyReplicatorServicer(), slave1)
    slave1.add_insecure_port('%s:%d' % (host, slave_channel))
    slave1.start()
    print("Server started at...%d" % slave_port)


    check_difference(server, slave1)




if __name__ == '__main__':
    run('0.0.0.0', 3000)