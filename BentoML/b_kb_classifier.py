# Prediction Service Class 생성
from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import DataframeInput, JsonInput
from bentoml.frameworks.xgboost import XgboostModelArtifact
import xgboost as xgb

import pandas as pd
import numpy as np
import json


from bentoml.types import JsonSerializable
from typing import List


@env(infer_pip_packages=True)
@artifacts([XgboostModelArtifact('model')])
class KbClassifier(BentoService):
    """
    A minimum prediction service exposing a Scikit-learn model
    """

    @api(input=JsonInput(), batch=False)
    # @api(input=JsonInput(), batch=True)
    # @api(input=DataframeInput(), batch=True)

    def predict(self, parsed_json):
    # def predict(self, parsed_json_list: List[JsonSerializable]):
    # def predict(self, data : pd.DataFrame):
        """
        An inference API named `predict` with Dataframe input adapter, which codifies
        how HTTP requests or CSV files are converted to a pandas Dataframe object as the
        inference API function input
        """

        data = parsed_json['data']
        data = pd.DataFrame(data)
        testX = data.iloc[:,:-1].to_numpy()
        testY = data.iloc[:,-1].to_numpy()

        testD = xgb.DMatrix(testX, label=testY)

        predY = self.artifacts.model.predict(testD)
        predY = np.argmax(predY, axis=1)

        return predY
