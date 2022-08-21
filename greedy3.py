# 풀이1
n, k = map(int, input().split())
result = 0

# n이 k이상이라면 k로 계속 나누기
while n > k: 
    # n이 k로 나누어 떨어지지 않는다면 1을 계속 빼기 
    while n % k != 0:
        n -= 1
        result += 1
    
    n //= k
    result += 1

# 마지막으로 남은 수에 대해서 1씩 빼기 
while n > 1:
    n -= 1
    result += 1
    
print(result)


# 풀이2 
n, k = map(int, input().split())
result = 0

while True: 
    # n == k 로 나누어떨어지는 수 가 될 때까지 1씩 빼기 
    target = (n // k) * k 
    result = (n - target)
    n = target
    # n이 k보다 작을때(더이상 나눌 수 없을때) 반복문 탈출
    if n < k:
        break 
    result += 1
    n //= k

#남은 수에 대해 1씩 빼기     
result += (n -1)
print(result)
