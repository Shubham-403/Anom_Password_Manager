from cryptography.fernet import Fernet

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
    
