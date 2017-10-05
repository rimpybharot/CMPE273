'''
################################## server.py #############################
# Lab1 gRPC RocksDB Server 
################################## server.py #############################
'''
import time
import grpc
import datastore_pb2
import datastore_pb2_grpc
import uuid
import rocksdb
import encodings

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MyDatastoreServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        self.db = rocksdb.DB("lab1.db", rocksdb.Options(create_if_missing=True))

    def put(self, request, context):
        print("put")
        key = uuid.uuid4().hex
        # save key and value into DB converting request.data string to utf-8 bytes 
        '''Rocksdb works on bytes hence it can not comprehend the string.
        First we need to extract the data from the request which is a string,
        and then we use encodings libraary to encode it to bytes.
        Finally provide the encoded byte value to the db , alongwith the encoded value
        of the key. Do db.put to add the key-value into the database.
        '''
        self.db.put(key.encode(), request.data.encode());
        return datastore_pb2.Response(data=key)

    def get(self, request, context):
        print("get")
        # retrieve the value from DB by the given key. Needs to convert request.data string to utf-8 bytes. 
        '''Rocksdb works on bytes hence it can not comprehend the string.
        First we need to extract the data from the request which is a string,
        and then we use encodings libraary to encode it to bytes.
        Finally provide the encoded byte value to the db , alongwith the encoded value
        of the key. Do db.get to get the value from the database for the key provided by user.
        The value returned will be in bytes and hence we need to decode it to the string.
        We use encodings library to decode the value retrieved from the data and send it as response.
        '''
        value = (self.db.get(request.data.encode())).decode();
        return datastore_pb2.Response(data=value)

def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    datastore_pb2_grpc.add_DatastoreServicer_to_server(MyDatastoreServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('0.0.0.0', 3000)