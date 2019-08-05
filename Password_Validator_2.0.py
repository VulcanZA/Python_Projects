# Password validator 2.0
# Password criteria :
# Should be longer than 8.
# Should be shorter than 12.
# Should contain a lowercase letter.
# Should contain an uppercase letter.
# Should contain a number.
# Should contain a special symbol, !@#$%^&*()_
# Shouldn't contain a space.
# Password Validator
import re
print('Password criteria:')
print('*Should be longer than 8.')
print('*Should be shorter than 12.')
print('*Should contain a lowercase letter.')
print('*Should contain an uppercase letter.')
print('*Should contain a number.')
print('*Should contain a special symbol, !@#$%^&*()_')
print('*Should not contain a space.')
Error = -1
while Error == -1:
    print('Please enter a password or enter exit to leave.')
    Password = input()
    if ((Password.upper()) == 'EXIT'):
        Error = 0
        break
    elif (len(Password) < 8):
        Error = -1
        print('Invalid password, should be longer than 8.')
    elif (len(Password) > 12):
        Error = -1
        print('Invalid password, should be shorter than 12.')
    elif not re.search("[a-z]", Password):
        Error = -1
        print('Invalid password, should contain a lowercase letter.')
    elif not re.search("[A-Z]", Password):
        Error = -1
        print('Invalid password, should contain an uppercase letter.')
    elif not re.search("[0-9]", Password):
        Error = -1
        print('Invalid password, should contain a number.')
    elif not re.search("[!@#$%^&*()_]", Password):
        Error = -1
        print('Invalid password, should contain a special symbol, !@#$%^&*()_')
    elif re.search("/s", Password):
        Error = -1
        print('Invalid password, should not contain a space.')
    else:
        Error = 0
        print('Valid password!')
