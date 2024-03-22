# Calcule la edad de una persona


def age_calculator():
    TODAY_YEAR = 2024
    TODAY_MONTH = 1
    TODAY_DAY = 19

    # user input
    birth_year = int(input("Enter your birth year: "))
    birth_month = int(input("Enter your birth month: "))
    birth_day = int(input("Enter your birth day: "))

    # calculate the age
    age = TODAY_YEAR - birth_year
    if birth_month > TODAY_MONTH:
        age -= 1
    elif birth_month == TODAY_MONTH and birth_day > TODAY_DAY:
        age -= 1

    print(f"You are {age} years old.")


if __name__ == "__main__":
    age_calculator()