# Realizar un algoritmo que pida caracteres e imprima „VOCAL‟ si son vocales y „NO VOCAL‟
# en caso contrario, el programa termina cuando se introduce un espacio


def vowels():
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    run_condition = True

    while run_condition:

        # user input
        letter = input("Enter a character: ").lower()
        if letter == " ":
            run_condition = False
        else:
            if letter in vowel_list:
                print("VOWEL")
            else:
                print("NO VOWEL")

    print("\nProgram execution has been completed.")


if __name__ == "__main__":
    vowels()