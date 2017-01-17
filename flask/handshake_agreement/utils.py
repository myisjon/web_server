from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA


def key_pair_init(rsa_length=1024):
    random_generator = Random.new().read
    rsa = RSA.generate(rsa_length, random_generator)
    private_pem = rsa.exportKey()
    with open('private_key.pem', 'wb') as f:
        print('create private key ......')
        f.write(private_pem)

    publick_pem = rsa.publickey().exportKey()
    with open('public_key.pem', 'wb') as f:
        print('create public key ......')
        f.write(publick_pem)

def encrypt(msg):
    pass

def decrypt(msg):
    pass
