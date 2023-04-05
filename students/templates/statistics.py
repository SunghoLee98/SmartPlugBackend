import pandas as pd
import numpy as np
from sklearn import svm
from datetime import datetime


def statmodel(id, type, day):  # 함수를 불러오는 방식으로 사용 id,type,day 는 데이터베이스 불러올때 사용

    # 해당 데모를 실행할 날짜
    # 오늘 날짜로 하고 싶으면 day=datetime.today().day

    if type == '에어컨':  # 어떤 제품을 학습시킬 것인지 알려주는 부분 (더미데이터를 가져오기 위해)
        df = pd.read_csv('aircon.csv')
    elif type == '헤어드라이기':  # 데모에서 어떤것을 사용하느냐에따라 바뀔것임
        df = pd.read_csv('hairdry.csv')
    else:
        return -1;
        # !서버에 저장된 csv파일을 불러오는 작업 필요

    X = pd.DataFrame.to_numpy(df.iloc[0:12, 0:day])
    # 더미데이터에서 각 달(month)에서 day만큼 데이터를 불러와서 학습시킬 데이터 준비

    Y = pd.DataFrame.to_numpy(df.iloc[:, [30]])
    # 더미테이터에서 각 달에서 최종적으로 30일까지 얼마나 소비했는지 불러와서 학습시킬 데이터 준비

    Y = Y.astype(np.int64)
    # 데이터 형변환 (안그럼 오류남)

    clf = svm.SVC(kernel='linear')
    realdata = np.array([[234, 214, 257, 269, 280.3]])
    # realdata 부분에 각 날짜마다 사용된 전력량 필요함   !서버에서 해당월 1일부터 해당요일까지 전력량을 불러오는 코드 추가 필요 (id,type이용)
    # 측정일이 15일이면 1~15일까지 각날들의 누적 전류량   !샘플은 헤어드라이, 불러오기 힘들면 그냥 여기서 입력 .day랑 배열길이가 똑같아야함!

    clf.fit(X, np.ravel(Y))  # 학습 -ing

    prediction = clf.predict(realdata)  # 예측값 wh 단위
    output = prediction[0] / 1000  # value 뽑아서 kwh로 바꿔줌

    if type == "에어컨":
        output = output - 39  # 겨울이니까 전력량 빼주기

    output = round(output, 3)  # 소수점 세자리까지
    return output  # 최종결과 반환


id = 6
type = "헤어드라이기"
day = 5
print(statmodel(id, type, day))