from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from regression_model.processing import preprocessors as pp
from regression_model.config import config

import logging


_logger = logging.getLogger(__name__)


flight_duration_pipe = Pipeline(
    [
        ('rare_label_encoder',
            pp.RareLabelCategoricalEncoder(
                tol=0.01,
                variables=config.CATEGORICAL_VARS)),

        ('categorical_encoder',
            pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),

        ('scaler', StandardScaler()),

        ('Linear_model', Ridge(alpha=0.005, random_state=42))
    ]
)
