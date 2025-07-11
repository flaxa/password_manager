from bullet import Bullet, SlidePrompt, Check, Input, YesNo, Numbers,Password


def setup_master_password() -> str:
    cli = SlidePrompt(
    [ Password("First time setup, please enter a password: "),
    Password("enter password again: ")])
    result = cli.launch()
    while(result[0][1] != result[1][1]):
        cli = SlidePrompt(
        [ Password("Passwords did not match, please enter a password: "),
        Password("enter password again: ")])
        result = cli.launch()
    return result[0][1]
def get_master_password() -> str:
    cli = SlidePrompt(
    [ Password("Please enter your master password: ")])
    result = cli.launch()
    return result[0][1]
def get_option() -> str:
    options = [
        "Add a new password",
        "Retrieve a password",
        "List all passwords",
        "Exit"
    ]
    cli_prompt = Bullet(
        prompt="What would you like to do?",
        choices=options,
        bullet="> "
    )
    choice = cli_prompt.launch()
    return choice   

def get_new_password_information() -> dict:
    cli = SlidePrompt(
        [
            Input("Enter the name of this record: "),
            Input("Enter the email (optional): "),
            Input("Enter the username (optional): "),
            Password("Enter the password: "),
            Input("Enter the URL (optional): "),
            Input("Enter any notes (optional): ")
        ]
    )
    result = cli.launch()
    return {
        "name": result[0][1],
        "email": result[1][1],
        "username": result[2][1],
        "password": result[3][1],
        "url": result[4][1],
        "notes": result[5][1]
    }
def retrieve_partial_password_name() -> str:
    cli = Input("Enter the name of the password record you want to retrieve: ")
    return cli.launch()
def retrieve_password_name(matches: list) -> str:
    if not matches:
        print("No matches found.")
        return None
    
    cli_prompt = Bullet(
        prompt="Select the password record you want to retrieve:",
        choices=[row[0] for row in matches],
        bullet="> "
    )
    selected = cli_prompt.launch()
    if not selected:
        print("No record selected.")
        return None
    return selected