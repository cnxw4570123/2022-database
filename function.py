# 1. 아래 설명을 바탕으로 실습을 진행합니다.
# 2. n 값을 input을 이용해 입력받습니다. n은 10상 5000 이하의 값입니다.
# 3. 리스트 A에 n개의 0부터 100 사이의 임의의 랜덤 수를 생성하여 저장합니다.
# 4. 이차원 n x n 리스트 B를 준비한 후, 모든 1 c= j에 대해, B[1] LJ]에 는 A[1]부터 A[J]까지의 합을 계산해 저장하는 sum 함수를 작성합니다.
# 단, sum 함수가 되도록 빠르게 수행될 수 있도록 구현되어야 합니다!!!
# 5. sum 함수의 수행시간을 측정해 출력합니다. (n의 값을 작은 값부터 큰 값까지 골고루 변화하면서 측정합니다)
import random, time 

def sum2(A, n):
    bef = time.process_time()
    B = [[A[i] if i == j else 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i == 0 and j == 0: 
                continue
            # print(f'i: {i}, j:{j}')
            B[i][j] += B[i][j-1] + A[j]
    aft = time.process_time()
    # print(f'{aft - bef:.3f}')
    return f'{aft - bef:.3f}'


n = int(input())
A = [random.randint(0, 100) for i in range(n)]
print(sum2(A, n))
