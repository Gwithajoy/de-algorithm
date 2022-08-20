n = 2860
count = 0

# 거슬러줄 수 있는 잔돈을 순서대로 나열
coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    
print(count)