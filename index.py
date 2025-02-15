if __name__ == "__main__":
    from datacleaning import clean_data
    from datanalysis import analyze_data
    from datavisualization import visualize_data
    
    country_data, day_wise_data, worldometer_data = clean_data()
    top_countries = analyze_data(country_data)
    visualize_data(top_countries, day_wise_data)
    
    # Save cleaned and processed data
    top_countries.to_csv("top_countries.csv", index=False)
    day_wise_data.to_csv("cleaned_day_wise.csv", index=False)
