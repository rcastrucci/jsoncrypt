import ast
import json
from os.path import exists
from .crypter import (encrypt256, encrypt, encode64,
                      decrypt, decode64,
                      get_content, get_sequence5, get_sequence6, get_string,
                      open_file)

# TO USE JSONCRYPT IMPORT Encrypt AND Decrypt from jsoncrypt
# FORMULAS TO USE ENCRYPT AND DECRYPT
# Encrypt.jsonfile(json_filename_to_encrypt)
# Encrypt.jsonstring(json_string_to_encrypt)
# Encrypt.dictionary(a_dictionary_to_encrypt)
# Decrypt.jsonfile(filename_encrypted)
# Decrypt.jsonstring(json_string_encrypted)
# Decrypt.dictionary(string_of_a_dictionary_encrypted)

class Encrypt:

    def encryptjson(decrypted_string, password="", sha256=True):
        if sha256:
            password = encrypt256(password)
        # RETURN AS A STRING
        return encrypt(decrypted_string, password)

    def jsonfile(filename, password="", sha256=True, save_file=False):
        try:
            json_crypt_document = Encrypt.encryptjson(open_file(filename), password=password, sha256=sha256)
        except:
            return None
        if save_file:
            # SAVE INTO FILE AND RETURN A BOOLEAN TRUE
            try:
                with open(filename, "w", encoding="utf-8") as json_file_encrypted :
                    json_file_encrypted.write(json_crypt_document)
                return True
            except:
                return False
        else:
            # RETURN AS A STRING
            return json_crypt_document

    def jsonstring(string_to_encrypt, password="", sha256=True, save_file=False, filename=None, overwrite=False):
        if save_file and filename is not None:
            if not exists(filename) or exists(filename) and overwrite:
                try:
                    with open(filename, "w", encoding="utf-8") as string_encrypted:
                        string_encrypted.write(Encrypt.encryptjson(string_to_encrypt, password=password, sha256=sha256))
                    return True
                except:
                    return False
            else:
                return False
        else:
            return Encrypt.encryptjson(string_to_encrypt, password=password, sha256=sha256)

    def dictionary(dictionary_to_encrypt, password="", sha256=True, save_file=False, filename=None, overwrite=False):
        if save_file and filename is not None:
            if not exists(filename) or exists(filename) and overwrite:
                try:
                    with open(filename, "w", encoding="utf-8") as dictionary_encrypted:
                        dictionary_encrypted.write(Encrypt.encryptjson(str(dictionary_to_encrypt), password=password, sha256=sha256))
                    return True
                except:
                    return False
            else:
                return False
        else:
            return Encrypt.encryptjson(str(dictionary_to_encrypt), password=password, sha256=sha256)


class Decrypt:

    def decryptjson(encrypted_document, password="", sha256=True, ignore_verification=False, indent=4):
        try:
            original_document_hash = encrypt256(encrypted_document[0])
            if sha256:
                password = encrypt256(password)
            # CHECK IF FILE IS ENCRYPTED OR IF WAS MODIFIED
            if encrypted_document[6] == original_document_hash or ignore_verification:
                crypt_key1 = get_sequence5(0, 5, password, encrypted_document[1])
                crypt_key2 = get_sequence5(5, 10, password, encrypted_document[2])
                crypt_key3 = get_sequence5(10, 15, password, encrypted_document[3])
                crypt_key4 = get_sequence5(15, 20, password, encrypted_document[4])
                crypt_key5 = get_sequence6(20, 26, password, encrypted_document[5])
                if crypt_key1 is not None and crypt_key2 is not None and \
                crypt_key3 is not None and crypt_key4 is not None and \
                crypt_key5 is not None:
                    crypt_content = []
                    for key_sequence in crypt_key1:
                        crypt_content.append(key_sequence)
                    for key_sequence in crypt_key2:
                        crypt_content.append(key_sequence)
                    for key_sequence in crypt_key3:
                        crypt_content.append(key_sequence)
                    for key_sequence in crypt_key4:
                        crypt_content.append(key_sequence)
                    for key_sequence in crypt_key5:
                        crypt_content.append(key_sequence)
                    decrypted_string = decrypt(encrypted_document[0], crypt_content)
                    return json.dumps(ast.literal_eval(decrypted_string), indent=indent, ensure_ascii=False)
                else:
                    return None
            else:
                return False
        except:
            return False

    def jsonstring(string_to_decrypt, password="", sha256=True, ignore_verification=False, indent=4):
        encrypted_document = get_string(string_to_decrypt)
        return Decrypt.decryptjson(encrypted_document, password=password, sha256=sha256,
                                   ignore_verification=ignore_verification, indent=indent)

    def dictionary(dictionary_to_decrypt, password="", sha256=True, ignore_verification=False, indent=4):
        encrypted_document = get_string(dictionary_to_decrypt)
        return json.loads(Decrypt.decryptjson(encrypted_document, password=password, sha256=sha256,
                                   ignore_verification=ignore_verification, indent=indent))

    def jsonfile(file_to_decrypt, password="", sha256=True, ignore_verification=False, indent=4, save_file=False, output="json"):
        encrypted_document = get_content(file_to_decrypt)
        decrypted_string = Decrypt.decryptjson(encrypted_document, password=password, sha256=sha256,
                                               ignore_verification=ignore_verification, indent=indent)
        if decrypted_string:
            if save_file:
                with open(file_to_decrypt, "w", encoding="utf-8") as output_file:
                    output_file.write(decrypted_string)
                return True
            else:
                if output == "json":
                    return json.loads(decrypted_string)
                else:
                    return decrypted_string
        elif decrypted_string is None:
            # File is not encrypted or was modified
            return None
        else:
            # Wrong password
            return False
