import random

debug = False

#......................... 1 .................................
def generateKey():
    '''
Generate the cipher keys
 return a dictionary of the encryption keys
    '''
    cipherLetters = generateAllLetters()
    cipher = {}
    for letter in generateAllLetters():
        randomIndex = random.randint(0, len(cipherLetters) - 1)
        cipher[letter] = cipherLetters.pop(randomIndex)
    
    return cipher

#......................... 2 .................................
def generateDecryptKey(key):
    '''
Generate the key required to decrypt given the encryption key
   key - the encryption key
 returns a dictionary of the decryption keys
    '''
    decryptKey = {}
    for letter in key:
        decryptKey[key[letter]] = letter
    return decryptKey

#......................... 3 .................................
def encrypt(phrase, key):
    '''
Encrypt the phrase
   phrase - the phrase to encrypt
   key - the key to use
 returns the encrypted key
    '''
    out = ""
    for character in phrase:
        if character in key:
            letter = key[character]
            out += letter
        else:
            letter = character
            out+= letter
        
    return out

#......................... 4 .................................
def decrypt(phrase, key):
    out = ""
    for character in phrase:
        if character in key:
            letter = key[character]
            out += letter
        else:
            letter = character
            out+= letter
    return out

#==================================================
# Test code below this point DO NOT MODIFY
def generateAllLetters():
    '''
Generate a list of every letter A-Z and a-z
 returns the list of every letter
    '''
    allLetters = []
    for letter in range(ord('A'), ord('Z') + 1):
        allLetters.append(chr(letter))
    for letter in range(ord('a'), ord('z') + 1):
        allLetters.append(chr(letter))

    return allLetters

TESTS = ["Simple", "HELLO PYTHON", "Simple Encryption in Python is Fun!",
         "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"]

def testEncryptionKey():
    encryptionKey = generateKey()
    if len(encryptionKey) != 52:
        print("generateKey Failed: I expected the key to contain 52 entries, but it contained", len(encryptionKey))
    return encryptionKey

def testDecryptionKey(encryptionKey):
    decryptionKey = generateDecryptKey(encryptionKey)
    for key in decryptionKey:
        if key != encryptionKey[decryptionKey[key]]:
            print("generateDecryptKey() Failed: The values", decryptionKey[key], "and", key, "do not match in the encryption and decryption keys")
    return decryptionKey

def testEncryption(encryptionKey, decryptionKey):
    success = True

    for phrase in TESTS:
        encrypted = encrypt(phrase, encryptionKey)
        if (encrypted == phrase):
            success = False
            print("encrypt() Failed:  The phrase", phrase, "did not change!")

        decrypted = decrypt(encrypted, decryptionKey)
        if decrypted != phrase:
            success = False
            print("decrypt() Failed: You returned", decrypted, "for the input", encrypted, "but I expected", phrase)

        if debug:
            print("Original: ", phrase)
            print("Encrypted:", encrypted)
            print("Decrypted:", decrypted)
    if success:
        print("Simple Cipher Passed!")

# Only run this code below if this is called as the main, not imported
if __name__ == '__main__':
    encryptionKey = testEncryptionKey()
    decryptionKey = testDecryptionKey(encryptionKey)
    testEncryption(encryptionKey, decryptionKey)
