
import pandas as pd

def get_bus_indexes(df):
    # Calculate the mean value of the 'bus' column
    mean_bus = df['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes

# Example usage
dataset_path = 'dataset-1.csv'
df = pd.read_csv(dataset_path)
result_list = get_bus_indexes(df)
print(result_list)
