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
import logging

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
MASTER_PORT = 3000


logging.basicConfig(filename='slave.log', filemode='w', level=logging.DEBUG,
                    format='DB event:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class SlaveUpdater(replicator_pb2.ReplicatorServicer):
    """Slave Class"""
    debug = 0
    def __init__(self, host):
        self.slave_db = rocksdb.DB("slave.db", rocksdb.Options(create_if_missing=True))
        self.channel = grpc.insecure_channel('%s:%d' % (host, MASTER_PORT))
        self.stub = replicator_pb2.ReplicatorStub(self.channel)


    def get_updates(self):
        """Get updates from master"""
        responses = self.stub.update_slave(replicator_pb2.Request(data="Send me data!"))
        for resp in responses:
            print(resp)
            if resp.method_type == "put":
                SlaveUpdater.debug = SlaveUpdater.debug + 1
                logging.debug(str(SlaveUpdater.debug) + "," + "put" +"," + resp.key + "," + (resp.value).strip("\n"))
                self.put(resp.key, resp.value)
            elif resp.method_type == "delete":
                SlaveUpdater.debug = SlaveUpdater.debug + 1
                logging.debug(str(SlaveUpdater.debug) + "," + "delete" +"," + resp.key + "," + "")
                self.delete(resp.key)
            else:
                print("Nothing to do")


    def put(self, key, value):
        """Put in Slave DB"""
        self.slave_db.put(key.encode(), value.encode())

    def delete(self, key):
        """Delte from Slave DB"""
        self.slave_db.delete(key.encode())

def main():
    '''
    Run the Slave
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="the ip of the server")
    args = parser.parse_args()
    host=args.host
    print(host)
    print("Slave is connecting to Server at {}:{}...".format(args.host, MASTER_PORT))
    slave = SlaveUpdater(host)

    try:
        while True:
            time.sleep(10*60)
            slave.get_updates()
    except KeyboardInterrupt:
        sys.exit("Slave Stopped")

if __name__ == '__main__':
    main()
