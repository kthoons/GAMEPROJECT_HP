import keyboard

name = []

while True :

    ask = input("메일을 보낼 유투버 이름을 입력하세요 (y누르면 입력을 마침):")

    if ask == "y" :
        break

    name.append(ask)
    print(name)

for nm in name :
    score_file = open( nm + ".txt", "w", encoding="utf8")
    print("""[메일 본문]
안녕하세요? {}님.
(주)나도출판 편집자 나코입니다.""".format(nm),file=score_file)

    score_file.close()