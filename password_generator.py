# Generating a password using python

# Importing the random module
import random
# List of alphabets and strings
alphabets=['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n', 'o','p','q','r','s','t','u','v','x','y','z']
str=""
symbols = ['+','~','!','@','#','$','%','^','&','*','.','?','/','=','-','%',"_"]
for i in range(6):
    # Selecting a character from both symbols and alphabets
    num=random.randint(0,24)
    num2=random.randint(0,16)
    str=f"{alphabets[num]}{symbols[num2]}"+str
password=str
print("The hardest python generated python password :",password)