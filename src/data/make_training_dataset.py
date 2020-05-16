"""
This script consolidates the monthly flights data downloaded directed from 
BTS website in 2017 and 2018. All flights arrived and departed at ATL airport are exported
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

file_path = 'C:\\Users\\lis\\repos\\flight_duration_prediction\\data\\raw\\training_data\\'
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
train_dataset_path = 'C:\\Users\\lis\\repos\\flight_duration_prediction\\data\\raw\\'
train_dataset_name = 'training_data_ATL.csv'

with open(train_dataset_path + train_dataset_name, "w") as my_empty_csv:
    pass

# CRSArrTime is an int with max four digits. Append zeros to make all consist of 4 digits
# then convert to a datetime object
def format_time(CRSTime):
    time_str = str(CRSTime)
    formatted_time_str = time_str.zfill(4)
    time = pd.to_datetime(formatted_time_str, format="%H%M")
    return time

one_day = pd.Timedelta('1 days')
five_min = pd.Timedelta('5 minutes')
ten_min = pd.Timedelta('10 minutes')
fifteen_min = pd.Timedelta('15 minutes')
twenty_min = pd.Timedelta('20 minutes')
twenty5_min = pd.Timedelta('25 minutes')
thirty_min = pd.Timedelta('30 minutes')

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
    
    # find arrival and departure flights of ATL airport
    atl_id = 10397
    arrivals = flights[flights['DestAirportID']==atl_id]
    departures = flights[flights['OriginAirportID']==atl_id]
    
    # convert FlightDate to a datetime object
    arrivals['FlightDate'] = pd.to_datetime(arrivals['FlightDate'])
    departures['FlightDate'] = pd.to_datetime(departures['FlightDate'])

    # convert CRS times to datetime objects
    arrivals['CRSArrTime'] = arrivals['CRSArrTime'].apply(lambda x: format_time(x)).dt.time
    departures['CRSDepTime'] = departures['CRSDepTime'].apply(lambda x: format_time(x)).dt.time

    # for arrival flights, the flight date may not be equal to ARRIVAL date
    # e.g., depart at origin airport at 2350 1 Jan, then arrived at ATL at 0340 2 Jan at ATL
    # add a column called ArrivalDate in arrivals dataframe
    # initialize the column values to be the same as FlightDate
    arrivals['ArrivalDate'] = arrivals['FlightDate']

    # for the arrival flights with CRSArrTime < CRSDepTime (convert CRSDepTime to a datetime object first)
    # let ArrivalDate be FlightDate + 1
    arrivals['CRSDepTime'] = arrivals['CRSDepTime'].apply(lambda x: format_time(x)).dt.time
    arrivals.loc[arrivals.CRSArrTime < arrivals.CRSDepTime, "ArrivalDate"] = arrivals['FlightDate'] + one_day

    # ARR_Flight_SLDT is obtained by concatenating ArrivalDate and CRSArrTime
    arrivals['ARR_Flight_SLDT'] = arrivals.apply(lambda r: pd.datetime.combine(r['ArrivalDate'], r['CRSArrTime']), 1)

    # concatenate departure date and time to generate STOT first
    departures['DEP_Flight_STOT'] = departures.apply(lambda r: pd.datetime.combine(r['FlightDate'], r['CRSDepTime']), 1)
    
    # initialize new feature columns in arrivals df
    feature_list = ['Num_Arr_SLDT-30', 'Num_Arr_SLDT-25', 'Num_Arr_SLDT-20', 'Num_Arr_SLDT-15', 'Num_Arr_SLDT-10',\
                    'Num_Arr_SLDT-5', 'Num_Arr_SLDT-0', 'Num_Arr_SLDT+5', 'Num_Arr_SLDT+10', 'Num_Arr_SLDT+15',\
                    'Num_Arr_SLDT+20', 'Num_Arr_SLDT+25', 'Num_Dep_SLDT-30', 'Num_Dep_SLDT-25', 'Num_Dep_SLDT-20',\
                    'Num_Dep_SLDT-15', 'Num_Dep_SLDT-10', 'Num_Dep_SLDT-5', 'Num_Dep_SLDT-0', 'Num_Dep_SLDT+5',\
                    'Num_Dep_SLDT+10', 'Num_Dep_SLDT+15', 'Num_Dep_SLDT+20', 'Num_Dep_SLDT+25']

    for feature in feature_list:
        arrivals[feature] = 0
    
    
    # generate the dep STOT df and stot series
    dep_flight_STOT = departures[['FlightDate','DEP_Flight_STOT']]
    stot = dep_flight_STOT['DEP_Flight_STOT']

    # generate the arr SLDT df and sldt series
    arr_flight_SLDT = arrivals[['FlightDate','ARR_Flight_SLDT']]
    sldt = arr_flight_SLDT['ARR_Flight_SLDT']
    
    features = ['Num_Dep_SLDT-30', 'Num_Dep_SLDT-25', 'Num_Dep_SLDT-20',\
                'Num_Dep_SLDT-15', 'Num_Dep_SLDT-10', 'Num_Dep_SLDT-5', 'Num_Dep_SLDT-0', 'Num_Dep_SLDT+5',\
                'Num_Dep_SLDT+10', 'Num_Dep_SLDT+15', 'Num_Dep_SLDT+20', 'Num_Dep_SLDT+25']

    features2 = ['Num_Arr_SLDT-30', 'Num_Arr_SLDT-25', 'Num_Arr_SLDT-20', 'Num_Arr_SLDT-15', 'Num_Arr_SLDT-10',\
                 'Num_Arr_SLDT-5', 'Num_Arr_SLDT-0', 'Num_Arr_SLDT+5', 'Num_Arr_SLDT+10', 'Num_Arr_SLDT+15',\
                 'Num_Arr_SLDT+20', 'Num_Arr_SLDT+25']

    # loop through every arrival flight in arrivals df
    for i in arrivals.index:
    
        this_SLDT = arrivals['ARR_Flight_SLDT'][i]
    
        minus_30 = this_SLDT - thirty_min
        minus_25 = this_SLDT - twenty5_min
        minus_20 = this_SLDT - twenty_min
        minus_15 = this_SLDT - fifteen_min
        minus_10 = this_SLDT - ten_min
        minus_5 = this_SLDT + five_min
        plus_30 = this_SLDT + thirty_min
        plus_25 = this_SLDT + twenty5_min
        plus_20 = this_SLDT + twenty_min
        plus_15 = this_SLDT + fifteen_min
        plus_10 = this_SLDT + ten_min
        plus_5 = this_SLDT + five_min
    
        time_list = [minus_30, minus_25, minus_20, minus_15, minus_10, minus_5, this_SLDT,\
                     plus_5, plus_10, plus_15, plus_20, plus_25, plus_30]

        for j in range(len(time_list)-1):
            mask_dep = (time_list[j] <= stot) & (stot < time_list[j+1])
            arrivals[features[j]][i] = dep_flight_STOT.loc[mask_dep].shape[0]
        
            mask_arr = (time_list[j] <= sldt) & (sldt < time_list[j+1])
            arrivals[features2[j]][i] = arr_flight_SLDT.loc[mask_arr].shape[0]
    
    # to remove the arrival flight itself from the number of arrival flights at its SLDT
    arrivals['Num_Arr_SLDT-0'] = arrivals['Num_Arr_SLDT-0'] - 1
    
    # append the df to csv file
    arrivals.to_csv(train_dataset_path + train_dataset_name, mode='a', header=first_df_flag)
    
    # set first_df_flag to be false for latter dataframes
    first_df_flag = False