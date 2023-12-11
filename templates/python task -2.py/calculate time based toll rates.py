import pandas as pd
from datetime import time

def calculate_time_based_toll_rates(toll_rate_data, start_col='start_timestamp', end_col='end_timestamp'):
    # Define time ranges and discount factors
    time_ranges = [
        {'start_time': time(0, 0, 0), 'end_time': time(10, 0, 0), 'weekday_factor': 0.8, 'weekend_factor': 0.7},
        {'start_time': time(10, 0, 0), 'end_time': time(18, 0, 0), 'weekday_factor': 1.2, 'weekend_factor': 0.7},
        {'start_time': time(18, 0, 0), 'end_time': time(23, 59, 59), 'weekday_factor': 0.8, 'weekend_factor': 0.7}
    ]

    # Initialize columns for start_day, start_time, end_day, and end_time
    time_data['start_day'] = time_data[start_col].dt.day_name()
    time_data['end_day'] = time_data[end_col].dt.day_name()
    time_data['start_time'] = time_data[start_col].dt.time
    time_data['end_time'] = time_data[end_col].dt.time

    # Initialize columns for each vehicle type with default rate coefficients
    vehicle_types = ['moto', 'car', 'rv', 'bus', 'truck']
    for vehicle_type in vehicle_types:
        time_data[vehicle_type] = 1.0

    # Update vehicle rates based on time ranges
    for time_range in time_ranges:
        weekday_condition = (time_data['start_day'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']) &
                             (time_data['start_time'] >= time_range['start_time']) & (time_data['start_time'] <= time_range['end_time']))
        weekend_condition = (time_data['start_day'].isin(['Saturday', 'Sunday']))

        time_data.loc[weekday_condition, vehicle_types] *= time_range['weekday_factor']
        time_data.loc[weekend_condition, vehicle_types] *= time_range['weekend_factor']

    return time_data[['start_day', 'start_time', 'end_day', 'end_time'] + vehicle_types]

# Example usage
# Assuming time_data is the DataFrame obtained from the previous steps
time_data_with_rates = calculate_time_based_toll_rates(ids_within_threshold,start_col='start_timestamp', end_col='end_timestamp')
