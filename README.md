Arrival flight duration (from AOBT to AIBT) prediction at ATL airport
==============================

Predict AOBT-AIBT for arrival flights at ATL airport in the US.

Project Organization
------------

    ├── README.md            <- The top-level README for developers using this project.
    ├── data
    │   ├── external         <- Data from third party sources.
    │   ├── interim          <- Intermediate data that has been transformed.
    │   ├── processed        <- The final, canonical data sets for modeling or testing.
    │   └── raw              <- The original, immutable data dump.
    │
    ├── docs                 <- A default Sphinx project
    │
    ├── notebooks            <- Jupyter notebooks
    |
    ├── src                  <- Source code for use in this project.
    │   ├── handle_raw_data  <- Scripts to preprocess data for building regression_model package
    │   │   └── make_test_dataset.py
    |   |   └── make_train_dataset.py
    │   │
    │   ├── regression_model <- Regression model package. run tox in this folder will generate model.pkl
    |   |
    │   └── tests            <- tests for the regression model
    |
    ├── ml_api               <- ml_api that serves the regression model
    │   ├── __init__.py      <- Makes src a Python module
    │   │
    │   ├── api              <- source code for api
    │   │   └── __init__.py      
    |   |   └── app.py
    │   │   └── config.py
    |   |   └── controller.py
    |   |   └── validation.py
    |   |
    │   ├── tests            <- tests for API endpoints
    |   |
    │   ├── requirements     <- dependencies of API
    |   |
    │   └── diff_test_requirements.txt       
    |                        <- required dependencies for differential test
    |
    ├── scripts              <- sample input JSON files, and the script for publishing model to Gemfury
    |
    └── Dockerfile           <- for generating docker image
