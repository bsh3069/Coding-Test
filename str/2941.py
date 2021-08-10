array = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
# for문을 써서 array에 있는것을 하나씩 불러온다.
for i in array:
    # 문자열에 replace를 써서 array에 있는 문자열을 특정 문자로 바꿔준다.
    word = word.replace(i,'1')
# 문자열 개수 출력
print(len(word))
