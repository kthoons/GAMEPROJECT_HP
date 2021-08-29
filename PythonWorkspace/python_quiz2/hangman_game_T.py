from random import *
import time
words = ["apple", "banana", "orange"]
word = choice(words)
print("answer : " + word)
letters = "" # 사용자로부터 지금까지 입력받은 모든 알파벳
chance = 10

while True:

    if chance == 0 :
        time.sleep(2)
        print("\nFail")
        break

    succeed = True
    print()
    for w in word : # a p p l e
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()

    if succeed:
        print("Success")
        break

    letter = input("Input letter > ") # 사용자 입력 받기
    if letter not in letters:
        letters += letter

    if letter in word:
        print("Correct")
    else:
        print("Wrong")
        chance -= 1
    
