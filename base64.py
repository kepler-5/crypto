#!/usr/bin/python

HEX_STRING = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d1'
B64_STRING = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29tEA=='

HEX_CHARS = '0123456789abcdef'
B64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

# 444 = 0100 0100 0100
#  RE = 010001 000100

def binaryify(hex_):
    if not hex_:
        return []

    ret = []
    num = HEX_CHARS.index(hex_[0].lower())
    for _ in xrange(4):
        ret.insert(0, num % 2)
        num /= 2

    return ret + binaryify(hex_[1:])

def toBase64Char(bits):
    value = 0
    for i in xrange(6):
        value = value * 2 + bits[i]
    return B64_CHARS[value]

def toBase64(hex_):
    bbits = binaryify(hex_)

    sneakyEqualsSigns = ''
    while len(bbits) % 6 != 0:
        bbits += [0, 0, 0, 0]
        sneakyEqualsSigns += '='

    chunkedBits = [bbits[i:i+6] for i in xrange(0, len(bbits), 6)]
    return ''.join([toBase64Char(bits_) for bits_ in chunkedBits]) + sneakyEqualsSigns

def toHexChar(bits):
    value = 0
    for i in xrange(4):
        value = value * 2 + bits[i]
    return HEX_CHARS[value]

def toHex(bits):
    chunkedBits = [bits[i:i+4] for i in xrange(0, len(bits), 4)]
    return ''.join([toHexChar(bits_) for bits_ in chunkedBits])

def toAsciiChar(bits):
    value = 0
    for i in xrange(8):
        value = value * 2 + bits[i]
    return chr(value)

def toAscii(hex_):
    binbits = binaryify(hex_)
    chunkedBits = [binbits[i:i+8] for i in xrange(0, len(binbits), 8)]
    return ''.join([toAsciiChar(bits_) for bits_ in chunkedBits])

def main():
    print toBase64(HEX_STRING)

if __name__ == '__main__':
    main()
