import pandas as pd

def find_ids_within_ten_percentage_threshold(distance_data, reference_value):
    # Calculate the average distance for the reference value
    average_distance = distance_data.loc[distance_data['id_start'] == reference_value, 'distance'].mean()

    # Calculate the lower and upper bounds for the 10% threshold
    lower_bound = average_distance - (average_distance * 0.1)
    upper_bound = average_distance + (average_distance * 0.1)

    # Filter the rows based on the 10% threshold
    within_threshold = distance_data.loc[
        (distance_data['id_start'] != reference_value) & 
        (distance_data['distance'] >= lower_bound) & 
        (distance_data['distance'] <= upper_bound)
    ]

    # Get unique values from the 'id_start' column and sort them
    result_ids = sorted(within_threshold['id_start'].unique())

    return result_ids

# Example usage
reference_value = 1  # Replace with the desired reference value
ids_within_threshold = find_ids_within_ten_percentage_threshold(unrolled_distance_df, reference_value)

# Display the sorted list of 'id_start' values within the 10% threshold
print(ids_within_threshold)
