import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(top_countries, day_wise_data):
    # Bar plot for top affected countries
    plt.figure(figsize=(12,6))
    sns.barplot(x='Confirmed', y='Country/Region', data=top_countries, palette='Reds_r')
    plt.xlabel("Total Cases")
    plt.ylabel("Country")
    plt.title("Top 10 Countries with Highest COVID-19 Cases")
    plt.show()
    
    # Line plot for daily new cases
    plt.figure(figsize=(12,6))
    sns.lineplot(x='Date', y='New cases', data=day_wise_data, marker='o', color='blue')
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.xticks(rotation=45)
    plt.title("Daily New COVID-19 Cases Trend")
    plt.show()
    
    # Additional Graphs
    # Pie chart for distribution of cases in top 10 countries
    plt.figure(figsize=(8,8))
    plt.pie(top_countries['Confirmed'], labels=top_countries['Country/Region'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Reds', len(top_countries)))
    plt.title("COVID-19 Cases Distribution Among Top 10 Countries")
    plt.show()
    
    # Line plot for daily deaths trend
    plt.figure(figsize=(12,6))
    sns.lineplot(x='Date', y='New deaths', data=day_wise_data, marker='o', color='red')
    plt.xlabel("Date")
    plt.ylabel("New Deaths")
    plt.xticks(rotation=45)
    plt.title("Daily New COVID-19 Deaths Trend")
    plt.show()
    
    # Line plot for daily recovered cases trend
    plt.figure(figsize=(12,6))
    sns.lineplot(x='Date', y='New recovered', data=day_wise_data, marker='o', color='green')
    plt.xlabel("Date")
    plt.ylabel("New Recovered Cases")
    plt.xticks(rotation=45)
    plt.title("Daily New COVID-19 Recovered Cases Trend")
    plt.show()
