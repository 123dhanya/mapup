import pandas as pd
import networkx as nx

def calculate_distance_matrix(dataset_path):
    # Load the dataset
    df = pd.read_csv(dataset_path)

    # Create a directed graph
    G = nx.DiGraph()

    # Add edges and distances to the graph
    for _, row in df.iterrows():
        G.add_edge(row['id_start'], row['id_end'], distance=row['distance'])

    # Create a distance matrix
    distance_matrix = nx.floyd_warshall_numpy(G, weight='distance')

    # Convert the distance matrix to a DataFrame
    distance_df = pd.DataFrame(distance_matrix, index=G.nodes(), columns=G.nodes())

    return distance_df

# Example usage
dataset_path = 'dataset-3.csv'
distance_matrix = calculate_distance_matrix(dataset_path)

# Display the resulting distance matrix
print(distance_matrix)
