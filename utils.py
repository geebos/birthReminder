import rsa
import base64


def encode(content: str):
    with open('public.pem', 'rb') as f:
        pubkey = rsa.PublicKey.load_pkcs1(f.read())
    result = rsa.encrypt(content.encode(), pubkey)
    return base64.b64encode(result).decode()


def decode(content: str, private_key: str):
    key = rsa.PrivateKey.load_pkcs1(private_key.encode())
    return rsa.decrypt(base64.b64decode(content), key).decode()
