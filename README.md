# jsoncrypt
Encryption and Decryption of JSON files. Option of reading JSON files encrypted and adding a password.

# JsonCrypt Options
save_file = "Boolean"  -> if True, saves the result into the same file
save_file = "Boolean"  -> Default is set to False, returns a Json object with the result without saving on the file
password = "str"       -> Add a password to the encryption (Using this option it will only decrypt with same password)
sha256 = "Boolean"     -> Is set True by default - this option will encrypt password with sha-256 signature
indent = "int"         -> Set indent to Json file on decryption, by default is set to indent=4
