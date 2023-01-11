# Type master using python

# Importing the random module and time module
import random
import time
alphabets=['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n', 'o','p','q','r','s','t','u','v','x','y','z']
i=True
print("\t\t\tWELCOME TO THE TYPING TEST !")
mistake=0
no_of_words=0
# Starting count of the time
start_time=time.perf_counter()
while i==True:
    num=random.randint(0,24)
    num1=random.randint(0,24)
    num2=random.randint(0,24)
    num3=random.randint(0,24)
    num4=random.randint(0,24)
    word=f"{alphabets[num]}{alphabets[num1]}{alphabets[num2]}{alphabets[num3]}{alphabets[num4]}"
    print("\tENTER THE GIVEN WORD :",word)
    input_word=input("\tEnter the word :")
    print('\n')
    if input_word=='quit':
        print("\tYou Have Successfully Quitted The Program | Thank You")
        break
    no_of_words=no_of_words+1
    if input_word!=word:
        mistake=mistake+1
        print("you made a mistake",mistake)
    end_time=time.perf_counter()
    if end_time - start_time >= 65:
        print('Time up sorry!!')
        break
# Informing the accuracy to the user
if no_of_words==0:
    accuracy=0
else:
    # calculating the accuracy to the user
    accuracy=int(((no_of_words-mistake)/no_of_words)*100)

print("\tNO OF WORDS PER MINUTE IS  ",no_of_words)
print(f"\tACCURACY IS {accuracy} WPM")
