from argon2 import PasswordHasher
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import os

def get_hash(password: str) -> str:
    ph = PasswordHasher()
    return ph.hash(password)

def check_hash(password: str, hashed_password: str) -> tuple:
    ph = PasswordHasher()
    is_correct = ph.verify(hashed_password, password)
    is_not_secure = ph.check_needs_rehash(hashed_password)
    if is_not_secure:
        raise ValueError("Password hash needs to be rehashed for security reasons.")
    return is_correct, is_not_secure

def derive_key(password: str, salt: str) -> bytes:

    salt = base64.urlsafe_b64decode(salt.encode('utf-8'))

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_password(key: bytes, plaintext: str) -> bytes:
    f = Fernet(key)
    return f.encrypt(plaintext.encode())

def decrypt_password(key: bytes, token: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(token).decode()