import configure

def main():
    if(is_setup()):
        configure.run_setup()
    else:
        run_program()

    
def is_setup():
    return True

def run_program():
    pass


main()
    
    