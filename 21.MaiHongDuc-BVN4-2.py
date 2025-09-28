def char_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    return chr((n % 26) + ord('A'))

def encrypt_substitution(plaintext, k):
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            p = char_to_num(c)
            c_num = (p + k) % 26
            ciphertext += num_to_char(c_num)
        else:
            ciphertext += c  # giữ nguyên dấu cách hoặc ký tự khác
    return ciphertext

def decrypt_substitution(ciphertext, k):
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            c_num = char_to_num(c)
            p = (c_num - k) % 26
            plaintext += num_to_char(p)
        else:
            plaintext += c
    return plaintext

if __name__ == "__main__":
    k = 21  # STT = 21
    plaintext = "MaiHongDuc"
    
    ciphertext = encrypt_substitution(plaintext, k)
    print("Plaintext:", plaintext)
    print("Key (k):", k)
    print("Ciphertext:", ciphertext)

    decrypted = decrypt_substitution(ciphertext, k)
    print("Decrypted:", decrypted)
