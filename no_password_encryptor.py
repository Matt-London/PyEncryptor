import random
import string
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
print(" ")
print("Because encryption looks better when it's readable, kind of")
print(" ")
def encrypt():
  _userinput = input("So enter the text that you would like to encrypt below:\n")
  _length = len(_userinput)
  _newinput = ""
  for x in _userinput:
    _randominput=""
    _randominputtwo=""
    for number in range(11):
      _randominput += random.choice(string.ascii_letters + string.digits)
      _randominputtwo += random.choice(string.ascii_letters + string.digits)
    _newinput+= _randominput + x + _randominputtwo
  print("The text has now been encrypted!")
  print("It reads:")
  print(_newinput)
def decrypt():
  _userinput = str(input("So enter the text you would like to decrypt below:\n"))
  _length = len(_userinput)
  _newinputnew = ""
  _newinputnew = _userinput[11::23]
  print("Done decrypting.\n")
  print("The message reads:\n")
  print(_newinputnew + "\n\n")
loop="yes"
while loop == "yes":
  print("Would you like to encrypt or decrypt a message?")
  print("1.)  Encrypt")
  print("2.)  Decrypt")
  _answer = input("\n")
  if _answer == "1":
    encrypt()
  elif _answer == "2":
    decrypt()