from data_ingestion import ingest_data

def test_ingestion():
    file_path = r'C:\Users\ALIHA\Downloads\backenddevelopmentexercise\sales_performance_data.csv'
    sales_data = ingest_data(file_path)
    
    # Check if data is loaded successfully
    if sales_data is not None and not sales_data.empty:
        print("Data Ingestion Successful!")
        print(sales_data.head())  # Print the first few rows to verify
    else:
        print("Data Ingestion Failed!")

if __name__ == "__main__":
    test_ingestion()
