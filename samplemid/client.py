'''
################################## client.py #############################
# Wallet Client calls a remote GRPC service to encrypt credit/debit cards
# data and decrypt token back to plain text card detail.
################################## client.py #############################
'''
import grpc
import wallet_pb2
import wallet_pb2
import wallet_pb2_grpc


class WalletClient(object):
    '''
    WalletClient encrypts and decrypts card info via GRPC's sub which internally calls
    the remote WalletServicer.
    '''

    def __init__(self, host='0.0.0.0', port=3000):
        '''
        Initializes GRPC channel and stud so that they can be used in encrypt and decrypt functions.
        '''
        # TODO
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = wallet_pb2.WalletStub(self.channel)

    def encrypt(self, plain_text):
        '''
        Encrypts raw card info via stub.
        :param self: the self reference
        :param plain_text: the card details in a dictionary, E.g. plain_text['card_holder_name']
            converts from plain_text => wallet_pb2.Card => wallet_pb2.CardEncryptRequest
        :return: return a protocol buffer card encrypted response.
        :rtype: wallet_pb2.CardEncryptResponse
        '''
        # TODO
        my_proto_wallet_card = wallet_pb2.Card(
                card_holder_name = plain_text['card_holder_name'],
                card_number = plain_text['card_number'],
                card_expiry_yyyymm = plain_text['card_expiry_yyyymm']
        )

        my_card_encrypt_request = wallet_pb2.CardEncryptRequest(card = my_proto_wallet_card)

        response = self.stub.encrypt(my_card_encrypt_request)
        return response


    def decrypt(self, _token):
        '''
        Decrypts _token via stub.
        :param self: the self reference
        :param _token: the encrypted token
        :return: return a protocol buffer card decrypted response.
        :rtype: wallet_pb2.CardDecryptResponse
        '''
        # TODO
        my_card_decrypt_request = wallet_pb2.CardDecryptRequest(token=_token)
        response = self.stub.decrypt(my_card_decrypt_request)
        return response




