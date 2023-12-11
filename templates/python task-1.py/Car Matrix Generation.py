import pandas as pd

def generate_car_matrix(dataset_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(dataset_path)

    # Pivot the DataFrame to get the desired matrix
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Set diagonal values to 0
    car_matrix.values[[range(car_matrix.shape[0])]*2] = 0

    return car_matrix

# Example usage
dataset_path = 'dataset-1.csv'
result_matrix = generate_car_matrix(dataset_path)
print(result_matrix)
