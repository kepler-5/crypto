#!/usr/bin/python

import base64

def fixed_xor(buffer1, buffer2):
    bits1 = base64.binaryify(buffer1)
    bits2 = base64.binaryify(buffer2)
    return base64.toHex([bits1[i] ^ bits2[i] for i in xrange(len(bits1))])

def main():
    print fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965') == '746865206b696420646f6e277420706c6179'

if __name__ == '__main__':
    main()