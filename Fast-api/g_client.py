import pandas as pd
import requests
import json
import time

if __name__ == "__main__":
    # 모델에 맞는 컬럼보다 많음
    # data = pd.read_csv("real_test_input.csv", index_col = False).iloc[:,1:].head(20)

    # 모델에 맞는 컬럼으로 임시 분리 => model1 / model2
    ## test1 - 10개 -> 0.83초 / 0,84초
    # data = pd.read_csv("real_test_input.csv", index_col = False).iloc[:,9:].head(10)

    ## test2 - 100개 -> 0.88초 / 0.88초
    # data = pd.read_csv("real_test_input.csv", index_col = False).iloc[:,9:].head(100)

    ## test3 - 1,000개 -> 1.17초 / 0.93초
    # data = pd.read_csv("real_test_input.csv", index_col = False).iloc[:,9:].head(1000)

    ## test4 - 10,000개 -> 3.22초 / 3.13초
    # data = pd.read_csv("real_test_input.csv", index_col=False).iloc[:, 9:].head(10000)

    ## test5 - 20,000개 -> 5.07초 / 7.8초
    data = pd.read_csv("real_test_input.csv", index_col=False).iloc[:, 9:].head(20000)

    payload = {
        'data': data.to_numpy().tolist()
    }
    # data = data.to_numpy().tolist()

    headers = {'Content-Type': 'application/json'}
    address = 'http://ip주소/predict'

    start = time.time()
    result = requests.post(address, data = json.dumps(payload), headers=headers)
    # result = requests.post(address, data = json.dumps(data), headers=headers)
    end = time.time()
    print(f"{end - start:.5f} sec")

    print(result.text)
    print(len(result.text))
    # print(json.loads(result.text))