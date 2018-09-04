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
model = LogR.fit(train[features], train[Y]['Class'])

#score 계산
print(model.score(test[features], test[Y]))


#------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

credit_data = pd.read_csv("C:\creditcard.csv")


# parameter 
#           valid_item : list of column - 확인하고자 하는 column name들을 list로 넘겨줌
# 
def GetData(valid_item):
    
    total_item = valid_item +["Class"]
    valid_df = pd.DataFrame(credit_data, columns=total_item)
    target_df = credit_data["Class"]

    # Class 0/1을 data를 분리 함 
    
    class_0_list = credit_data[credit_data["Class"] == 0].index
    class_1_list = credit_data[credit_data["Class"] == 1].index

    # Row 추가하여 확인하는 코드 (교차확인)
    #class_2_list = credit_data[credit_data["Class"] == 1]
    #class_3_list = credit_data[credit_data["Class"] == 1]
    #class_1_list = pd.concat([class_2_list, class_3_list], axis=0)
    #class_1_list = pd.concat([class_1_list, class_1_list], axis=0)
    #class_1_list = class_1_list.index

     #unbalance data여기 때문에 class 0/1의 data 비를 class 1기준으로 balancing 해줌
    data_index = class_0_list[:len(class_1_list)].append(class_1_list[:len(class_1_list)])
    
    # data를 생성
    x_Data = pd.DataFrame(valid_df, index=data_index)
    y_Data = pd.DataFrame(target_df, index=data_index)
    
    return x_Data


total_result = {}
selected_col = []
display_data = {}

# 10개 조합까지 변수를 전진 선택법으로 select하여 socre 값을 확인 
for i in range(10):
    check_col = []
    result = {}
    for column in credit_data.columns:
        
        
        if column != "Time" and column !="Class" and str(column) not in selected_col:
            check_col = []
            # 앞 단계에서 선택된 colunm이 있을 경우 colunm 조합 
            if selected_col != [] :
                check_col += selected_col
               
            check_col.append(column) 
            
            # 선택된 column 기준으로 data 가져옴 
            x_Data=GetData(check_col)
            
            # train test 데이타를 분리 시킴 
            train, test = train_test_split(x_Data, test_size=0.2, random_state=180831)
            
            # LogisticRegression 으로 fit 
            LogR = linear_model.LogisticRegression()
            model = LogR.fit(train[check_col], train['Class'])
            dic_key = ''.join(check_col)
            
            # score 값을 저장 
            result[column] = model.score(test[check_col], test["Class"])
            
            # 결과를 저장함 
            total_result[dic_key] = result[column] 
    # loop 별로 max 값이 나온 column을 확인 
    max_col = (max(result, key=result.get))
    
    print("max col : ", max_col)    
    # 전진 선택방법을 위해서 max column을 추가 시킴
    selected_col = selected_col + [max_col]
    
    # socre 값 확인 
    print("selected col", selected_col, "socre : ", total_result[''.join(selected_col)])
    
    # bar plot를 위해서 선택된 column 들의 score 값을 저장 
    display_data[''.join(selected_col)] = total_result[''.join(selected_col)]

# bar plot 
plt.xticks(rotation=90)
plt.bar(display_data.keys(), display_data.values())
