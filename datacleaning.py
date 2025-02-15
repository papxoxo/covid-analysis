import pandas as pd

def clean_data():
    country_data = pd.read_csv("country_wise_latest.csv")
    day_wise_data = pd.read_csv("day_wise.csv")
    worldometer_data = pd.read_csv("worldometer_data.csv")
    
    # Handle missing values
    country_data.fillna(0, inplace=True)
    day_wise_data.fillna(0, inplace=True)
    worldometer_data.fillna(0, inplace=True)
    
    # Convert Date column to datetime format
    day_wise_data['Date'] = pd.to_datetime(day_wise_data['Date'])
    
    # Sort by Date
    day_wise_data = day_wise_data.sort_values(by='Date')
    
    # Remove duplicate rows if any
    day_wise_data = day_wise_data.drop_duplicates()
    
    # Ensure numerical columns have proper data types
    numeric_cols = ['Confirmed', 'Deaths', 'Recovered', 'New cases', 'New deaths', 'New recovered']
    for col in numeric_cols:
        day_wise_data[col] = pd.to_numeric(day_wise_data[col], errors='coerce').fillna(0)
    
    return country_data, day_wise_data, worldometer_data