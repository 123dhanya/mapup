
import pandas as pd
​
def calculate_toll_rate(distance_data):
    # Define rate coefficients for each vehicle type
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}
​
    # Calculate toll rates for each vehicle type
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        # Create a new column with the toll rate for the specific vehicle type
        distance_data[vehicle_type] = distance_data['distance'] * rate_coefficient
​
    return distance_data
​
# Example usage
# Assuming unrolled_distance_df is the DataFrame obtained from Question 2
toll_rate_data = calculate_toll_rate(unrolled_distance_df)
​
# Display the resulting DataFrame with toll rates
print(toll_rate_data)
​
