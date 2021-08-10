def ceasar_cipher_encryptor(string, key):
    # 1. generate an alphabet and empty array for encrypted string
    alphabet = list(map(chr, range(97, 123))) # len = 26
    encrypted_string = []
    # 2. Loop over each character in string
    for letter in string:
        # 3. determine current position of the curent letter in the alphabet
        current_position = alphabet.index(letter)
        # 4. determine position of the current letter after shifting it by the key
        target_position = wrap_pointer(current_position, key)
        # 5. determine what will the current letter become after shifting and append it encrypted string
        encrypted_string.append(alphabet[target_position])

    return ''.join(encrypted_string)

def wrap_pointer(current_position, key):
    if key + current_position < 26:
        return key + current_position
    else:
        return (key + current_position) % 26


def ceasar_cipher_encryptor_alt(string, key):
    new_letters = []
    new_key = key % 26
    alphabet = list(map(chr, range(97, 123)))

    for letter in string:
        new_letters.append(get_new_letter(letter, new_key, alphabet))

    return "".join(new_letters)

def get_new_letter(letter, new_key, alphabet):
    new_letter_code = alphabet.index(letter) + new_key
    return alphabet[new_letter_code % 26]