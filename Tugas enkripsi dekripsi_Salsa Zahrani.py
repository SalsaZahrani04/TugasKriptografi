# Fungsi untuk enkripsi
def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        # Jika karakter adalah huruf besar
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Jika karakter adalah huruf kecil
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # Jika karakter bukan huruf (spasi, tanda baca, angka)
        else:
            encrypted_text += char
    
    return encrypted_text  

# Fungsi untuk dekripsi
def decrypt(text, shift):
    decrypted_text = ""
    
    for char in text:
        # Jika karakter adalah huruf besar
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Jika karakter adalah huruf kecil
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        # Jika karakter bukan huruf (spasi, tanda baca, angka)
        else:
            decrypted_text += char
    
    return decrypted_text

# Contoh penggunaan program
if __name__ == "__main__":
    plain_text = input("Masukkan teks yang akan dienkripsi: ")
    shift_value = int(input("Masukkan nilai shift (pergeseran): "))
    
    # Enkripsi
    encrypted_text = encrypt(plain_text, shift_value)
    print(f"Teks terenkripsi: {encrypted_text}")
    
    # Dekripsi
    decrypted_text = decrypt(encrypted_text, shift_value)
    print(f"Teks terdekripsi: {decrypted_text}")
