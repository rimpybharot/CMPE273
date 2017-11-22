'''
################################## server.py #############################
# Lab1 gRPC RocksDB Server 
################################## server.py #############################
'''
import time
import grpc
import replicator_pb2
import replicator_pb2_grpc
import uuid
import rocksdb
import encodings

class Slave:
    def __init__(self):
        self.slave_db = rocksdb.DB("slave.db", rocksdb.Options(create_if_missing=True))

    def put(self, key, value):
        print("put")
        self.slave_db.put(key.encode(), value.encode());

    def get(self, key):
        print("get")
        value = (self.slave_db.get(key.encode())).decode();
        return value