import pathlib
import regression_model
import pandas as pd


pd.options.display.max_rows = 10
pd.options.display.max_columns = 10


PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

# data
TRAINING_DATA_FILE = "test_data.csv"
TEST_DATA_FILE = "train_data.csv"
TARGET = 'AOBTtoAIBT'

# input variables
FEATURES = [
    'UniqueCarrierCode',
    'OriginAirportID',
    'OriginCityMarketID',
    'OriginState',
    'OBTDelay',
    'OBTDel15',
    'OBTDelayGroups',
    'SOBTtoSIBT',
    'Distance',
    'DistanceGroup',
    'Num_Arr_SIBTm30',
    'Num_Arr_SIBTm25',
    'Num_Arr_SIBTm20',
    'Num_Arr_SIBTm15',
    'Num_Arr_SIBTm10',
    'Num_Arr_SIBTm0',
    'Num_Arr_SIBTp5',
    'Num_Arr_SIBTp10',
    'Num_Arr_SIBTp20',
    'Num_Arr_SIBTp25',
    'Num_Dep_SIBTm30',
    'Num_Dep_SIBTm25',
    'Num_Dep_SIBTm20',
    'Num_Dep_SIBTm15',
    'Num_Dep_SIBTm10',
    'Num_Dep_SIBTm0',
    'Num_Dep_SIBTp5',
    'Num_Dep_SIBTp10',
    'Num_Dep_SIBTp15',
    'Num_Dep_SIBTp20',
    'Num_Dep_SIBTp25',
    'SIBTQuarter',
    'SIBTMonth',
    'SIBTDayOfMonth',
    'SIBTDayOfWeek',
    'SIBTHour'
]

# categorical variables to encode
CATEGORICAL_VARS = [
    'UniqueCarrierCode',
    'OriginAirportID',
    'OriginCityMarketID',
    'OriginState'
]

PIPELINE_NAME = "ridge_regression"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

# used for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05
