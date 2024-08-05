import socket
import requests
import json
import pickle

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created successfully')

port=1255
s.bind(('',port))
print('socket binded to port %s' %(port))

s.listen(5)
print('socket is listening')

while True:
    c, addr = s.accept()
    print('connection received from ', addr)

    c.send('Welcome to COWIN Portal'.encode())

    pin=c.recv(1024).decode()
    date=c.recv(1024).decode()

    api_url=f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin}&date={date}"
    response = requests.get(api_url)

    # status=response.status_code
    # c.send(str(status).encode())
    # if(status==200):
    #     print("\ndata fetched succesfully\n")

    data=response.json()

    if(len(data["sessions"])==0):
        print("NO NEARBY VACCINATION CENTERS FOUND !")

    data_string = pickle.dumps(data, -1)
    c.send(data_string)

    c.close()
    break