import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
data = pd.read_csv("C:\creditcard.csv")


#데이터 전처리 (Train / Test 데이터 비율을 8:2로 설정하여 나눔)
train, test = train_test_split(data, test_size=0.2, random_state=180831)

#시각화 과제에서 선정한 feature를 선택
features = ['V1', 'V2', 'V3', 'V4', 'Amount']
Y = ['Class']

#Logistic Regression
LogR = linear_model.LogisticRegression()
LogR.fit(train[features], train[Y]['Class'])

#score 계산
print(LogR.score(test[features], test[Y]))