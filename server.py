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

            # save the file and write key in file
            with open('encrypted_Symmetric_Key.key', 'wb') as esk:
                esk.write(encrypted_symentric_key)

            # with open (Secret_key, 'rb') as f:
            #     symentric = f.read()
            break       

# reaad the private key
with open ("D:\conestoga\cryptography\Assignment_1\private_key.key", 'rb') as pb:
    pb = serialization.load_pem_private_key(pb.read(), password=None)
           
# this command decrypt encrypt_symentric_key using private key
decrypted_symmetric_Key = pb.decrypt(encrypted_symentric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

# write the decrypt key in file for decrypt the encrypt_file
with open ('decrypt_symentric_key.key', 'wb') as d:
    d.write(decrypted_symmetric_Key)
                        
print('connection completed and key recived')
        