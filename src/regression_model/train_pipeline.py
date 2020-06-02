import numpy as np

from regression_model import pipeline
from regression_model.processing.data_management import load_dataset, save_pipeline
from regression_model.config import config
from regression_model import __version__ as _version

import logging


_logger = logging.getLogger(__name__)


def run_training() -> None:
    """Train the model"""

    # read training data
    train_data = load_dataset(file_name=config.TRAINING_DATA_FILE)

    # obtain train data
    X_train = train_data[config.FEATURES]
    y_train = train_data[config.TARGET]

    pipeline.flight_duration_pipe.fit(X_train[config.FEATURES], y_train)

    _logger.info(f"saving model version: {_version}")
    save_pipeline(pipeline_to_persist=pipeline.flight_duration_pipe)


if __name__ == '__main__':
    run_training()
