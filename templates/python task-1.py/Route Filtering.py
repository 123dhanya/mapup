import pandas as pd

def filter_routes(df):
    # Group by 'route' and calculate the average of the 'truck' column
    route_avg_truck = df.groupby('route')['truck'].mean()

    # Filter routes where the average of 'truck' values is greater than 7
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    # Sort the list of selected routes
    selected_routes.sort()

    return selected_routes

# Example usage
dataset_path = 'dataset-1.csv'
df = pd.read_csv(dataset_path)
result_list = filter_routes(df)
print(result_list)

