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
    
    