import pandas as pd
import numpy as np

def analyze_data(country_data):
    top_countries = country_data[['Country/Region', 'Confirmed', 'Deaths', 'Recovered']]
    top_countries = top_countries.sort_values(by='Confirmed', ascending=False).head(10)
    return top_countries