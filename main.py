from flask import Flask, request, jsonify
import pandas as pd
from openai_integration import generate_gpt_insights
from data_ingestion import ingest_data

app = Flask(__name__)

# Endpoint for individual sales representative performance
@app.route('/api/rep_performance', methods=['GET'])
def rep_performance():
    rep_id = request.args.get('rep_id')  # Get rep_id from query parameter
    sales_data = ingest_data(r'C:\Users\ALIHA\Downloads\backenddevelopmentexercise\sales_performance_data.csv')
    # Convert rep_id to integer and filter the data
    rep_data = sales_data[sales_data['employee_id'] == int(rep_id)]

    # Check if the filtered data is empty
    if rep_data.empty:
        return jsonify({"rep_id": rep_id, "insights": "No data available for the specified rep."}), 200

    # Create aggregate columns for total texts sent and calls made
    rep_data['texts_sent'] = rep_data[['mon_text', 'tue_text', 'wed_text', 'thur_text', 'fri_text', 'sat_text', 'sun_text']].sum(axis=1)
    rep_data['calls_made'] = rep_data[['mon_call', 'tue_call', 'wed_call', 'thur_call', 'fri_call', 'sat_call', 'sun_call']].sum(axis=1)

    # Limit columns and rows to avoid overloading the model
    relevant_columns = ['employee_id', 'revenue_confirmed', 'tours_scheduled', 'applications', 'texts_sent', 'calls_made']
    rep_data_limited = rep_data[relevant_columns].head(50)

    # Generate insights using GPT
    insights = generate_gpt_insights(rep_data_limited)
    return jsonify({"rep_id": rep_id, "insights": insights})


# Endpoint for overall team performance
@app.route('/api/team_performance', methods=['GET'])
def team_performance():
    sales_data = ingest_data(r'C:\Users\ALIHA\Downloads\backenddevelopmentexercise\sales_performance_data.csv')
    
    # Limit to 100 rows and key columns
    relevant_columns = ['employee_id', 'revenue_confirmed', 'tours_scheduled', 'applications']
    sales_data_limited = sales_data[relevant_columns].head(100)

    # Generate insights using GPT
    insights = generate_gpt_insights(sales_data_limited)
    return jsonify({"team_insights": insights})


# Endpoint for sales performance trends
@app.route('/api/performance_trends', methods=['GET'])
def performance_trends():
    time_period = request.args.get('time_period')  # Get the time period for trend analysis
    sales_data = ingest_data(r'C:\Users\ALIHA\Downloads\backenddevelopmentexercise\sales_performance_data.csv')
    
    # Limit data for trend analysis to avoid token overflow
    relevant_columns = ['employee_id', 'revenue_confirmed', 'tours_scheduled', 'applications']
    sales_data_limited = sales_data[relevant_columns].head(100)

    # Generate insights using GPT
    insights = generate_gpt_insights(sales_data_limited)
    return jsonify({"time_period": time_period, "trends_insights": insights})

if __name__ == '__main__':
    app.run(debug=True)
