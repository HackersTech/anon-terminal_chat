import socket
import threading
import subprocess
subprocess.call('',shell=True)
# Choosing Nickname
print("""\033[32m 
   ▄████▄   ██▓     ██▓ ▓█████ ███▄    █ ▄▄▄█████▓
  ▒██▀ ▀█   ██▒     ██▒ ▓█     ██ ▀█   █    ██▒ 
  ▒▓█    ▄  ██░     ██▒ ▒███   ██  ▀█ ██   ▓██░ 
  ▒▓▓▄ ▄██  ██░     ██░ ▒▓█    ██▒  ▐▌██   ▓██▓ 
    ▓███▀   ██████  ██░ ▒ ████ ██░   ▓██░  ▒██▒ 


  
\033[0m
hacKer X
""")
nickname = input("\033[38;5;22;48;5;227m Choose your nickname : \033[0m")
host=input('\033[34m enter host ip or ngrok link-: ')
# Connecting To Server
port=int(input('enter port -: '))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print('\n',message)
        except:
            # Close Connection When Error
            print("\033[31m error ")
            client.close()
            break
# Sending Messages To Server
def write():
    while True:
        message = '\033[38;5;40m {}: {}\033[0m'.format(nickname, input(''))
        client.send(message.encode('ascii'))
# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
