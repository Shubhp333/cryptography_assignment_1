import socket
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# IP and PORT for connect to the client
IP = "10.0.0.150"  
PORT = 333  

print("server start")

# this is for server connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connection from {addr} established')

    with conn:
        while True:
            encrypted_symentric_key = conn.recv(1024)
            break     

print('connection completed and key recived')

# read the private key in binary form
with open ("D:\conestoga\cryptography\Assignment_1\private_key.key", 'rb') as pb:
    pb = serialization.load_pem_private_key(pb.read(), password=None)
           
# this command decrypt the encrypt_symentric_key using private key
decrypted_symentric_key = pb.decrypt(encrypted_symentric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

# this is new port for receive connection from client
IP = "10.0.0.150"  
PORT = 334

# server send decrypted symentric key to the client system
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))
    print('successfuly connected')
    s.send(decrypted_symentric_key)
    print('key sended to client')
    s.close()
                        

        