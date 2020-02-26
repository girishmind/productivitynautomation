import socket, time


server = '10.100.172.116'
port = 12345
is_connect = False
while not is_connect:
    try:
        print("Connecting...")
        client_socket = socket.socket()
        client_socket.connect((server,port))
        is_connect = True

    except:
        print("Retrying...")
        time.sleep(2)
        continue

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
send_msg = "{ \"" + host_name + "\" : \"" + host_ip+"\"}"
print("ClientAgent: Sending "+send_msg)
client_socket.send(send_msg)
client_socket.close()