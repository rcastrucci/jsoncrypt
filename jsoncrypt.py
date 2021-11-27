import base64
import hashlib
import random
import ast
import json
import string


def code(file_to_encrypt, password="", sha256=True, save_file=False):
    try:
        if sha256:
            password = JsonCrypt.encrypt256(password)
        json_crypt_document = JsonCrypt.encrypt(JsonCrypt.open_file(file_to_encrypt), password)
        if save_file:
            with open(file_to_encrypt, "w", encoding="utf-8") as json_file_encrypted :
                json_file_encrypted.write(json_crypt_document)
            return True
        else:
            return json_crypt_document
    except:
        return False


def decode(file_to_decrypt, password="", sha256=True, ignore_verification=False, indent=4, save_file=False):
    try:
        encrypted_document = JsonCrypt.get_content(file_to_decrypt)
        original_document_hash = JsonCrypt.encrypt256(encrypted_document[0])
        if sha256:
            password = JsonCrypt.encrypt256(password)
        # CHECK IF FILE IS ENCRYPTED OR IF WAS MODIFIED
        if encrypted_document[6] == original_document_hash or ignore_verification:
            crypt_key1 = JsonCrypt.get_sequence5(0, 5, password, encrypted_document[1])
            crypt_key2 = JsonCrypt.get_sequence5(5, 10, password, encrypted_document[2])
            crypt_key3 = JsonCrypt.get_sequence5(10, 15, password, encrypted_document[3])
            crypt_key4 = JsonCrypt.get_sequence5(15, 20, password, encrypted_document[4])
            crypt_key5 = JsonCrypt.get_sequence6(20, 26, password, encrypted_document[5])
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
                decrypt = JsonCrypt.decrypt(encrypted_document[0], crypt_content)
                json_output = json.dumps(ast.literal_eval(decrypt), indent=indent, ensure_ascii=False)
                if save_file:
                    with open(file_to_decrypt, "w", encoding="utf-8") as output_file:
                        output_file.write(json_output)
                    return True
                else:
                    return json_output
            else:
                return None
    except:
        return False


