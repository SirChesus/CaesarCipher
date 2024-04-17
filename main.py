import getpass
from EncryptionCode import EncryptionCode

person_input = getpass.getpass("Type a word to be encrypted: ")
number_of_shift = int(input("How many times shall I shift it? "))
print(' ')

test = EncryptionCode(person_input, number_of_shift, False, 'sleepy')

chooseDef = input("Basic or Advanced Cipher? ")

while test.get_isProper() == False:
  if chooseDef.lower() == 'basic':
    print('Encrypted Message: ')
    encrypted = test.caesarBasic(person_input, number_of_shift)
    print(encrypted)
    test.set_isProper(True)

  elif chooseDef.lower() == 'advanced':
    print('Encrypted Message: ')
    encrypted = test.caesarAdv(person_input, number_of_shift)
    print(encrypted)
    test.set_isProper(True)

  else:
    chooseDef = input("Type either 'basic' or 'advanced': ")
    #continue


print(' ')
password = getpass.getpass("To decrypt, input password: ")
print(' ')

print('Decrypted Message: ')
if chooseDef.lower() == 'basic':
  out = test.keyBasic(encrypted, number_of_shift, password)
  print(out)
if chooseDef.lower() == 'advanced':
  out = test.keyAdv(str(encrypted), number_of_shift, password)
  print(out)
