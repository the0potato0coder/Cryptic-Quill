def affine_cipher(text, a, b):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(((a * (ord(char) - 65) + b) % 26) + 65)
        elif char.islower():
            result += chr(((a * (ord(char) - 97) + b) % 26) + 97)
        else:
            result += char
    return result
