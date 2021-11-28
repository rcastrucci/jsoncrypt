import jsoncrypt

# TO ENCRYPT A JSON FILE - FOLLOW EXAMPLE
filename = "example.json"

# TO ENCRYPT AND SAVE FILE
if jsoncrypt.Encrypt.jsonfile(filename, save_file=True):
    with open(filename, "r") as file:
        encrypted_json = file.read()
        print(encrypted_json)

        print("encrypted_json type is -> {}".format(type(encrypted_json)))
        input("Press any key to see decrypted version working with a string")

        # TO USE DECRYPTION AS A STRING
        decrypted_json = jsoncrypt.Decrypt.jsonstring(encrypted_json)
        print(decrypted_json)
else:
    print("Something went wrong!")

input("Press any key to decrypt file and save it")

# TO DECRYPT AND SAVE FILE
if jsoncrypt.Decrypt.jsonfile(filename, save_file=True):
    with open(filename, "r") as file:
        decrypted_json = file.read()
        print(decrypted_json)

input("Press any key to encrypt from a file into memory")

# TO ENCRYPT WITHOUT SAVING IN A FILE
print(jsoncrypt.Encrypt.jsonfile(filename, save_file=False, output="json"))

# OPTIONS TO ENCRYPT AND DECRYPT A JSON FILE
# save_file="Boolean"  -> Saves the result into the same file
# save_file="Boolean"  -> Returns a Json object with the result without saving on the file
# password="str"       -> Add a password to the encryption (Using this option it will only decrypt with same password)
# sha256="Boolean"     -> Is set True by default - this option will encrypt password with sha-256 signature
# indent="int"         -> Set indent to Json file on decryption, by default is set to indent=4
