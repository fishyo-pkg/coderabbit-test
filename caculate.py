# 일부러 비효율적으로 작성된 샘플 코드입니다.
def calculate_total(items):
    t = 0
    for i in range(len(items)):
        # 변수 이름이 불분명하고, 불필요한 연산이 포함됨
        val = items[i]
        t = t + val
    
    # 결과 출력 (함수는 값을 반환하는 것이 좋음)
    print("Total is:", t)

# 하드코딩된 데이터 (보안상 좋지 않은 예시 포함 가능)
my_list = [10, 20, 30]
calculate_total(my_list)
