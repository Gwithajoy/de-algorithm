# 문제3. 숫자들이 적힌 카드를 정렬했을때, N은 행의 개수, M은 열의 개수를 의미하며 행에서 가장 숫자가 낮은 카드들을 뽑은 뒤 그 중 가장 큰 숫자를 구하시오.


# 풀이1
n, m = map(int, input().split())
result = 0

# 한줄씩 입력을 받는다. 
for i in range(n):
    data = list(map(int, input(int, input().split())))
    min_data = min(data) # 입력받은 데이터 값(행)에서 가장 작은 수의 값 찾기
    result = max(result, min_data) # 가장 작은 수에서 가장 큰 값을 찾아라
    
    
print(result)
     
