import pandas as pd

import joblib
import config

import os
dirname = os.path.dirname(__file__)

def make_prediction(input_data):
    
    _pipe_price = joblib.load(filename=config.PIPELINE_NAME)
    
    results = _pipe_price.predict(input_data)

    return results
   
if __name__ == '__main__':
    
    # test pipeline
    import numpy as np
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
    from math import sqrt

    # read data
    train_file = os.path.join(dirname, config.TRAINING_DATA_FILE)
    test_file = os.path.join(dirname, config.TEST_DATA_FILE)
    train_data = pd.read_csv(train_file)
    test_data = pd.read_csv(test_file)

    # obtain train data
    X_train = train_data[config.FEATURES]
    y_train = train_data[config.TARGET]

    # obtain test data
    X_test = test_data[config.FEATURES]
    y_test = test_data[config.TARGET]
    
    pred = make_prediction(X_test)
    
    # determine metrics
    print('test rmse: {:.3f}'.format(sqrt(mean_squared_error(y_test, pred))))
    print('test mae: {:.3f}'.format(mean_absolute_error(y_test, pred)))
    print('test r2: {:.3f}'.format(r2_score(y_test, pred)))
    