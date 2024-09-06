# Sales Performance Analysis App

## Overview

This project is a Flask-based web application that integrates with a Large Language Model (LLM) such as GPT-3.5 to analyze sales performance data. The system processes sales data, generates qualitative feedback, and provides actionable insights for both individual sales representatives and the entire sales team.

## Features

- **LLM Integration:** Leverages GPT-3.5 to analyze sales data and provide insights for performance improvement.
- **Individual Representative Insights:** Feedback and suggestions based on the lead conversion efficiency, call/text activity, and performance.
- **Team-Wide Insights:** Performance trends, activity analysis, and actionable recommendations for the entire team.
- **Data-Driven Feedback:** Automated feedback generation for high and low performers with recommendations for improvement.

## Architecture

- **Backend:** Flask framework for serving APIs.
- **Data Processing:** Pandas for ingesting and processing sales performance data.
- **LLM Integration:** OpenAI API for generating qualitative feedback and actionable insights.
- **Database:** CSV-based data processing for sales data (extendable to other data sources).
- **API Endpoints:**
  - `/api/rep_performance`: Provides individual sales representative performance analysis.
  - `/api/team_performance`: Generates insights for overall team performance.
  - `/api/performance_trends`: Analyzes performance trends over a specific time period.

## Technologies Used

- **Python**: Main programming language for the backend.
- **Flask**: Web framework for building and running the application.
- **Pandas**: Library for data manipulation and analysis.
- **OpenAI API**: Used for LLM integration to generate feedback and insights.
- **Git**: Version control system.
- **HTML/CSS/JavaScript**: For frontend development if further extended.

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/your-username/SalesPerformanceApp.git
cd SalesPerformanceApp

### 2. Create and activate a virtual environment
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\\Scripts\\activate
# On MacOS/Linux:
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Set Up Environment Variables
You need an OpenAI API key to use the GPT-based insights generation feature. Create a .env file in the root directory of the project and add your OpenAI API key like this:
# .env file content
OPENAI_API_KEY=your-openai-api-key-here
### 5. Run the Flask Application
Start the Flask development server:
flask run

The application will now be running on http://127.0.0.1:5000/.

### 6. Test the API Endpoints
You can test the following API endpoints:

/api/rep_performance?rep_id=<id>: Provides individual sales representative performance analysis.
/api/team_performance: Generates insights for overall team performance.
/api/performance_trends?time_period=<30_days>: Analyzes performance trends over a specific time period.
To access these endpoints, you can use tools like Postman or cURL, or simply visit them in your browser.

### 7. Running Tests
To ensure everything is functioning correctly, run the test script:
python test_llm_integration.py
This script will test the integration of the Large Language Model (LLM) with the sales data processing system.
