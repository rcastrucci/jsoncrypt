import crypter
import ast
import json


class Encrypt:

    def jsonfile(filename, password="", sha256=True, save_file=True, output="json"):
        try:
            if sha256:
                password = crypter.encrypt256(password)
            json_crypt_document = crypter.encrypt(crypter.open_file(filename), password)
            if save_file:
                # SAVE INTO FILE AND RETURN A BOOLEAN TRUE
                with open(filename, "w", encoding="utf-8") as json_file_encrypted :
                    json_file_encrypted.write(json_crypt_document)
                return True
            else:
                if output == "json":
                    # RETURN AS A DICTIONARY
                    return json.loads(json_crypt_document)
                else:
                    # RETURN AS A STRING
                    return json_crypt_document
        except:
            return False

class Decrypt:

    def decryptjson(encrypted_document, password="", sha256=True, ignore_verification=False, indent=4):
        try:
            original_document_hash = crypter.encrypt256(encrypted_document[0])
            if sha256:
                password = crypter.encrypt256(password)
            # CHECK IF FILE IS ENCRYPTED OR IF WAS MODIFIED
            if encrypted_document[6] == original_document_hash or ignore_verification:
                crypt_key1 = crypter.get_sequence5(0, 5, password, encrypted_document[1])
                crypt_key2 = crypter.get_sequence5(5, 10, password, encrypted_document[2])
                crypt_key3 = crypter.get_sequence5(10, 15, password, encrypted_document[3])
                crypt_key4 = crypter.get_sequence5(15, 20, password, encrypted_document[4])
                crypt_key5 = crypter.get_sequence6(20, 26, password, encrypted_document[5])
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
                    decrypt = crypter.decrypt(encrypted_document[0], crypt_content)
                    return json.dumps(ast.literal_eval(decrypt), indent=indent, ensure_ascii=False)
                else:
                    return None
            else:
                return False
        except:
            return False

    def jsonstring(string_to_decrypt, password="", sha256=True, ignore_verification=False, indent=4):
        encrypted_document = crypter.get_string(string_to_decrypt)
        return Decrypt.decryptjson(encrypted_document, password, sha256, ignore_verification, indent)

    def jsonfile(file_to_decrypt, password="", sha256=True, ignore_verification=False, indent=4, save_file=False, output="json"):
        encrypted_document = crypter.get_content(file_to_decrypt)
        decrypted_string = Decrypt.decryptjson(encrypted_document, password, sha256, ignore_verification, indent)
        if decrypted_string:
            print("File decrypted successfully")
            # IF OPTION SAVE_FILE BOOLEAN TRUE SAVE INTO FILE
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
            print("File is not encrypted or was modified")
        else:
            print("Wrong password")
