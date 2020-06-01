import pathlib

import regression_model


PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

# data
TESTING_DATA_FILE = "test_data.csv"
TRAINING_DATA_FILE = "train.csv"
TARGET = "SalePrice"


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
