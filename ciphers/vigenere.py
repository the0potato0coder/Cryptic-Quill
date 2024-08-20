def vigenere_cipher(text, key):
    key = key.lower()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    ciphertext = ''
    for i in range(len(text_int)):
        if text[i].isalpha():
            value = (text_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65 if text[i].isupper() else value + 97)
        else:
            ciphertext += text[i]
    return ciphertext
