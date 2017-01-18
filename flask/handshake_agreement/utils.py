from Crypto import Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


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


# https://www.dlitz.net/software/pycrypto/api/2.6/
def rsa_encrypt(msg, pub_key_path):
    msg = bytes(msg, 'utf-8')
    h = SHA.new(msg)
    with open(pub_key_path, 'rb') as f:
        key = RSA.importKey(f.read())
    cipher = PKCS1_v1_5.new(key)
    return cipher.encrypt(msg + h.digest())


def rsa_decrypt(msg, pri_key_path):
    with open(pri_key_path, 'rb') as f:
        key = RSA.importKey(f.read())
    dsize = SHA.digest_size
    sentinel = Random.new().read(15 + dsize)
    cipher = PKCS1_v1_5.new(key)
    msg = cipher.decrypt(msg, sentinel)
    digest = SHA.new(msg[:-dsize]).digest()
    if digest == msg[-dsize:]:
        return msg[:-dsize]
    return msg


def main():
    key_pair_init(rsa_length=1024)
    msg = rsa_decrypt(rsa_encrypt('test+1+测试', 'public_key.pem'), 'private_key.pem')
    print(msg)
    print(msg.decode('utf-8'))


if __name__ == '__main__':
    main()
