import pandas as pd
import requests
import json
import time

if __name__ == "__main__":
    # 모델에 맞는 컬럼보다 많음
    # data = pd.read_csv("real_test_input.csv", index_col = False).iloc[:,1:].head(20)

    # 모델에 맞는 컬럼으로 임시 분리
    ## test1 - 1,000개 -> 10.57초
    data = pd.read_csv("real_test_input.csv", index_col = False).iloc[:,9:].head(100)

    ## test2 - 10,000개 -> 37.8초

    ## test2 - 전체
    # data = pd.read_csv("real_test_input.csv", index_col=False).iloc[:, 9:]

    data = data.to_numpy().tolist()

    headers = {'Content-Type': 'application/json'}
    address = 'http://ip주소/predict'

    start = time.time()
    result = requests.post(address, data = json.dumps(data), headers=headers)
    end = time.time()
    print(f"{end - start:.5f} sec")

    print(json.loads(result.text))