class JsonCrypt:

    def encrypt256(self):
        sha_signature = hashlib.sha256(self.encode()).hexdigest()
        return sha_signature

    def encode64(self):
        message_bytes = self.encode('utf-8')
        base64_bytes = base64.b64encode(message_bytes)
        base64_string = base64_bytes.decode('utf-8')
        return base64_string

    def decode64(self):
        base64_message = self
        base64_bytes = base64_message.encode('utf-8')
        message_bytes = base64.b64decode(base64_bytes)
        decoded_string = message_bytes.decode('utf-8')
        return decoded_string

    def encrypt(self, hash_pass):
        alfa = list(string.ascii_lowercase)
        # CREATE SUB_LISTS
        ps1 = []
        ps2 = []
        ps3 = []
        ps4 = []
        ps5 = []
        # GENERATE A SEQUENCE
        for i1 in range(0, 5):
            ps1.append(i1)
        for i2 in range(5, 10):
            ps2.append(i2)
        for i3 in range(10, 15):
            ps3.append(i3)
        for i4 in range(15, 20):
            ps4.append(i4)
        for i5 in range(20, 26):
            ps5.append(i5)
        # RANDOMIZE SEQUENCES
        random.shuffle(ps1)
        random.shuffle(ps2)
        random.shuffle(ps3)
        random.shuffle(ps4)
        random.shuffle(ps5)
        # ADD SUB_LISTS TO A FINAL LIST
        pswitched = []
        for sq in ps1:
            pswitched.append(sq)
        for sq in ps2:
            pswitched.append(sq)
        for sq in ps3:
            pswitched.append(sq)
        for sq in ps4:
            pswitched.append(sq)
        for sq in ps5:
            pswitched.append(sq)
        # ENCODE BASE64
        encoded_string = JsonCrypt.encode64(self)
        # START ENCRYPTION
        encrypted_string = ""
        for letter in encoded_string:
            counter = 0
            found = False
            for i in alfa:
                if letter == i:
                    found = True
                    encrypted_string += "{}".format(alfa[pswitched[counter]])
                    break
                elif letter == i.upper():
                    found = True
                    encrypted_string += "{}".format(alfa[pswitched[counter]].upper())
                    break
                counter += 1
            if not found:
                encrypted_string += "{}".format(letter)

        # ADD A HASH OF ENCRYPTED DOCUMENT TO SIGN
        hash_k = JsonCrypt.encrypt256(encrypted_string)

        # ADD KEY TO DECRYPT
        k1 = JsonCrypt.encrypt256(hash_pass + str(ps1))
        k2 = JsonCrypt.encrypt256(hash_pass + str(ps2))
        k3 = JsonCrypt.encrypt256(hash_pass + str(ps3))
        k4 = JsonCrypt.encrypt256(hash_pass + str(ps4))
        k5 = JsonCrypt.encrypt256(hash_pass + str(ps5))

        # POSITION KEYS HALF WAY OF THE ENCRYPTED STRING
        position = int(len(encrypted_string) / 2)

        output = "".join((encrypted_string[:position], hash_k, k1, k2, k3, k4, k5, encrypted_string[position:]))

        # RESULT ENCRYPTED
        return output

    def decrypt(self, pswitched):
        alfa = list(string.ascii_lowercase)
        decoded_string = ""
        for letter in self:
            counter = 0
            found = False
            for i in alfa:
                if letter == i:
                    found = True
                    position = 0
                    for n in pswitched:
                        if n == counter:
                            decoded_string += "{}".format(alfa[position])
                            break
                        position += 1
                    break
                elif letter == i.upper():
                    found = True
                    position = 0
                    for n in pswitched:
                        if n == counter:
                            decoded_string += "{}".format(alfa[position].upper())
                            break
                        position += 1
                    break
                counter += 1
            if not found:
                decoded_string += "{}".format(letter)
        # RESULT ENCRYPTED
        return str(JsonCrypt.decode64(decoded_string))

    def get_sequence5(self, end, pwrd_hash, hash256):
        plis = []
        for n in range(self, end):
            plis.append(n)
        for loop in range(0, len(plis)):
            if 0 < loop < len(plis):
                plis.insert(0, plis.pop(loop))
            for i in range(0, len(plis)-1):
                lis = [plis[0], plis[1], plis[2], plis[3], plis[4]]
                if 0 < i < len(plis)-1:
                    lis.insert(1, lis.pop(i+1))
                ml = [lis[0], lis[1], lis[2], lis[3], lis[4]]
                if JsonCrypt.encrypt256(pwrd_hash+str(ml)) == hash256:
                    return ml
                ml = [lis[0], lis[1], lis[2], lis[4], lis[3]]
                if JsonCrypt.encrypt256(pwrd_hash+str(ml)) == hash256:
                    return ml
                ml = [lis[0], lis[1], lis[3], lis[2], lis[4]]
                if JsonCrypt.encrypt256(pwrd_hash+str(ml)) == hash256:
                    return ml
                ml = [lis[0], lis[1], lis[3], lis[4], lis[2]]
                if JsonCrypt.encrypt256(pwrd_hash+str(ml)) == hash256:
                    return ml
                ml = [lis[0], lis[1], lis[4], lis[3], lis[2]]
                if JsonCrypt.encrypt256(pwrd_hash+str(ml)) == hash256:
                    return ml
                ml = [lis[0], lis[1], lis[4], lis[2], lis[3]]
                if JsonCrypt.encrypt256(pwrd_hash+str(ml)) == hash256:
                    return ml
        return None

    def get_sequence6(self, end, pwrd_hash, hash256):
        plis = []
        for n in range(self, end):
            plis.append(n)
        for loop in range(0, len(plis)):
            if 0 < loop < len(plis):
                plis.insert(0, plis.pop(loop))
            for n in range(0, len(plis)-1):
                lis = [plis[0], plis[1], plis[2], plis[3], plis[4], plis[5]]
                if 0 < n < len(plis)-1:
                    lis.insert(1, lis.pop(n+1))
                for i in range(0, len(lis)-1):
                    li = [lis[0], lis[1], lis[2], lis[3], lis[4], lis[5]]
                    if 0 < i < len(lis)-1:
                        li.insert(2, li.pop(i+1))
                    # COMPARE
                    ml = [li[0], li[1], li[2], li[3], li[4], li[5]]
                    if JsonCrypt.encrypt256(pwrd_hash+str(ml)) == hash256:
                        return ml
                    ml = [li[0], li[1], li[2], li[3], li[5], li[4]]
                    if JsonCrypt.encrypt256(pwrd_hash+str(ml)) == hash256:
                        return ml
                    ml = [li[0], li[1], li[2], li[4], li[3], li[5]]
                    if JsonCrypt.encrypt256(pwrd_hash+str(ml)) == hash256:
                        return ml
                    ml = [li[0], li[1], li[2], li[4], li[5], li[3]]
                    if JsonCrypt.encrypt256(pwrd_hash+str(ml)) == hash256:
                        return ml
                    ml = [li[0], li[1], li[2], li[5], li[4], li[3]]
                    if JsonCrypt.encrypt256(pwrd_hash+str(ml)) == hash256:
                        return ml
                    ml = [li[0], li[1], li[2], li[5], li[3], li[4]]
                    if JsonCrypt.encrypt256(pwrd_hash+str(ml)) == hash256:
                        return ml
        return None

    def open_file(self):
        with open(self, "r", encoding="utf-8") as file:
            json_content = json.loads(file.read())
        return str(json_content)

    def get_content(self):
        with open(self, "r", encoding="utf-8") as file:
            all_content = file.read()
            position = int((len(all_content)-384) / 2)
            hash_document = all_content[position:position+64]
            k1 = all_content[position+(1*64):position + 128]
            k2 = all_content[position+(2*64):position + 192]
            k3 = all_content[position+(3*64):position + 256]
            k4 = all_content[position+(4*64):position + 320]
            k5 = all_content[position+(5*64):position + 384]
            document = all_content[:position] + all_content[position+384:]
        return [document, k1, k2, k3, k4, k5, hash_document]