import cli
import data.manager
import encryption
import gc


def run_setup():
    password = cli.setup_master_password()
    hashed_password = encryption.get_hash(password)
    del(password)
    gc.collect()
    data.manager.save_hash(hashed_password)
    print("Setup complete. You may now re run to use the vault!")
    
    