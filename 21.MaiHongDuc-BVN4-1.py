def caesar_encrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():  # chỉ mã hóa chữ cái
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char  # giữ nguyên ký tự không phải chữ
    return result


if __name__ == "__main__":
    k = 21
    plaintext = "Mai Hong Duc"
    ciphertext = caesar_encrypt(plaintext, k)
    print("Plaintext:", plaintext)
    print("Key (k):", k)
    print("Ciphertext:", ciphertext)
