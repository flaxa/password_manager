import os

DATA_DIR = os.path.dirname(__file__)
HASH_PATH = os.path.join(DATA_DIR, "password.hash")

def save_hash(hashed_password):
    file = open(HASH_PATH, "w")
    file.write(hashed_password)
    file.close()

def get_hash():
    file = open(HASH_PATH, "r")
    hashed_password = file.read()
    file.close()
    return hashed_password
    
def hash_exists():
    return os.path.exists(HASH_PATH)