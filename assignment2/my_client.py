import argparse
import ReplicatorClient

PORT = 3000

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="the ip of the host")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = ReplicatorClient(host=args.host, port=PORT)
    
    value = 'foo'
    print("## PUT Request: value = " + value) 
    resp = client.put(value)
    key = resp.data
    print("## PUT Response: key = " + key)

    print("## GET Request: key = " + key) 
    resp = client.get(key)
    print("## GET Response: value = " + resp.data) 


if __name__ == "__main__":
    main()