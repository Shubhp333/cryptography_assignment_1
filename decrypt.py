import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransomeware.py" or file == "server.py" or file == "decrypt.py" or file == "random_key.txt":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

key = input("enter the key:")

for file in files:
    with open (file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)