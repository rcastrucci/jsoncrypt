from Crypter.jsoncrypt import code, decode

# TO ENCRYPT A JSON FILE - FOLLOW EXAMPLE
filename = "./example.json"

# TO ENCRYPT AND SAVE FILE
if code(filename, save_file=True):
    with open(filename, "r") as file:
        encrypted_json = file.read()
        print(encrypted_json)

input("Press any key to see decrypted version")

# TO DECRYPT AND SAVE FILE
if decode(filename, save_file=True):
    with open(filename, "r") as file:
        decrypted_json = file.read()
        print(decrypted_json)

input("Press any key to see encryption as an object")

# TO USE ENCRYPTION AND DECRYPTION ONLY AS AN OBJECT WITHOUT SAVING RESULTS IN A FILE
encrypted_json = code(filename)
print(encrypted_json)



# OPTIONS TO ENCRYPT AND DECRYPT A JSON FILE
# save_file="Boolean"  -> Saves the result into the same file
# save_file="Boolean"  -> Returns a Json object with the result without saving on the file
# password="str"       -> Add a password to the encryption (Using this option it will only decrypt with same password)
# sha256="Boolean"     -> Is set True by default - this option will encrypt password with sha-256 signature
# indent="int"         -> Set indent to Json file on decryption, by default is set to indent=4
