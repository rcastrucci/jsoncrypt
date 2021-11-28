from jsoncrypt import Encrypt, Decrypt

# FORMULAS TO ENCRYPT AND DECRYPT
# Encrypt.jsonfile(json_filename_to_encrypt)
# Encrypt.jsonstring(json_string_to_encrypt)
# Encrypt.dictionary(a_dictionary_to_encrypt)
# Decrypt.jsonfile(filename_encrypted)
# Decrypt.jsonstring(json_string_encrypted)
# Decrypt.dictionary(string_of_a_dictionary_encrypted)
# FOLLOWING SOME EXAMPLES

# SELECT A JSON FILE
filename = "./example.json"

# TO ENCRYPT FROM A FILE AND JUST GET AS A STRING WITHOUT SAVING IT
Encrypt.jsonfile(filename)
# IT WILL RETURN A STRING IF WAS A JSON FILE AND SUCCESS TO ENCRYPT OR
# IT WILL RETURN A NONE IF WASN'T A JSON FILE AND FAILED TO ENCRYPT
# FINALLY TO CATCH NOT JSON FILES USE
string_encrypted = Encrypt.jsonfile(filename)
if string_encrypted:
    print("Encrypted successfully")
    print(string_encrypted)
else:
    print("Not possible to encrypt non json files")

# TO ENCRYPT FROM A FILE AND SAVE FILE USE
# Encrypt.jsonfile(filename, save_file=True)
# IT WILL RETURN BOOLEAN TRUE IF WAS SUCCESS OR BOOLEAN FALSE IF FAILED TO SAVE
# FINALLY USE FORMULA TO CATCH NON JSON FILES OR NO PERMISSIONS TO SAVE ON DISK
if Encrypt.jsonfile(filename, save_file=True):
    print("File {} was successfully encrypted and has been saved!".format(filename))
else:
    print("Failed to encrypt file")

# DECRYPT INTO MEMORY TO USE DATA AS NECESSARY (HERE FILE USED MUST BE ENCRYPTED TO BE ABLE TO DECRYPT RIGHT!?)
# IF FILE IS NOT ENCRYPTED IT WILL RETURN A BOOLEAN FALSE
# TO DECRYPT AND GET AS DICTIONARY USE
dictionary = Decrypt.jsonfile(filename)
# TO DECRYPT AND GET AS STRING USE
string_decrypted = Decrypt.jsonfile(filename, output="string")
# TO DECRYPT AND GET AS STRING AND CHANGE INDENT USE (DEFAULT INDENT IS 4)
string_indented = Decrypt.jsonfile(filename, output="string", indent=2)

# TO DECRYPT FROM A FILE AND SAVE IT
# IT WILL RETURN BOOLEAN TRUE IF WAS SUCCESSFULLY DECRYPTED OR BOOLEAN FALSE IF FAILED TO SAVE
# FINALLY USE FORMULA TO CATCH NON ENCRYPTED FILES OR NO PERMISSIONS TO SAVE ON DISK
if Decrypt.jsonfile(filename, save_file=True):
    print("File {} was successfully decrypted and has been saved!".format(filename))
else:
    print("File is not encrypted or it was modified")

# IT IS POSSIBLE ALSO TO ENCRYPT AND DECRYPT FROM A STRING
# IMPORTANT! STRING MUST BE ON A JSON TYPE FORMAT
my_json_string_encrypted = Encrypt.jsonfile(filename)
print("ENCRYPTED FROM A FILE INTO A STRING")
print(my_json_string_encrypted)
# TO DECRYPT A STRING ON FORMAT OF JSON USE
decrypted_jsonstring = Decrypt.jsonstring(my_json_string_encrypted)
if decrypted_jsonstring:
    print("DECRYPTED FROM A STRING INTO ANOTHER STRING")
    print(decrypted_jsonstring)
else:
    print("String is not encrypted or not in a json format")

# IS POSSIBLE TO ENCRYPT ALSO A DICTONARY TYPE
# ON ENCRYPT IT RETURN A STRING AND ON DECRYPT IT RETURN A DICTIONARY
mydict = {"Name": "GRC Algoritmos"}
encrypted_dict = Encrypt.dictionary(mydict)
# LET's SEE:
print("Encrypted Dictionary:")
print(encrypted_dict)
print(type(encrypted_dict))
print("Decrypted Dictionary:")
# DECRYPTED AS A DICTIONARY
decrypted_dict = Decrypt.dictionary(encrypted_dict)
print(decrypted_dict)
print(type(decrypted_dict))
# DECRYPTED AS A STRING
decrypted_string = Decrypt.jsonstring(encrypted_dict)
print(decrypted_string)
print(type(decrypted_string))

# IS POSSIBLE TO ENCRYPT A DICTONARY AND SAVE IN A FILE
# IT WILL RETURN A BOOLEAN TRUE IF WAS SUCCESSFULL SAVED OR BOOLEAN FALSE IF FAILED
# IF FILE EXISTS AS DEFAULT IT WILL RETURN FALSE BUT IS POSSIBLE TO ALLOW OVERWRITE JUST SET overwrite=True
mydict = {"Name": "GRC Algoritmos", "File": "Saved"}
if Encrypt.dictionary(mydict, save_file=True, filename="grc.json", overwrite=True):
    print("Successfully saved!")
else:
    print("Not possible to save")


# OPTIONS TO ENCRYPT AND DECRYPT A JSON FILE
# save_file="Boolean"  -> Saves the result into the same file
# save_file="Boolean"  -> Returns a Json object with the result without saving on the file
# password="str"       -> Add a password to the encryption (Using this option it will only decrypt with same password)
# sha256="Boolean"     -> Is set True by default - this option will encrypt password with sha-256 signature
# indent="int"         -> Set indent to Json file on decryption, by default is set to indent=4
