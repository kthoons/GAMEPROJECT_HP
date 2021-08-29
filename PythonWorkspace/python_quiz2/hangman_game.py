from random import *

# 랜덤 박스 (단어 추가 가능)
quiz_box = ["apple", "banana", "orange"]

ran_num = int(random() * int(len(quiz_box)))
sel_voc = quiz_box[ran_num]

chance = 10
blank = []

for i in range(len(sel_voc)):
    blank.append("_")

while chance > 0 :
    
    count = 0

    for i in range(len(sel_voc)):
        print(blank[i], end=" ")
    
        
    res = 0
    answer = input("\nInput letter > ")

    for idx,i in enumerate(sel_voc) :

        if i == answer :
            blank[idx] = i
            res += 1

    for i in blank:
        if i == "_":    
            count += 1

    if res >= 1 :
        print("Correct\n")
    else :
        print("Wrong\n")
        chance -= 1

    if count == 0:
        for i in range(len(sel_voc)):
            print(blank[i], end=" ")
        print("\nSucceed")
        break
    
