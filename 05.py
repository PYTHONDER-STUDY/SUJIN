word = input().lower()
for i in range(1, len(word)//2): # 인덱스번호 1부터 word 절반만큼. 가운데 문자는 무시.
    if word[i-1] == word[-i]: 
    # 첫번째 반복에서 i-1==0, -i==-1(가장 오른쪽)이 됨. 두번째 반복은 i-1==1, -i==-2(오른쪽에서 두번째)
        answer = 1
    else:
        answer = 0
        break
print(answer)

# 인덱스 이해하기
# word = 'abcde'
# print(word[0]) # a
# print(word[-2]) # d