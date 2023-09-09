

def save_hash(hashed_password):
    file = open("./data/password.hash", "w")
    file.write(hashed_password)
    file.close()

def get_hash():
    file = open("./data/password.hash", "r")
    hashed_password = file.read()
    file.close()
    return hashed_password
    