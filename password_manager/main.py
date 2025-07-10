from password_manager import cli
from password_manager.data import filemanager
from password_manager import encryption
import gc

def main():
    if(is_setup()):
        run_setup()
    else:
        run_program()

    
def is_setup():
    return not filemanager.hash_exists()


def run_setup():
    password = cli.setup_master_password()
    hashed_password = encryption.get_hash(password)
    del(password)
    gc.collect()
    filemanager.save_hash(hashed_password)
    print("Setup complete. You may now re run to use the vault!")

def run_program():
    print("Welcome to the Password Manager CLI!")
    master_password = cli.get_master_password()
    hashed_password = filemanager.get_hash()
    is_correct, is_not_secure = encryption.check_hash(master_password, hashed_password)
    if not is_correct:
        print("Incorrect password. Exiting.")
        return
    print("Password verified successfully.")
    option = cli.get_option()
    if option == "Add a new password":
        add_password()
    elif option == "Retrieve a password":
        retrieve_password()
    elif option == "List all passwords":
        list_passwords()
    elif option == "Exit":
        print("Exiting the Password Manager. Goodbye!")
        return
    

def add_password():
    # Placeholder for adding a password
    print("Adding a password...")

def retrieve_password():
    # Placeholder for retrieving a password
    print("Retrieving a password...")

def list_passwords():
    # Placeholder for listing all passwords
    print("Listing all passwords...")



if __name__ == "__main__":
    main()
    
    