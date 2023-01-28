# We use add cipher.
# and insert 'a' every 6 letters

# add cipher
# plain_text : the text you want to cipher
# key : add key into plain_text (need 0~26 integer)
# plain_text 'a', key 3 : return 'd'
def add_cipher(plain_text, key):
    cipher_text = ''
    for i in plain_text:
        cipher_text += chr(ord(i) + key)

    return cipher_text


# Inserting
# plain_text : the text you want to insert
# insert 'a' into every 6 letters
def inserting_cipher(plain_text):
    index = 0
    cipher_str_list = []

    for i in plain_text:
        cipher_str_list.append(i)
        index += 1

        if index % 6 == 0:
            cipher_str_list.append('a')

    cipher_text = ''
    for i in cipher_str_list:
        cipher_text += i
    return cipher_text


# Extracting
# cipher_text : completely ciphered text
# extract additional 'a' in cipher_text (because of inserting_cipher)
def extract_padding(cipher_text):
    new_text = ''
    index = 0
    for i in cipher_text:
        if (index + 1) % 7 == 0:
            pass
        else:
            new_text += i

        index += 1
    return new_text


def main():
    print('201413271 김석우')
    sentence = input('암호화 할 문장을 입력하세요. : ')

    added_text = add_cipher(sentence, 3)
    cipher = inserting_cipher(added_text)

    print('암호화된 문장 : {}'.format(cipher))
    print('=============')

    cipher_sentence = input('복호화 할 문장을 입력하세요. : ')
    extracted = extract_padding(cipher_sentence)
    plain = add_cipher(extracted, -3)
    print('복호화된 문장 : {}'.format(plain))


if __name__ == '__main__':
    main()
