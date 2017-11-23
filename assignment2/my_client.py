import time
import grpc
import replicator_pb2
import replicator_pb2_grpc
import uuid
import rocksdb
import encodings
import argparse
import sys

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
MASTER_PORT = 3000

class MyClient(replicator_pb2.ReplicatorServicer):
    """Slave Class"""
    def __init__(self, host, port):
        self.channel = grpc.insecure_channel('%s:%d' % (host, MASTER_PORT))
        self.stub = replicator_pb2.ReplicatorStub(self.channel)


    # def get_updates(self):
    #     """Get updates from master"""
    #     resp = self.stub.update_slave(replicator_pb2.Request(data="Requesting Updates!"))
    #     if resp.method_type == "put":
    #         self.put(resp.key, resp.val)
    #     elif resp.method_type == "delete":
    #         self.delete(resp.key)
    #     else:
    #         return

    def get(self, key):
        """Put in Slave DB"""
        return self.stub.get(replicator_pb2.Request(data=key))

    def put(self, value):
        """Put in Slave DB"""
        return self.stub.put(replicator_pb2.Request(data=value))

    def delete(self, key):
        """Delte from Slave DB"""
        return self.stub.delete(replicator_pb2.Request(data=key))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="the ip of the host")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, MASTER_PORT))
    client = MyClient(host=args.host, port=MASTER_PORT)
    
    value = 'foo'
    print("## PUT Request: value = " + value) 
    resp = client.put(value)
    key = resp.data
    print("## PUT Response: key = " + key)

    print("## GET Request: key = " + key) 
    resp = client.get(key)
    print("## GET Response: value = " + resp.data)

    print("## DELETE Request: key = " + key) 
    resp = client.delete(key)
    print("## DELETE Response: key deleted" + resp.data) 


if __name__ == "__main__":
    main()