# Prediction Service Class 생성
from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import JsonInput, JsonOutput
from bentoml.frameworks.sklearn import SklearnModelArtifact
from bentoml.frameworks.xgboost import XgboostModelArtifact

import pandas as pd
import json
import numpy as np
import xgboost as xgb

@env(infer_pip_packages=True)
@artifacts([SklearnModelArtifact('model')])
class KbClassifier(BentoService):
    """
    A minimum prediction service exposing a Scikit-learn model
    """

    @api(input=JsonInput(), batch=False)
    # @api(input=JsonInput(), batch=True)
    def predict(self, parsed_json):
        """
        An inference API named `predict` with Dataframe input adapter, which codifies
        how HTTP requests or CSV files are converted to a pandas Dataframe object as the
        inference API function input
        """
        #batch=True일 때 -> return 값이 자꾸 1로만 나옴
        # dict_data = parsed_json[0]
        # data = dict_data['data']

        # batch=False일 때
        data = parsed_json['data']

        data = pd.DataFrame(data)
        testX = data.iloc[:,:-1].to_numpy()

        predY = self.artifacts.model.predict(testX)

        return predY
        # return predY.tolist()
