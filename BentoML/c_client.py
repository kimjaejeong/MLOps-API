import pandas as pd
import requests
import json
import time

if __name__ == "__main__":
    # 모델에 맞는 컬럼보다 많음
    # data = pd.read_csv("real_test_input.csv", index_col = False).iloc[:,1:].head(5)

    # 모델에 맞는 컬럼으로 임시 분리 => Batch False / True
    ## test1 - 10개 -> 0.43초 / 0.86초
    # data = pd.read_csv("real_test_input.csv", index_col = False).iloc[:,9:].head(10)

    ## test2 - 100개 -> 0.65초 / 0.64초
    # data = pd.read_csv("real_test_input.csv", index_col = False).iloc[:,9:].head(100)

    ## test3 - 1,000개 -> 2.6초 / 2.99초
    # data = pd.read_csv("real_test_input.csv", index_col = False).iloc[:,9:].head(1000)

    ## test4 - 10,000개 -> 14초 / 13.27초
    # data = pd.read_csv("real_test_input.csv", index_col=False).iloc[:, 9:].head(10000)

    ## test5 - 20,000개 -> 40초 / Request timeout
    data = pd.read_csv("real_test_input.csv", index_col=False).iloc[:, 9:].head(20000)

    payload = {
        'data': data.to_numpy().tolist()
    }
    # data = data.to_numpy().tolist()

    headers = {'Content-Type': 'application/json'}
    address = 'http://ip주소/predict'

    start = time.time()
    result = requests.post(address, data=json.dumps(payload), headers=headers)
    # result = requests.post(address, data = json.dumps(data), headers=headers)
    end = time.time()
    print(f"{end - start:.5f} sec")
    print(result.text)
    print(json.loads(result.text))


