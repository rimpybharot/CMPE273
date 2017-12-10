How to run:

Make sure there are no transaction error, else the app will fail because not much exception handling has been done.

Tested with Docker, Dockefile is attached.

Run Server in Console 1:
sudo docker run --net=host -it --rm --name master -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python36-rocksdb-grpc:latest python3.6 master.py

Run Slave in Console 2:
sudo docker run --net=host -it --rm --name a2-slave2 -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python36-rocksdb-grpc:latest python3.6 slave.py 0.0.0.0

Run My_Client in Console 3:
sudo docker run --net=host -it --rm --name a2-client -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python36-rocksdb-grpc:latest python3.6 my_client.py 0.0.0.0




![alt text](https://github.com/rimpybharot/CMPE273/blob/master/assignment2/Replicator.png)
