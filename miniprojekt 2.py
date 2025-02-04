
email = str(input("Enter your email: "))

if 7 < len(email) < 30:
    if email.count('@') == 1:
        if email.endswith('.dk'):
            print("din email er vaild")
        else:
            print("du mangler .dk")
    else:
        print("du mangler '@'")
elif len(email) > 30:
    print("din email er for lang")
elif len(email) < 7:
    print("din email er for kort")