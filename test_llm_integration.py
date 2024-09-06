import pandas as pd
from openai_integration import generate_gpt_insights
import os

def test_llm_integration():
    # Load a sample of the sales data
    sales_data = pd.read_csv(r'C:\Users\ALIHA\Downloads\backenddevelopmentexercise\sales_performance_data.csv'
)

    # Test the LLM integration by passing a subset of the data
    insights = generate_gpt_insights(sales_data.head())  # Analyze the first few rows for testing
    
    # Print the insights
    print("Generated Insights:\n", insights)

if __name__ == "__main__":
    test_llm_integration()
