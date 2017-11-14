'''
################################## server.py #############################
# Encoder Server encodes string and decodes integer back to the original
# string. It can be used to generate unique id for a given URL.
################################## server.py #############################
'''
import time
import grpc
import encoder_pb2
import encoder_pb2_grpc

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class EncoderServer(encoder_pb2.EncoderServicer):
    '''
    EncoderServer is the main class that handles encoding and decoding.
    '''

    def __init__(self):
        print("init")

    def encode(self, request, context):
        '''
        :return: encoder_pb2.EncodeResponse
        '''
        # TODO

        print("in server")
        shortURL = request.url
        my_id = 0

        for i in range(0, len(request.url)):
            if ('a' <= shortURL[i] and shortURL[i] <= 'z'):
                my_id = my_id*62 + ord(shortURL[i]) - ord('a')
            if ('A' <= shortURL[i] and shortURL[i] <= 'Z'):
                my_id = my_id*62 + ord(shortURL[i]) - ord('A') + 26
            if ('0' <= shortURL[i] and shortURL[i] <= '9'):
                my_id = my_id*62 + shortURL[i] - ord('0') + 52

        print("Encode:\n", request)
        return encoder_pb2.EncodeResponse(id = my_id)

    def decode(self, request, context):
        '''
        :return: encoder_pb2.DecodeResponse
        '''
        # TODO
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        my_id = request.id
        shorturl = ""

        while(my_id):
            my_id = int(my_id)
            id1 = int(my_id%62)
            char1 = characters[id1]
            shorturl = shorturl + char1
            my_id = my_id/62

        shorturl = shorturl[::-1]
        print("Decode:\n", request)
        return encoder_pb2.DecodeResponse(url=str(shorturl))

def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    encoder_pb2_grpc.add_EncoderServicer_to_server(EncoderServer(), server)
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
