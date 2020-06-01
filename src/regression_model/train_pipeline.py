import numpy as np
import pandas as pd
import joblib

from regression_model import pipeline
from regression_model.config import config


def save_pipeline(*, pipeline_to_persist) -> None:
    """Persist the pipeline."""

    save_file_name = "regression_model.pkl"
    save_path = config.TRAINED_MODEL_DIR / save_file_name
    joblib.dump(pipeline_to_persist, save_path)

    print("saved pipeline")


def run_training() -> None:
    """Train the model"""

    # read training data
    train_data = pd.read_csv(config.DATASET_DIR / config.TRAINING_DATA_FILE)

    # obtain train data
    X_train = train_data[config.FEATURES]
    y_train = train_data[config.TARGET]

    pipeline.flight_duration_pipe.fit(X_train, y_train)
    save_pipeline(pipeline_to_persist=pipeline.flight_duration_pipe)


if __name__ == '__main__':
    run_training()
