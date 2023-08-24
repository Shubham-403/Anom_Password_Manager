from cryptography.fernet import Fernet

# def keyGen():
#     key = Fernet.generate_key()
#     fernetObj = Fernet(key)
#     return fernetObj

# def str2Byte(string):
#     byte = string.encode()
#     return byte

# def byte2Str(byte):
#     string = byte.decode()
#     return string

# def encrypter(fernetObj, data):
#     cipher = fernetObj.encrypt(data)
#     return cipher

# def decrypter(fernetObj, data):
#     byteString = fernetObj.decrypt(data)
#     string = byte2Str(byteString)
#     return string

# def encryption(string):
#     key = keyGen()
#     data = str2Byte(string)
#     hash = encrypter(key, data)
#     return hash, key

# def decryption(key, hash):
#     decripted = decrypter(key, hash)
#     return decripted

class cryptoGraphy:
    @staticmethod
    def genKey():
        key = Fernet.generate_key()
        return key

    def encrypt(key, data):
        encodedData = data.encode()
        fernetObj = Fernet(key)
        encryptedData = fernetObj.encrypt(encodedData)
        return encryptedData

    def decrypt(key, encryptedData):
        fernetObj = Fernet(key)
        decryptedData = fernetObj.decrypt(encryptedData)
        decodedencryptedData = decryptedData.decode()
        return decodedencryptedData
    
