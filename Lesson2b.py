# using if else, elif with strings

county = str(input('Which county to visit:'))

if county.lower() == 'kisumu':
    print('Visit lake victoria')

elif county.lower() == 'meru':
    print(' Bring some bananas')

else:
    print('Not available')



import re
password = str(input('What is your password:'))
if len(password) < 8:
    print('Your password is too short')

elif password.startswith('M'):
    print('Password should not start with an M')

elif not re.search("[0-9]", password):
    print('A number is not available')

elif not re.search("[A-Z]", password):
    print('A capital is not available')

elif not re.search("[a-z]", password):
    print('A small letter is not available')


elif not re.search("[_@#$^&*]", password):
    print('A symbol is not available')

else:
    print('Password is valid')