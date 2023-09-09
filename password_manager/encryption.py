from argon2 import PasswordHasher


def get_hash(password):
    ph = PasswordHasher()

    return ph.hash(password)

def check_hash(password, hashed_password):
    ph = PasswordHasher()
    is_correct = ph.verify(hashed_password, password)
    is_secure = ph.check_needs_rehash(hashed_password)
    return is_correct, is_secure