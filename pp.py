# 간단한 스팸 메시지 분류 프로그램

spam_keywords = ["무료", "당첨", "클릭", "이벤트", "100%", "지금", "혜택"]

def classify_message(message):
    for word in spam_keywords:
        if word in message:
            return "스팸 메시지입니다"
    return "정상 메시지입니다 "

# 실행 부분
print("📩 메시지를 입력하세요:")
user_input = input()

result = classify_message(user_input)
print("결과:", result)
