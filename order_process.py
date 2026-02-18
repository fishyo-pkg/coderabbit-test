# 주문 처리를 위한 샘플 코드 (의도적인 오류 포함)
import datetime

def process_order(item_name, quantity, price_per_unit):
    # 1. 보안 위험: API 키가 코드에 노출됨 (Hardcoded Secret)
    API_KEY = "SG.xK92ls0283SL_example_key" 
    
    # 2. 논리 오류: 수량이 0이나 음수일 때 체크가 없음
    total_price = quantity * price_per_unit
    
    # 3. 비효율적 연산: 굳이 필요 없는 반복문으로 시간 낭비
    items_list = []
    for i in range(quantity):
        items_list.append(item_name)
    
    # 4. 가독성 및 유지보수: 세금(10%)이 하드코딩되어 있음
    final_amount = total_price * 1.1 
    
    # 5. 에러 처리 부재: 파일 저장 시 발생할 수 있는 오류를 무시함
    f = open("order_log.txt", "a")
    f.write(f"{datetime.datetime.now()}: {item_name} - {final_amount}\n")
    f.close()

    return final_amount

# 테스트 호출
print(process_order("Knit Sweater", -5, 15.0))
