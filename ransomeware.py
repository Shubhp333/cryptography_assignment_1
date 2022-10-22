import socket
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# create a symentric key using fernet library
symentric_key = Fernet.generate_key()

# this command for save the fernet key
# with open("thekey.key", "wb") as thekey:
#     thekey.write(symentric_key)


# encrypt the file using symentric key
file = "D:\conestoga\cryptography\Assignment_1\client.txt"
with open (file, "rb") as client_file:
    content = client_file.read()
client_file_encrypted = Fernet(symentric_key).encrypt(content)
with open(file, "wb") as encrypt_file:
    encrypt_file.write(client_file_encrypted)

# this function read the public key in binary form
with open ("D:\conestoga\cryptography\Assignment_1\public_key.key", 'rb') as public_key:
    public_key = serialization.load_pem_public_key(public_key.read())

# this command encrypt symentric key using public key
    encrypted_Symmetric_Key = public_key.encrypt(symentric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

# this for server ID and port for send key to server
IP = "10.0.0.150"  
PORT = 333

# this command send encrypted symentric key to server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))
    print('successfuly connected')
    s.send(encrypted_Symmetric_Key)
    print('key sended')
    s.close()