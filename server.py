from email.headerregistry import Address
import socket
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

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

            # encrypt symentric key received from clientcode
            encrypted_symentric_key = conn.recv(1024)
            break     

# this is for decryption part  
print('connection completed and key recived')

# read the private key
with open ("D:\conestoga\cryptography\Assignment_1\private_key.key", 'rb') as pb:
    pb = serialization.load_pem_private_key(pb.read(), password=None)
           
# this command decrypt the encrypt_symentric_key using private key
decrypted_symentric_key = pb.decrypt(encrypted_symentric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))


# with open ("decrypted_symentric_key", 'wb') as dsk:
#     dsk.write(decrypted_symmetric_key)

IP = "10.0.0.150"  
PORT = 334

# this command send encrypted symentric key to server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))
    print('successfuly connected')
    s.send(decrypted_symentric_key)
    print('key sended')
    s.close()
                        

        