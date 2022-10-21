import socket

IP = "10.0.0.150"  
PORT = 333  
print("server start")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connection from {addr} established')
    with conn:
        while True:
            Secret_key = conn.recv(1024)
            with open('random_key.txt', 'wb') as f:
                f.write(Secret_key)


                with open (random_key.txt, "rb") as thefile:
                     contents = thefile.read()
                contents_encrypted = Fernet(key).encrypt(contents)
                with open(file, "wb") as thefile:
                    thefile.write(contents_encrypted)


            break
        print('connection completed and key recived')