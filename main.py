from passGen import passGen, passLen
from cryptoGraphy import encryption, decryption

password = passGen(passLen())
print(password)

hash, key = encryption(password)
print(hash)
print(key)

decript = decryption(key, hash)
print(decript)
