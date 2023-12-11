import pandas as pd

def verify_timestamp_completeness(dataset_path):
    # Read the dataset with a specific encoding
    df = pd.read_csv(dataset_path, encoding='ISO-8859-1', sep='\t')

    # Print the column names to identify the correct ones
    print(df.columns)

    # Replace 'your_start_column', 'your_start_time_column', 'your_end_column', and 'your_end_time_column'
    # with the actual column names from your dataset
    start_col = 'startDay'
    time_col = 'startTime'
    end_col = 'endDay'
    end_time_col = 'endTime'

    # Combine start and time columns to create 'start_timestamp'
    df['start_timestamp'] = pd.to_datetime(df[start_col] + ' ' + df[time_col], errors='coerce')

    # Combine end and time columns to create 'end_timestamp'
    df['end_timestamp'] = pd.to_datetime(df[end_col] + ' ' + df[end_time_col], errors='coerce')

    # Clip datetime values to stay within the valid range
    df['start_timestamp'] = df['start_timestamp'].clip(lower=pd.to_datetime('1678-01-01'), upper=pd.to_datetime('2262-04-11'))
    df['end_timestamp'] = df['end_timestamp'].clip(lower=pd.to_datetime('1678-01-01'), upper=pd.to_datetime('2262-04-11'))

    # Check if each (id, id_2) pair has correct timestamps
    completeness_check = (
        df.groupby(['id', 'id_2'])
        .apply(lambda group: (group['end_timestamp'].max() - group['start_timestamp'].min()).total_seconds() ==
                             (pd.to_timedelta('24:00:00')).total_seconds() * 7)
    )

    return completeness_check

# Example usage
dataset_path = 'dataset-2.csv'
completeness_series = verify_timestamp_completeness(dataset_path)

# Display the boolean series with multi-index (id, id_2)
print(completeness_series)
