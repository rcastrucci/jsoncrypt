# JsonCrypt
Encryption and Decryption of JSON files and Dictionaries

Lock the file and encrypt with a password signature SHA-256

The data will be randomicly encrypted with **24.883.200.000 different combinations.**
So the same data with same password will always look diferent.

The key to decrypt is divided in 5 parts, combined with a password and hashed with SHA-256.
So the only way to decrypt data is using the password.

Encrypt also **dictionaries with a password**, save as a file and decrypt as a dictionary or a string.

# **pip install jsoncrypt**
    pip install jsoncrypt

**HOW TO USE**

    from jsoncrypt import Encrypt, Decrypt

# Formula to encrypt and decrypt
    Encrypt.jsonfile(json_filename_to_encrypt)

    Encrypt.jsonstring(json_string_to_encrypt)

    Encrypt.dictionary(a_dictionary_to_encrypt)

    Decrypt.jsonfile(filename_encrypted)

    Decrypt.jsonstring(json_string_encrypted)

    Decrypt.dictionary(string_of_a_dictionary_encrypted)

# Following some code samples

**Select a Json File**
    
    filename = "./example.json"

# To encrypt a Json file and return a string 
    Encrypt.jsonfile(filename)

**It will return a string if was a Json file and successfully encrypted or it will return None if wasn't a Json file or failed to encrypt. Exceptions will be handled by the Encrypt class.
Finally to catch these exceptions use this formula:**

    string_encrypted = Encrypt.jsonfile(filename)
    if string_encrypted:
        print("Encrypted successfully")
        print(string_encrypted)
    else:
        print("Not possible to encrypt non json files")
    

# To encrypt from a file and save file encrypted

    Encrypt.jsonfile(filename, save_file=True)

**It will return boolean True if successfully encrypted or boolean False if failed to save
Finally use this formula to catch non Json files or no permissionn to save on disk**

    if Encrypt.jsonfile(filename, save_file=True):
        print("File {} was successfully encrypted and has been saved!".format(filename))
    else:
        print("Failed to encrypt file")

# **Decrypt into memory to use as data and keep your files encrypted on disk**
**If file is not encrypted it will return a boolean False**

**To decrypt and get as dictionary**

    dictionary = Decrypt.jsonfile(filename)

**To decrypt and get as string**

    string_decrypted = Decrypt.jsonfile(filename, output="string")

**To decrypt, get as string and change indent (Default indent is 4)**

    string_indented = Decrypt.jsonfile(filename, output="string", indent=2)

# To decrypt from a file and save it
**It will return boolean True if was successfully decrypted or boolean False if failed to save.
Finally use this formula to catch non encrypted files or no permission to save on disk**

    if Decrypt.jsonfile(filename, save_file=True):
        print("File {} was successfully decrypted and has been saved!".format(filename))
    else:
        print("File is not encrypted or it was modified")

# It is possible also to encrypt and decrypt from a string or a dictionary
**IMPORTANT! Strings to be able to encrypt must be written on a dictionary format**

    my_json_string_encrypted = Encrypt.jsonfile(filename)
    print("ENCRYPTED FROM A FILE INTO A STRING")
    print(my_json_string_encrypted)

**To decrypt a string that was encrypted as a dictionary type**

    decrypted_jsonstring = Decrypt.jsonstring(my_json_string_encrypted)

    if decrypted_jsonstring:
        print("DECRYPTED FROM A STRING INTO ANOTHER STRING")
        print(decrypted_jsonstring)
    else:
        print("String is not encrypted or not in a json format")

# Encrypt a dictionary type
**On encrypt it returns a string and on decrypt it returns back a dictionary**

    mydict = {"Name": "GRC Algoritmos"}
    encrypted_dict = Encrypt.dictionary(mydict)

**LET'S SEE:**

    print("Encrypted Dictionary:")
    print(encrypted_dict)
    print(type(encrypted_dict))

# Decrypt as a dictionary

    print("Decrypted Dictionary:")
    decrypted_dict = Decrypt.dictionary(encrypted_dict)
    print(decrypted_dict)
    print(type(decrypted_dict))

# Decrypt as a string

    decrypted_string = Decrypt.jsonstring(encrypted_dict)
    print(decrypted_string)
    print(type(decrypted_string))

# It's possible also to encrypt a dictionary and save as a file
**It will return a boolean True if successfully saved or boolean False if failed
If file exists as default it will return False, but it's possible to allow "Overwrite" just set overwrite=True**

    mydict = {"Name": "GRC Algoritmos", "File": "Saved"}
    if Encrypt.dictionary(mydict, save_file=True, filename="grc.json", overwrite=True):
        print("Successfully saved!")
    else:
        print("Not possible to save")

# Options to use with Encrypt and Decrypt class

**save_file=True**       -> Saves the return on disk

**save_file=False**      -> Returns a Json object without saving on disk

**password="str/int"**       -> Add a password to the encryption (Using this option it will only decrypt with same password)

**sha256=Boolean**     -> Is set True by default - this option will encrypt passwords with sha-256

**indent="int"**         -> Set indent to Json file on decryption, by default is set to indent=4

**output="string"**      -> Return decryption as a string, as default is set to "json" which returns as dictionary type

**filename="file"**      -> Set the file name to be saved

**overwrite=Boolean**    -> True overwrite the file if already exists and as Default returns False if a file already exists with same name
