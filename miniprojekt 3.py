def passwordchecker(password):


    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    special_chars = "!@#$%^&*()‐_=+[{]}:',<.>/?"

    if len(password) < min_length:
        print('dit kodeord er for kort, minimum 8 tegn')
        return False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True

    if not has_uppercase:
        print("dit password skal have et eller flere store bogstaver")
        return False
    elif not has_lowercase:
        print("dit password skal have et eller flere små bogstaver")
        return False
    elif not has_digit:
        print("dit password skal have minimum 1 digit")
        return False
    elif not has_special_char:
        print("dit password skal have minimum 1 speciel karacter")
        return -False

    else:
        print("du har et stærkt kodeord")



password = input('Skriv dit kodeord her: ')
passwordchecker(password)

