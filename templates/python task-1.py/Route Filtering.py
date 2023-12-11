import pandas as pd

def multiply_matrix(result_matrix):
    # Create a deep copy of the input DataFrame to avoid modifying the original
    modified_matrix = result_matrix.copy(deep=True)

    # Apply the multiplication logic based on the given conditions
    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25

    # Round the values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix

# Example usage (assuming result_matrix is the DataFrame from Question 1)
# Replace this line with the actual DataFrame you have from Question 1
result_matrix = pd.DataFrame(data={'A': [0, 25, 10], 'B': [15, 30, 5], 'C': [12, 18, 22]})

modified_result = multiply_matrix(result_matrix)
print(modified_result)
