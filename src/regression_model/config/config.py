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
    'Num_Arr_SIBT-30',
    'Num_Arr_SIBT-25',
    'Num_Arr_SIBT-20',
    'Num_Arr_SIBT-15',
    'Num_Arr_SIBT-10',
    'Num_Arr_SIBT-0',
    'Num_Arr_SIBT+5',
    'Num_Arr_SIBT+10',
    'Num_Arr_SIBT+20',
    'Num_Arr_SIBT+25',
    'Num_Dep_SIBT-30',
    'Num_Dep_SIBT-25',
    'Num_Dep_SIBT-20',
    'Num_Dep_SIBT-15',
    'Num_Dep_SIBT-10',
    'Num_Dep_SIBT-0',
    'Num_Dep_SIBT+5',
    'Num_Dep_SIBT+10',
    'Num_Dep_SIBT+15',
    'Num_Dep_SIBT+20',
    'Num_Dep_SIBT+25',
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
