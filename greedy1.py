# 문제2 큰수의 법칙은 다양한 수로 이루어진 배열이 있을때 주어진 수들을 M번 더해서 가장 큰 수를 만ㄷ는 법칙이다. 
# 단 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과해서 더해질 수 없는 특징이 있다.
# 배열의 크기는 N, 숫자가 더해지는 횟수 M, 한 숫자가 연속으로 더해질 수 없는 횟수 제한은 K.


# 1번 방법
n, m, k = map(int, input().split()) # n = 배열의 크기, m = 숫자가 더해지는 횟수, k = 한 숫자가 연산 초과횟수제한
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0 

while True:
    for i in range(k): # 가장 큰 수는 k의 횟수제한이 있다.
        if m == 0: # 단 숫자가 더해지는 횟수가 0일 경우 더이상 연산을 할 수 없으므로 break 처리
            break 
        result += first # m != 0  이면 첫번째로 큰 숫자가 연속해서 k 번 더해진다.
        m -= 1 # 그러나 숫자가 더해지는 횟수가 1번씩 차감되도록 설정해서 m의 갯수를 확인한다. 또한 나머지 m의 값이 second 값이 연산될 수 있도록 한다.
        if m == 0: # m = 0이면 더이상의 연산이 필요 없이 result 값만 가져오면 된다. 
            break 
        result += second # 만약 m이 0이 아니라면 m의 남은 횟수만큼 second값이 더해질 수 있도록 한다. 
        m -= 1
        
print(result)
        
# 2번 방법
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / k+1) * k # 가장 큰 수가 반복되는 횟수
count += m % (k+1) # count 연산이 딱 떨어지지 않을때를 대비, 나머지를 더해주면 횟수가 나온다.

result += first * count 
result += second * (m - count)



