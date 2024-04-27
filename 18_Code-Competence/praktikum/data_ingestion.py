import pandas as pd
import numpy as np
import os

class DataLakeBuilder:
    def read_csv_data(self, file_path):
        return pd.read_csv(file_path)

    def handle_missing_values(self, df):
        return df.ffill().bfill()

    def handle_outliers(self, df, column):
        Q1, Q3 = df[column].quantile([0.25, 0.75])
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[column] = np.clip(df[column], lower_bound, upper_bound)
        return df

    def save_to_parquet(self, df, file_name):

        df.to_parquet(file_name)
        print(f"Data saved to {file_name}.")

    def validate_data(self, file_path):
        
        df = pd.read_parquet(file_path)
        print(df.head(), '\n', df.describe())

# Eksekusi Script
if __name__ == "__main__":
    data_builder = DataLakeBuilder()
    data_source_dir = 'data_source'
    files_to_process = ['events.csv', 'customers.csv', 'tickets.csv', 'transactions.csv', 'customer_feedback.csv']
    for file in files_to_process:
        file_path = os.path.join(data_source_dir, file)
        # Read CSV
        df = data_builder.read_csv_data(file_path)
        if df is not None:
            # Handle missing values
            df = data_builder.handle_missing_values(df)
            # Handle outliers (assuming numeric columns)
            for column in df.select_dtypes(include=np.number).columns:
                df = data_builder.handle_outliers(df, column)
            # Save to Parquet
            file_name = os.path.splitext(file)[0] + '.parquet'
            file_path_parquet = os.path.join(data_source_dir, file_name)
            data_builder.save_to_parquet(df, file_path_parquet)
            # Validate data
            data_builder.validate_data(file_path_parquet)
