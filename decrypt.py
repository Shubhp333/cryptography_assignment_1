from cryptography.fernet import Fernet

key = input("enter the key:")

# with open("D:\conestoga\cryptography\Assignment_1\private_key.key", 'rb') as p:
#     private_key = p.read()
# key_decrypt = private_key.decrypt(key)


with open ("D:\conestoga\cryptography\Assignment_1\client.txt", "rb") as thefile:
    contents = thefile.read()
contents_decrypted = Fernet(key).decrypt(contents)
with open("D:\conestoga\cryptography\Assignment_1\client.txt", "wb") as thefile:
    thefile.write(contents_decrypted)