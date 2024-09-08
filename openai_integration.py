import openai
import os
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

def process_insights(insights):
    # Simplify and focus on actionable feedback
    key_sections = []
    for line in insights.split('\n'):
        if 'lead conversion' in line.lower() or 'recommendation' in line.lower():
            key_sections.append(line)
    
    return '\n'.join(key_sections)

def format_insights(insights):
    formatted = f"**Sales Performance Insights**\n\n{insights}\n\n**Key Action Points**\n- Encourage collaboration.\n- Improve lead conversion rates."
    return formatted

def generate_gpt_insights(sales_data):
    sales_data_limited = sales_data.head(50)  
    
    # Construct the prompt with limited data
    prompt = f"""
    Analyze the following sales data and provide actionable insights:
    {sales_data_limited.to_string(index=False)}
    
    Focus on:
    1. Lead conversion efficiency.
    2. Individual performance feedback (high and low performers).
    3. Overall team recommendations.
    4. Suggestions for improving sales and conversions.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are an expert in analyzing sales data."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

    except OpenAIError as e:
        return f"An error occurred: {str(e)}"
