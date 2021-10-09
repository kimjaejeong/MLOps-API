# Prediction Service Class 생성
from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import DataframeInput
from bentoml.frameworks.xgboost import XgboostModelArtifact
import xgboost

import pandas as pd
import numpy as np
import json

from typing import List
from bentoml.types import JsonSerializable



@env(infer_pip_packages=True)
@artifacts([XgboostModelArtifact('model')])
class KbClassifier(BentoService):
    """
    A minimum prediction service exposing a Scikit-learn model
    """

    # @api(input=DataframeInput(), batch=True)
    @api(input=DataframeInput(), batch=True)
    # def predict(self, data : json):
    def predict(self, data : pd.DataFrame):
        """
        An inference API named `predict` with Dataframe input adapter, which codifies
        how HTTP requests or CSV files are converted to a pandas Dataframe object as the
        inference API function input
        """
        # testX = data.drop('TARGET', axis=1)
        # testY = data.TARGET
        # testX = testX.to_numpy()
        # testY = testY.to_numpy()

        ########################################################################
        testX = data.iloc[:,:-1].to_numpy()
        testY = data.iloc[:,-1].to_numpy()

        testD = xgboost.DMatrix(testX, label=testY)

        predY = self.artifacts.model.predict(testD)
        predY = np.argmax(predY, axis=1)
        return predY
