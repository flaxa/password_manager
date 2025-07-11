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
    filemanager.create_vault()
    print("Setup complete. You may now re run to use the vault!")

def run_program():
    print("Welcome to the Password Manager CLI!")
    check_master_password()
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
    # Questions to gather information about the new password
    master_password = check_master_password()
    information = cli.get_new_password_information()
    key = encryption.derive_key(master_password, information['name'])
    encrypted_password = encryption.encrypt_password(key, information['password'])
    filemanager.add_password_to_vault(
        information['name'], 
        information['email'], 
        information['username'], 
        encrypted_password, 
        information['url'], 
        information['notes']
        )
    print(f"Password for {information['name']} added successfully.")
    filemanager.print_db()

def check_master_password():
    master_password = cli.get_master_password()
    hashed_password = filemanager.get_hash()
    is_correct, is_not_secure = encryption.check_hash(master_password, hashed_password)
    if not is_correct:
        raise ValueError("Incorrect master password.")
    else:
        return master_password
    
def retrieve_password():
    master_password = check_master_password()
    name = cli.retrieve_partial_password_name()
    matches = filemanager.get_passwords_by_name(name)
    full_name = cli.retrieve_password_name(matches)
    print(f"Retrieving password for {full_name}...")
    key = encryption.derive_key(master_password, full_name)
    information = filemanager.get_password_by_name(full_name)
    if information is None:
        print(f"No password found for {full_name}.")
        return
    decrypted_password = encryption.decrypt_password(key, information[3])
    print(f"Password for {full_name}: {decrypted_password}")
    print(f"Email: {information[1]}")
    print(f"Username: {information[2]}")
    print(f"URL: {information[4]}")
    print(f"Notes: {information[5]}")

def list_passwords():
    # Placeholder for listing all passwords
    print("Listing all passwords...")



if __name__ == "__main__":
    main()
    
    