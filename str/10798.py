# 5개의 입력           
array = []
for _ in range(5):
    a= input()
    array.append(a)
# 이중  for문 사용
for i in range(15):
    for j in range(5):
        if i >= len(array[j]):
            continue
        else:
            print(array[j][i],end='')
