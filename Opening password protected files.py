passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
  print('Access granted')
  if typedPassword == '12345':
    { print('wrong password.')
else:
     print('Access denied')
