fName = input('what is your first name')
mName = input('what is your middle name')
lName = input('what is your last name')

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f'Welcome to {fName} {mName:.1s} {lName}')
