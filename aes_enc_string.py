from ast import parse
from codecs import encode
from urllib import parse
from Cryptodome.Cipher import AES
from Cryptodome import Random
from Cryptodome.Protocol.KDF import PBKDF2

import base64

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def get_private_key(secret_key):
    salt = "ably_2022_@!V"
    kdf = PBKDF2(secret_key, salt, 64, 1000)
    key = kdf[:32]
    return key

def encrypt(raw, secret_key):
    private_key = get_private_key(secret_key)
    raw = pad(raw).encode('utf-8')
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')

def decrypt(enc, secret_key):
    private_key = get_private_key(secret_key)
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:])).decode('utf-8')

enc_str = encrypt('hello', '1234')
print(parse.parse_qs(enc_str))
print(enc_str)
dec_str = decrypt(enc_str, '1234')
print(dec_str)


dec_str = decrypt('tObsD7j8EZ5CLq6UwbFGN2516/lIYJVvgHmv4FTzi3s=', '1234')
print(dec_str)