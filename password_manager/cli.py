from bullet import Bullet, SlidePrompt, Check, Input, YesNo, Numbers,Password


def setup_master_password():
    cli = SlidePrompt(
    [ Password("First time setup, please enter a password: "),
    Password("enter password again: ")])
    result = cli.launch()
    print(result)
    print(result[0][1])
    print(result[1][1])
    while(result[0][1] != result[1][1]):
        cli = SlidePrompt(
        [ Password("Passwords did not match, please enter a password: "),
        Password("enter password again: ")])
        result = cli.launch()
    return result[0][1]
        
    
    