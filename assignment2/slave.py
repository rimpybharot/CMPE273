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
import argparse
import sys

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
MASTER_PORT = 3000

class SlaveUpdater(replicator_pb2.ReplicatorServicer):
    """Slave Class"""
    def __init__(self, host):
        self.slave_db = rocksdb.DB("slave.db", rocksdb.Options(create_if_missing=True))
        self.master_channel = grpc.insecure_channel('%s:%d' % (host, MASTER_PORT))
        self.stub = replicator_pb2.ReplicatorServicer(self.master_channel)

    def get_updates(self):
        """Get updates from master"""
        resp = self.stub.update_slave("Requesting Updates!")
        if resp.method_type == "put":
            self.put(resp.key, resp.val)
        elif resp.method_type == "delete":
            self.delete(resp.key)

    def put(self, key, value):
        """Put in Slave DB"""
        self.slave_db.put(key.encode(), value.encode())

    def delete(self, key):
        """Delte from Slave DB"""
        self.slave_db.delete(key.encode())

def main():
    '''
    Run the GRPC server
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="the ip of the server")
    args = parser.parse_args()
    print("Slave is connecting to Server at {}:{}...".format(args.host, MASTER_PORT))
    slave = SlaveUpdater(host=args.host)

    try:
        while True:
            slave.get_updates()
            time.sleep(5*60)
    except KeyboardInterrupt:
        sys.exit("Slave Stopped")

if __name__ == '__main__':
    main()
