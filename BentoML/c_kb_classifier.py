# Prediction Service Class 생성
from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import JsonInput
from bentoml.frameworks.sklearn import SklearnModelArtifact
# from bentoml.frameworks.xgboost import XgboostModelArtifact

import pandas as pd

@env(infer_pip_packages=True)
@artifacts([SklearnModelArtifact('model')])
class KbClassifier(BentoService):
    """
    A minimum prediction service exposing a Scikit-learn model
    """

    @api(input=JsonInput(), batch=False)
    def predict(self, parsed_json):
        """
        An inference API named `predict` with Dataframe input adapter, which codifies
        how HTTP requests or CSV files are converted to a pandas Dataframe object as the
        inference API function input
        """
        data = parsed_json['data']
        data = pd.DataFrame(data)
        testX = data.iloc[:,:-1].to_numpy()

        predY = self.artifacts.model.predict(testX)

        return predY.tolist()
