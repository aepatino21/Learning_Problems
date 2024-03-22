# Realizar un algoritmo que  pida  al  usuario  su  nombre  y  contraseña  y  le  de  tres  oportunidades 
# para  introducir  los  datos  correctos,  que  serán  root y  1234.  Si  los datos  
# introducidos  son  correctos  se  mostrará  por  pantalla  “Bienvenido  al sistema”. En caso 
# contrario se mostrará un mensaje por pantalla indicando que se ha superado el número de 
# intentos permitido


def login_attempts() -> None:
    USERNAME = "root"
    PASSWORD = 1234
    attempts = 3

    # user input
    while True:
        if attempts == 0:
            print("No more attempts allowed!")
            break
        else:
            name = input("Enter your username: ")
            password = int(input("Enter your password: "))
        
            # find out whether the username and password are correct or not
            if name == USERNAME and password == PASSWORD:
                print("Bienvenido al sistema")
                break
            else:
                attempts -= 1
                print(f"Error! Password and/or username are not correct, try again (remaining attempts = {attempts})")


if __name__ == "__main__":
    login_attempts()