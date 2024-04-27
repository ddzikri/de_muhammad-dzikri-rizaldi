import pandas as pd
from datetime import datetime
import os
import firebase_admin
from firebase_admin import storage

class DataWarehouseLoader:
    def __init__(self, service_account_path, bucket_name, local_data_path):
        self.bucket_name = bucket_name
        self.service_account_path = service_account_path
        self.client = None
        self.local_data_path = local_data_path
        self.initialize_firebase()

    def initialize_firebase(self):
        cred = firebase_admin.credentials.Certificate(self.service_account_path)
        firebase_admin.initialize_app(cred, {'storageBucket': self.bucket_name})
        self.client = storage.bucket(self.bucket_name)

    def load_data(self, file_path):
        # Load data from Data Lake (Parquet format)
        df = pd.read_parquet(file_path)
        return df

    def transform_data(self, df_transactions, df_tickets, df_events, df_customer_feedback):
        # Merge transactions with tickets based on ticket_id
        merged_data = pd.merge(df_transactions, df_tickets, on='ticket_id')
        # Merge with events based on event_id
        merged_data = pd.merge(merged_data, df_events, on='event_id')

        # Calculate Tickets Sold per Event
        tickets_sold_per_event = merged_data.groupby('event_id')['quantity'].sum().reset_index()

        # Calculate Total Revenue per Event
        revenue_per_event = merged_data.groupby('event_id')['total_amount'].sum().reset_index()

        # Merge customer_feedback with transactions based on transaction_id
        feedback_analysis = pd.merge(df_customer_feedback, df_transactions, on='transaction_id')

        # Calculate Average Rating per Event
        avg_rating_per_event = feedback_analysis.groupby('feedback_id')['rating'].mean().reset_index()

        return tickets_sold_per_event, revenue_per_event, avg_rating_per_event

    def save_to_warehouse(self, df, table_name):
        # Naming the result file
        current_date = datetime.now().strftime("%Y-%m-%d")
        folder_name = datetime.now().strftime("%Y-%m-%d")
        file_name = f"{table_name}.parquet"

        # Save to local data path
        local_folder_path = os.path.join(self.local_data_path, folder_name)
        os.makedirs(local_folder_path, exist_ok=True)
        local_file_path = os.path.join(local_folder_path, file_name)
        df.to_parquet(local_file_path)

        print(f"Data telah tersimpan di Local Anda: {local_file_path}")

        # Upload to Data Warehouse bucket
        blob = self.client.blob(f"{folder_name}/{file_name}")
        df.to_parquet(f"/tmp/{file_name}")  # Temporary save locally
        blob.upload_from_filename(f"/tmp/{file_name}")

        print(f"Data telah tersimpan di Warehouse: {folder_name}/{file_name}")

# Example usage
if __name__ == "__main__":
    service_account_path = "C:\\codes\\de_muhammad-dzikri-rizaldi\\18_Code-Competence\\praktikum\\ServiceAccount.json"
    bucket_name = "code-competence-41105.appspot.com"
    local_data_path = "C:\\codes\\de_muhammad-dzikri-rizaldi\\18_Code-Competence\\praktikum"

    # Initialize DataWarehouseLoader with service account path, bucket name, and local data path
    loader = DataWarehouseLoader(service_account_path, bucket_name, local_data_path)

    # Load data from Data Lake
    df_transactions = loader.load_data("data_source/transactions.parquet")
    df_tickets = loader.load_data("data_source/tickets.parquet")
    df_events = loader.load_data("data_source/events.parquet")
    df_customer_feedback = loader.load_data("data_source/customer_feedback.parquet")

    # Transform data
    tickets_sold_per_event, revenue_per_event, avg_rating_per_event = loader.transform_data(df_transactions, df_tickets, df_events, df_customer_feedback)

    # Save transformed data to Data Warehouse
    loader.save_to_warehouse(tickets_sold_per_event, "Tickets_sold_per_event")
    loader.save_to_warehouse(revenue_per_event, "Revenue_per_event")
    loader.save_to_warehouse(avg_rating_per_event, "Feedback_analysis")
