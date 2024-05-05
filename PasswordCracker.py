import math, time, random
import itertools
import string
import time
start_time = time.time()
DoTheyHaveAPassword = ""
PasswordConfirm = []
Guess = []
chars = string.printable





Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Capletters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Numbers = ['1','2','3','4','5','6','7','8','9']
Symbols = ['!','@','#','£','%','$','&','*','+','-']

def Generator():
    Length = int(input("How long would you like the password: "))
    for i in range(Length - 3):
        Choice = random.randint(1,4)
        if Choice == 1:
            PasswordConfirm.append(random.choice(Letters))
        elif Choice == 2:
              PasswordConfirm.append(random.choice(Numbers))
        elif Choice == 3:
            PasswordConfirm.append(random.choice(Symbols))
        else:
            PasswordConfirm.append(random.choice(Capletters))
    PasswordConfirm.append(random.choice(Capletters))
    PasswordConfirm.append(random.choice(Symbols))
    PasswordConfirm.append(random.choice(Numbers))
    

def PasswordChecker():
    DoTheyHaveAPassword = input("Would You Like A Randomly Generated Password or not? (Yes/No): ")
    if DoTheyHaveAPassword.lower() == "yes":
        Generator()
    elif DoTheyHaveAPassword == "no":
        PasswordConfirm.append(input("Enter Your Password"))
    else:
        print("Invalid Value")
        PasswordChecker()


def PasswordCracker() :
    for length in range(1, 100):
        for combination in itertools.product(chars, repeat=length):
            PossiblePasswird = "".join(combination)
            print("Trying password:", PossiblePassword)
            if PossiblePassword == PasswordConfirm:
                end_time = time.time()
                print("Password found:", PossiblePassword)
                time_taken = end_time - start_time
                print("Time taken:", time_taken, "seconds")
                raise SystemExit

    
PasswordChecker()
print("".join(PasswordConfirm))
Continue = input("")
PasswordConfirm = "".join(PasswordConfirm)
PasswordCracker()


        

    
    
