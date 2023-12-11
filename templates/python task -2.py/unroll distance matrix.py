import pandas as pd

def unroll_distance_matrix(distance_matrix):
    # Initialize an empty list to store the unrolled data
    unrolled_data = []

    # Iterate over rows in the distance matrix
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            # Skip the combination where id_start is equal to id_end
            if id_start != id_end:
                # Get the distance from the distance matrix
                distance = distance_matrix.loc[id_start, id_end]

                # Append the data to the list
                unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

    # Create a DataFrame from the unrolled data
    unrolled_df = pd.DataFrame(unrolled_data)

    return unrolled_df

# Example usage
unrolled_distance_df = unroll_distance_matrix(distance_matrix)

# Display the resulting unrolled DataFrame
print(unrolled_distance_df)
