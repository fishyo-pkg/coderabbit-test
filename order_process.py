# 주문 처리를 위한 샘플 코드 (의도적인 오류 포함)
import datetime

def process_order(item_name, quantity, price_per_unit):
import os
import datetime

def process_order(item_name, quantity, price_per_unit):
    # 필요시 환경 변수에서 API 키 로드
    # api_key = os.environ.get("ORDER_API_KEY")
    
    if quantity <= 0:
        raise ValueError("수량은 양수여야 합니다")
    if price_per_unit < 0:
        raise ValueError("단가는 음수일 수 없습니다")
    
    # 2. 논리 오류: 수량이 0이나 음수일 때 체크가 없음
    total_price = quantity * price_per_unit
    

    
    # 4. 가독성 및 유지보수: 세금(10%)이 하드코딩되어 있음
    final_amount = total_price * 1.1 
    
    # 5. 에러 처리 부재: 파일 저장 시 발생할 수 있는 오류를 무시함
    try:
        with open("order_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {item_name} - {final_amount}\n")
    except IOError as e:
        # 로깅 실패 시 처리 (예: 로그 출력 또는 무시)
        print(f"로그 기록 실패: {e}")

    return final_amount

# 테스트 호출
print(process_order("Knit Sweater", -5, 15.0))
