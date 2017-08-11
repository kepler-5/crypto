#!/usr/bin/python

import base64
import operator

LETTER_FREQUENCY = 'zqxjkvbpygfwmucldrhsnioate'

def get_letter_frequency(character):
    if character in LETTER_FREQUENCY:
        return LETTER_FREQUENCY.index(character)
    return 0

def xor_cipher_single(ascii_string, character):
    return [chr(ord(c) ^ character) for c in ascii_string]

def score(text):
    return reduce(operator.add, [get_letter_frequency(c) for c in text], 0)

def main():
    cipher_text = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ascii_cipher = base64.toAscii(cipher_text)

    dictionary = {}
    for i in xrange(128):
        text = xor_cipher_single(ascii_cipher, i)
        dictionary[chr(i)] = (score(text), text)
    
    best = sorted(dictionary.items(), key=lambda item: item[1][0], reverse=True)
    print ''.join(best[0][1][1])

if __name__ == '__main__':
    main()