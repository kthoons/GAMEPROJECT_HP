import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ...

p = re.compile("ca.e") 
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination | fade (X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)

def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력받은 문자열
        print("m.start():", m.start()) # 일치하는 문자열의 끝 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

# m = p.match("cakse") # match : 주어진 문자열의 처음부터 일치하는지 확인 ex) careless 가능
# print_match(m)

# m = p.search("careless") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)





# <정리>

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination | fade (X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)

# w3school 페이지 아래에 Learn Pyton 들어가서 왼쪽에 RegEx 에서 예제들로 공부가능
# python re 검색후 docs 클릭 
    