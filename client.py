import socket
import pickle

s=socket.socket()
port=1255
s.connect(('127.0.0.1', port))

print(s.recv(1024).decode())

pin=input("\nEnter the Pincode: ")
s.send(pin.encode())

print("\nEnter the date: ")
date=input("in DD-MM-YYYY format: ")
s.send(date.encode())

# status=s.recv(1024).decode()
# if(status=='200'):
#     print("\nvaccination centres fetched successfully\n")

data = pickle.loads(s.recv(1024444))
if(len(data["sessions"])==0):
    print("NO NEARBY VACCINATION CENTERS FOUND !")

for i in range(len(data["sessions"])):
    print("\nname                         : "+ data["sessions"][i]["name"])
    print("address                      : " + str(data["sessions"][i]["address"]))
    print("available_capacity           : " + str(data["sessions"][i]["available_capacity"]))
    print("available_capacity_dose1     : " + str(data["sessions"][i]["available_capacity_dose1"]))
    print("available_capacity_dose2     : " + str(data["sessions"][i]["available_capacity_dose2"]))
    print("fee_type                     : " + data["sessions"][i]["fee_type"])
    print("min_age_limit                : " + str(data["sessions"][i]["min_age_limit"]))
    print("slots                        : " + str(data["sessions"][i]["slots"]))
    print("vaccine                      : " + str(data["sessions"][i]["vaccine"]))
    print("\n")

s.close()