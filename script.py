from cryptography.fernet import Fernet


# generate the key for encryption and decryption method
def gen_key():

    key = Fernet.generate_key()

    with open("my_key.key", "wb") as my_key:
        my_key.write(key)


# load my key from dir
def load_key():
    return open("my_key.key", "rb").read()


# generate and write a new key
gen_key()

# load the key
key = load_key()

my_msg = "Hola magic code !!".encode()

# initialize the Fernet class
f = Fernet(key)

encrypted_msg = f.encrypt(my_msg)

print(encrypted_msg)

# decrypt this msg
decrypted_msg = f.decrypt(encrypted_msg)
print(decrypted_msg)