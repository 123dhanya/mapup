import pandas as pd

def get_type_count(df):
    # Create a new column 'car_type' based on conditions
    df['car_type'] = pd.cut(df['car'],
                            bins=[float('-inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'],
                            right=False)

    # Calculate the count of occurrences for each car_type category
    type_counts = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts

# Example usage
dataset_path = 'dataset-1.csv'
df = pd.read_csv(dataset_path)
result_dict = get_type_count(df)
print(result_dict)
