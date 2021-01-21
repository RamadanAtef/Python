theName = input('Please enter your name')
theEmail = input('Please enter your e-mail')

Useranme = theEmail[:theEmail.index('@')]
Domain = theEmail[theEmail.index('@') + 1:]

print(f'welcome to {theName} Your E-mail Is {theEmail}')

print(f'Your USername is {Useranme} \n And Your Domain is {Domain}')
