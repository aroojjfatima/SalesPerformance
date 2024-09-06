import pandas as pd

def ingest_data(file_path):
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            data = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format. Please use CSV or JSON.")
        
        if data is not None:
            print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error ingesting data: {e}")
        return None


if __name__ == "__main__":
    file_path = r'C:\Users\ALIHA\Downloads\backenddevelopmentexercise\sales_performance_data.csv'
    sales_data = ingest_data(file_path)
    print(sales_data.head())
