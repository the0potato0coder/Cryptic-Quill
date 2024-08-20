import pandas as pd
from ciphers.caesar import caesar_cipher
from ciphers.vigenere import vigenere_cipher
from ciphers.playfair import playfair_cipher
from ciphers.rail_fence import rail_fence_cipher
from ciphers.affine import affine_cipher


def create_encrypted_dataset(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    data = []
    caesar_shift = 3
    vigenere_key = "KEY"
    playfair_key = "MONARCHY"
    rail_fence_key = 3
    affine_a, affine_b = 5, 8

    for line in lines:
        line = line.strip()
        if not line:
            continue
        encrypted_caesar = caesar_cipher(line, caesar_shift)
        encrypted_vigenere = vigenere_cipher(line, vigenere_key)
        encrypted_playfair = playfair_cipher(line, playfair_key)
        encrypted_rail_fence = rail_fence_cipher(line, rail_fence_key)
        encrypted_affine = affine_cipher(line, affine_a, affine_b)

        data.append([encrypted_caesar, "Caesar"])
        data.append([encrypted_vigenere, "Vigenère"])
        data.append([encrypted_playfair, "Playfair"])
        data.append([encrypted_rail_fence, "Rail Fence"])
        data.append([encrypted_affine, "Affine"])

    df = pd.DataFrame(data, columns=["Encrypted_Text", "Cipher_Type"])
    df.to_csv('data/encrypted_dataset.csv', index=False)
    print("Dataset created successfully!")


if __name__ == "__main__":
    input_file = 'data/plaintext.txt'  # Path to your input .txt file
    create_encrypted_dataset(input_file)
