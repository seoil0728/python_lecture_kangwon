# cipher methods

# To make plain list (pair of (alphabet, number))
def make_plain_alphabet(a):
    di = dict()
    count = 0
    for i in a:
        di[i] = count
        count += 1
    return di


# To make cipher list (pair of (number, alphabet))
def make_cipher_alphabet(a):
    di = dict()
    count = 0
    for i in a:
        di[count] = i
        count += 1
    return di


# calculate inverse of multiple
def inverse_modulo(key, modulo):
    inverse = 0
    is_inverse = False

    for i in range(modulo):
        inverse = (key * i) % modulo
        if inverse == 1:
            inverse = i
            is_inverse = True
            break

    if is_inverse:
        return inverse
    else:
        return 0


# add cipher
# text = sentence you want to cipher (needs Upper case, no blank)
# plain = list of sets (alphabet, number)
# cipher = list of sets (number, alphabet)
# key = key of add cipher
def add_cipher(text, plain, cipher, key):
    cipher_text = ''
    for i in text:
        num = plain.get(i)
        num += key
        if num > 25:
            num = num % 26
        word = cipher.get(num)
        cipher_text += word

    return cipher_text


# multiple cipher
# text = sentence you want to cipher (needs Upper case, no blank)
# plain = list of sets (alphabet, number)
# cipher = list of sets (number, alphabet)
# key = key of multiple cipher
def multiple_cipher(text, plain, cipher, key):
    cipher_text = ''
    if key not in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        cipher_text = 'unavailable key'
    else:
        for i in text:
            num = plain.get(i)
            num *= key
            if num > 25:
                num = num % 26
            word = cipher.get(num)
            cipher_text += word

    return cipher_text


# affine cipher
# text = sentence you want to cipher (needs Upper case, no blank)
# plain = list of sets (alphabet, number)
# cipher = list of sets (number, alphabet)
# key = key of affine cipher (needs set like (7, 20))
def affine_cipher(text, plain, cipher, key):
    cipher_text = ''
    if key[0] not in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        cipher_text = 'unavailable key'
    else:
        for i in text:
            num = plain.get(i)
            num *= key[0]
            num += key[1]
            if num > 25:
                num = num % 26
            word = cipher.get(num)
            cipher_text += word

    return cipher_text


# add decrypter
# text = sentence you want to decrypt (needs Upper case, no blank)
# plain = list of sets (alphabet, number)
# cipher = list of sets (number, alphabet)
# key = key of add decrypt
def add_decrypter(text, plain, cipher, key):
    cipher_text = ''
    for i in text:
        num = plain.get(i)
        num -= key
        if num < 0:
            num = num + 26
        word = cipher.get(num)
        cipher_text += word

    return cipher_text


# multiple decrypter
# text = sentence you want to decrypt (needs Upper case, no blank)
# plain = list of sets (alphabet, number)
# cipher = list of sets (number, alphabet)
# key = key of multiple decrypt
def multiple_decrypter(text, plain, cipher, key):
    cipher_text = ''
    if key not in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        cipher_text = 'unavailable key'
    else:
        a = inverse_modulo(key, 26)
        if a == 0:
            cipher_text = 'unavailable key'
        else:
            for i in text:
                num = plain.get(i)
                num *= a
                if num > 25:
                    num = num % 26
                word = cipher.get(num)
                cipher_text += word

    return cipher_text


# affine decrypter
# text = sentence you want to decrypt (needs Upper case, no blank)
# plain = list of sets (alphabet, number)
# cipher = list of sets (number, alphabet)
# key = key = key of affine decrypt (needs set like (7, 20))
def affine_decrypter(text, plain, cipher, key):
    cipher_text = ''
    if key[0] not in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        cipher_text = 'unavailable key'
    else:
        a = inverse_modulo(key[0], 26)
        if a == 0:
            cipher_text = 'unavailable key'
        for i in text:
            num = plain.get(i)
            num -= key[1]
            num *= a
            while num < 0:
                num += 26
            if num > 25:
                num = num % 26
            word = cipher.get(num)
            cipher_text += word

    return cipher_text


# Vigenere cipher
# text = sentence you want to cipher (needs Upper case, no blank)
# plain = list of sets (alphabet, number)
# cipher = list of sets (number, alphabet)
# keyword = keyword of Vigenere cipher (needs Upper case, no blank)
def vigenere_cipher(text, plain, cipher, keyword):
    cipher_text = ''
    key = []
    for i in keyword:
        key.append(plain.get(i))

    count = 0
    for i in text:
        num = plain.get(i)
        num += key[count]
        if num > 25:
            num = num % 26
        word = cipher.get(num)
        cipher_text += word
        count += 1
        if count == len(keyword):
            count = 0

    return cipher_text


def main():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    plain = make_plain_alphabet(alphabet)
    cipher = make_cipher_alphabet(alphabet)

    print('Exercise no.21')
    sentence = 'THISISANEXERCISE'
    print('Plain text =', sentence)
    print(add_cipher(sentence, plain, cipher, 20))
    print(multiple_cipher(sentence, plain, cipher, 15))
    print(affine_cipher(sentence, plain, cipher, (15, 20)))
    #
    print()
    ciphered_text = 'NBCMCMUHYRYLWCMY'
    print(add_decrypter(ciphered_text, plain, cipher, 20))
    ciphered_text = 'ZBQKQKANIHIVEQKI'
    print(multiple_decrypter(ciphered_text, plain, cipher, 15))
    ciphered_text = 'TVKEKEUHCBCPYKEC'
    print(affine_decrypter(ciphered_text, plain, cipher, (15, 20)))

    print()
    print('Exercise no.23')
    sentence = 'LIFEISFULLOFSURPRISES'
    print(vigenere_cipher(sentence, plain, cipher, 'HEALTH'))

    sentence = 'We live in an insecure world'
    print(sentence.upper().replace(' ', ''))

    print()
    print('Exercise no.28')
    ciphered_text = 'NCJAEZRCLASJLYODEPRLYZRCLASJLCPEHZDTOPDZQLNZTY'
    print(add_decrypter(ciphered_text, plain, cipher, 13))
    print(add_decrypter(ciphered_text, plain, cipher, 12))
    print(add_decrypter(ciphered_text, plain, cipher, 11))
    print(add_decrypter(ciphered_text, plain, cipher, 14))
    print(add_decrypter(ciphered_text, plain, cipher, 15))


if __name__ == '__main__':
    main()
