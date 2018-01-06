import random
import getpass
import string
##Greeting
print("Hello")
print("你好")
print("Hola")
print("Welcome to the...")
print("==============================")
print("|                            |")
print("|          Readable          |")
print("|          Encryptor         |")
print("|                            |")
print("==============================")
print("Written By: rmiffi")
print(" ")
print("Because encryption looks better when it's readable, kind of")
print(" ")

def encrypt(_password, _userinput):

  ##Collect password and add necessary characters and str attribute
  _password = str(_password)
  _password += "`"
  _userinput = str(_userinput)
  _length = len(_userinput)
  _newinputone = ""
  _newinputtwo = ""

  ##int variables and fill with giberish
  for x in _password:
    _randominput=""
    _randominputtwo=""
    for number in range(13):
      _randominput += random.choice(string.ascii_letters + string.digits)
      _randominputtwo += random.choice(string.ascii_letters + string.digits)
    _newinputone += _randominput + x + _randominputtwo
  for x in _userinput:
    _randominput=""
    _randominputtwo=""
    for number in range(11):
      _randominput += random.choice(string.ascii_letters + string.digits)
      _randominputtwo += random.choice(string.ascii_letters + string.digits)
    _newinputtwo +=_randominput + x + _randominputtwo
  _finalEncrypt = _newinputone + _newinputtwo
  print("The text has now been encrypted!")
  print("It reads:")
  print(_finalEncrypt)
  input("Press enter to exit:\n")
  exit()

def decrypt(_enteredpassword, _userinput):

  ##grab length, convert password to str, int needed variables
  _enteredpassword = str(_enteredpassword)
  _userinput = str(_userinput)
  _length = len(_userinput)
  _prepassFromEncrypt = ""
  _passFromEncrypt = ""
  _prepassFromEncrypt = _userinput[13::27]

  ##iterate through thh password to remove '`' and what follows
  for x in _prepassFromEncrypt:
    if x == '`':
      break
    else:
      _passFromEncrypt += x

  ##grab the garbled pass
  _garbledpass = ""
  for x in _userinput:
    if x != '`':
      _garbledpass += x
    else:
      break

  ##Test if the password is incorrect and insult if it is
  if _passFromEncrypt != _enteredpassword:
    print("Trying to steal data?\n Shame.")
    input("Press enter to exit:\n")
    exit()

  ##Remove the garbled pass from the encrypted string
  _lengthPass = len(_garbledpass)
  _toRemove = _lengthPass + 25
  _encryptpattern = _userinput[_toRemove::23]

  ##Display decrypted string
  print("Done decrypting.\n")
  print("The message reads:\n")
  print(_encryptpattern + "\n\n")
  input("Press enter to exit:\n")
  exit()

##Setup while loop to be infinite
loop="yes"
while loop == "yes":

  ##Prompt user
  print("Would you like to encrypt or decrypt a message?")
  print("1.)  Encrypt")
  print("2.)  Decrypt")
  _answer = input("\n")

  ##Run encrypt function
  if _answer == "1":
    _password = getpass.getpass("Enter the password you would like to use to encrypt the data:\n")
    _userinput = input("Please enter the text you would like to encrypt:\n")
    encrypt(_password, _userinput)

  ##Run decrypt function
  elif _answer == "2":
    _enteredpassword = getpass.getpass("Enter the password you used to encrypt the data:\n")
    _userinput = input("Please enter the encrypted text:\n")
    decrypt(_enteredpassword, _userinput)
