import random
import string



def fun(len):
    for x in range(0,len):
        uppercase = random.choice(string.ascii_uppercase)
        lowercase = random.choice(string.ascii_lowercase)
        number = random.choice(string.digits)
        punc = random.choice(string.punctuation)
        return (uppercase+lowercase+number+punc)




print("Choose difficulty of password:")
print("1. Easy\n2.Medium\n3.Hard\n\n")
diff = int(input("Enter the difficulty (1-3): "))

if diff == 1:
        len = 2
elif diff == 2:
        len = 3
else:
        len = 4

password = ""
for x in range(0,len):
    password = password + fun(len) 

print("Your password is: "+ password)

