import string 
import random
length = int(input("enter the password length :"))
print('''choose from these to set your password :
      1. digits
      2.letters
      3. special characters
      4, exit''')
plist = ""
while(True):
    choice = int(input("choose your choice : "))
    if(choice == 1):
        plist += string.digits
    elif(choice == 2):
        plist += string.ascii_letters
    elif(choice == 3):
        plist += string.punctuation
    elif(choice == 4):
        break
    else:
        print("choose a valid option!")
password = []
for i in range(length):
    randomchar = random.choice(plist)
    password.append(randomchar)
print("the random password is " +" ".join(password))
