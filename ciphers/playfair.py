def playfair_cipher(text, key):
    def generate_key_matrix(key):
        key_matrix = []
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key = "".join(dict.fromkeys(key.upper().replace("J", "I")))  # remove duplicates and replace J with I
        key += ''.join(filter(lambda x: x not in key, alphabet))
        key_matrix = np.array(list(key)).reshape(5, 5)
        return key_matrix

    def chunk_text(text):
        text = text.upper().replace("J", "I")
        text = ''.join([i if i.isalpha() else "" for i in text])
        text_pairs = []
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i + 1] if i + 1 < len(text) else "X"
            if a == b:
                text_pairs.append(a + "X")
                i += 1
            else:
                text_pairs.append(a + b)
                i += 2
        if len(text_pairs[-1]) == 1:
            text_pairs[-1] += "X"
        return text_pairs

    def find_position(char, key_matrix):
        pos = np.where(key_matrix == char)
        return pos[0][0], pos[1][0]

    key_matrix = generate_key_matrix(key)
    text_pairs = chunk_text(text)
    ciphertext = ""

    for pair in text_pairs:
        r1, c1 = find_position(pair[0], key_matrix)
        r2, c2 = find_position(pair[1], key_matrix)
        if r1 == r2:
            ciphertext += key_matrix[r1, (c1 + 1) % 5] + key_matrix[r2, (c2 + 1) % 5]
        elif c1 == c2:
            ciphertext += key_matrix[(r1 + 1) % 5, c1] + key_matrix[(r2 + 1) % 5, c2]
        else:
            ciphertext += key_matrix[r1, c2] + key_matrix[r2, c1]
    return ciphertext