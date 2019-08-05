# Password Validator by VulcanZA
# Password criteria :
# Should be longer than 8.
# Should be shorter than 12.
# Should contain a lowercase letter.
# Should contain an uppercase letter.
# Should contain a number.
# Should contain a special symbol, !@#$%^&*()
# Shouldn't contain a space.
# Password Validator
import re
print('Enter a password to validate')
Password = input()
Error = 0
while True:
    if (len(Password) < 8):
        Error = -1
        print('Password should be longer than 8')
        break
    elif (len(Password) > 12):
        Error = -1
        print('Password should not be longer than 12')
        break
    elif not re.search("[a-z]", Password):
        Error = -1
        print('Password should contain lowercase letters')
        break
    elif not re.search("[A-Z]", Password):
        Error = -1
        print('Password should contain uppercase letters')
        break
    elif not re.search("[0-9]", Password):
        Error = -1
        print('Password should contain a number')
        break
    elif not re.search("[!@#$%^&*()]", Password):
        Error = -1
        print('Password should contain a special symbol')
        break
    elif re.search("\s", Password):
        Error = -1
        print('Password should not contain a space')
        break
    else:
        Error = 0
        print("Valid Password")
        break

if Error == -1:
    print("Invalid Password")
