"""
This script consolidates the monthly flights data downloaded directed from 
BTS website in 2018. All flights arrived and departed at ATL airport are exported
as a CSV file. The CSV file is then manually zipped. The original CSV file is
in my local pc.
Possible improvements:
    output a zip file straight away
"""
import os
import pandas as pd

# ignore warnings
import warnings
warnings.filterwarnings('ignore')

file_path = 'D:\\flight_airborne_time_prediction\\data\\raw\\training_data\\'
file_list = os.listdir(file_path)

# irrelvant fields to the project
field_list = ['FirstDepTime', 'TotalAddGTime', 'LongestAddGTime', 'DivAirportLandings', 'DivReachedDest',\
              'DivActualElapsedTime', 'DivArrDelay', 'DivDistance', 'Div1Airport', 'Div1AirportID', 'Div1AirportSeqID',\
              'Div1WheelsOn', 'Div1TotalGTime', 'Div1LongestGTime', 'Div1WheelsOff', 'Div1TailNum',  'Div2Airport', \
              'Div2AirportID', 'Div2AirportSeqID', 'Div2WheelsOn', 'Div2TotalGTime', 'Div2LongestGTime', 'Div2WheelsOff',\
              'Div2TailNum', 'Div3Airport', 'Div3AirportID', 'Div3AirportSeqID', 'Div3WheelsOn', 'Div3TotalGTime',\
              'Div3LongestGTime', 'Div3WheelsOff', 'Div3TailNum', 'Div4Airport', 'Div4AirportID', 'Div4AirportSeqID', \
              'Div4WheelsOn', 'Div4TotalGTime', 'Div4LongestGTime', 'Div4WheelsOff', 'Div4TailNum', 'Div5Airport', \
              'Div5AirportID', 'Div5AirportSeqID', 'Div5WheelsOn', 'Div5TotalGTime', 'Div5LongestGTime', \
              'Div5WheelsOff', 'Div5TailNum', 'Cancelled', 'CancellationCode', 'Diverted']

# create an empty csv file to be written
train_dataset_path = 'D:\\flight_airborne_time_prediction\\data\\raw\\'
train_dataset_name = 'training_data_ATL_2018.csv'

with open(train_dataset_path + train_dataset_name, "w") as my_empty_csv:
    pass

# flag for header in csv file
first_df_flag = True

# process each zip file
for file_name in file_list:
    # load a zip file
    monthly_flights = pd.read_csv(file_path + file_name)
    
    # find normally operated flights
    not_cancelled = monthly_flights['Cancelled']==0
    not_diverted = monthly_flights['Diverted']==0
    normal_flights = not_cancelled & not_diverted
    flights = monthly_flights[normal_flights]
    
    # remove irrelevant columns
    for field in field_list:
        flights = flights.drop(labels=field, axis=1)
    
    flights.drop(flights.columns[flights.columns.str.contains('unnamed', case=False)],\
                                 axis=1, inplace=True)
    
    # find flights of ATL airport
    arrivals = flights['DestAirportID']==10397
    departures = flights['OriginAirportID']==10397
    all_flights = arrivals | departures
    flights_ATL = flights[all_flights]
    
    # append the df to csv file
    flights_ATL.to_csv(train_dataset_path + train_dataset_name, mode='a', header=first_df_flag)
    
    # set first_df_flag to be false for latter dataframes
    first_df_flag = False