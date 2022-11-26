
"""

"""
import rsa


def generate_keys() -> None:
    pub_key, priv_key = rsa.newkeys(1024)
    
    with open('keys/pubkey.pem', 'wb') as f:
        f.write(pub_key.save_pkcs1('PEM'))
    
    with open('keys/privkey.pem', 'wb') as f:
        f.write(priv_key.save_pkcs1('PEM'))


def load_keys() -> tuple[str, str]:

    with open('keys/pubkey.pem', 'rb') as f:
        pub_key = rsa.PublicKey.load_pkcs1(f.read())

    with open('keys/privkey.pem', 'rb') as f:
        priv_key = rsa.PrivateKey.load_pkcs1(f.read())

    return pub_key, priv_key


def encrypt(msg: str, key):
    return rsa.encrypt(msg.encode('ascii'), key)


def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False


def sign_sha256(msg: str, key):
    return rsa.sign(msg.encode('ascii'), key, 'SHA-256')


def verify_sha256(msg: str, signature, key):
    try:
        return rsa.verify(msg.encode('ascii'), signature, key) == 'SHA-256'
    except:
        False


generate_keys()
pub_key, priv_key = load_keys()

message = input('Enter a message: ')
ciphertext = encrypt(message, pub_key)

signature = sign_sha256(message, priv_key)

plain_text = decrypt(ciphertext, priv_key)

print(f'\n\nCipher text: {ciphertext}\n\nSignature: {signature}\n\n')

if plain_text:
    print(f'Plain text: {plain_text}')
else:
    print('Could not decrypt the message')

if verify_sha256(plain_text, signature, pub_key):
    print('Signature verified!')
else:
    print('Could not verify the message signature.')