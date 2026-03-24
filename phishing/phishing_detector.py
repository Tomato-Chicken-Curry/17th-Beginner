import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 1. 학습용 데이터 준비 (간단한 예시)
data = {
    'url': [
        'google.com', 'naver.com', 'github.com', 'daum.net', 
        'secure-login-naver.com', 'update-google-account.net', 
        'free-iphone-event.xyz', 'my-bank-check.info'
    ],
    'label': ['정상', '정상', '정상', '정상', '피싱', '피싱', '피싱', '피싱']
}

df = pd.DataFrame(data)

# 2. 특징 추출 (URL 텍스트를 숫자로 변환)
cv = CountVectorizer()
X = cv.fit_transform(df['url'])
y = df['label']

# 3. AI 모델 생성 및 학습 (로지스틱 회귀 사용)
model = LogisticRegression()
model.fit(X, y)

# 4. 새로운 URL 테스트 함수
def predict_url(new_url):
    new_data = cv.transform([new_url])
    prediction = model.predict(new_data)
    return prediction[0]

# 5. 결과 출력
print("--- AI 피싱 URL 탐지 결과 ---")
test_list = ['google.com', 'login-check-security.xyz']

for url in test_list:
    result = predict_url(url)
    print(f"URL: {url} -> 결과: {result}")
