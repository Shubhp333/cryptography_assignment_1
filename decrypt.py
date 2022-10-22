from cryptography.fernet import Fernet

# server send the decrypted symmetric key to client and client have to put key manually
key = input("enter the decrypt symmetric key for decrypt file :")

# this code decrypt the client file with the key
file_client = "D:\conestoga\cryptography\Assignment_1\client.txt"
with open (file_client, "rb") as thefile:
    contents = thefile.read()
contents_decrypted = Fernet(key).decrypt(contents)
with open(file_client, "wb") as thefile:
    thefile.write(contents_decrypted)