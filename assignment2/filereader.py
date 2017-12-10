import rocksdb
import logging

def comparator(logfile): 

    print("In compatarator") 
    f = open("master.log", "r+")
    lines = list(f)

    if(len(lines)>0):

        #print(list(f))
        lastlogmaster = lines[-1]
        last_master = lastlogmaster.split(",")[0]
        last_master = last_master.split(":")[1]
        # print(last_master)
    else:
        last_master=0


    f = open(logfile, "r+")
    lines = list(f)

    if(len(lines)>0):

        #print(list(f))
        lastlogslave = lines[-1]
        last_slave = lastlogslave.split(",")[0]
        last_slave = last_slave.split(":")[1]
        # print(last_slave)
    else:
        last_slave=0

    if last_master != last_slave:
        print("slave is behind by "  + str(int(last_master)-int(last_slave)) + " log entries")
        return (last_slave)
    else:
        print("both are same")
        return -1

# def update_slave(last_slave):
#     print("Updating slave starting from " + last_slave)
#     f = open("master_db.log", "r+")
#     lines = list(f);

#     if(len(lines)>0):
#         for line in lines:
#             index = (line.split(",")[0]).split(":")[1]
#             if int(index) >= int(last_slave)+1:
#                         key = line.split(",")[1]
#                         value = line.split(",")[2]
#                         print("Put data in Slave1 DB")
#                         slave1_db = rocksdb.DB("slave_.db", rocksdb.Options(create_if_missing=True))
#                         slave1_db.put(key.encode(), value.encode())
#                         logging.debug(str(index) + "," + key + "," + value)


#     else:
#         last_master=0



#if __name__ == "__main__":
#    comparator()
