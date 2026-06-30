from cryptography.fernet import Fernet

key = Fernet.generate_key() # symmetric key
# print(key)

cipher = Fernet(key)
# print(key)

msg = b"Hello, this is a secert!"
encrypted = cipher.encrypt(msg)
print("Encrypted: ", encrypted)

decrypted = cipher.decrypt(encrypted)
print("Decrypted: ", decrypted.decode())