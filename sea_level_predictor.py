import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    lin_result = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    slope = lin_result.slope
    intercept = lin_result.intercept
    year_extended = pd.Series([int(i) for i in range(1880, 2050)])
    best_fit1 = slope * year_extended + intercept
    plt.plot(year_extended, best_fit1, 'r')

    # Create second line of best fit
    recent = df[df['Year'] >= 2000]
    lin_result = linregress(x=recent['Year'], y=recent['CSIRO Adjusted Sea Level'])
    slope = lin_result.slope
    intercept = lin_result.intercept
    year_extended = pd.Series([int(i) for i in range(2000, 2050)])
    best_fit2 = intercept + slope * year_extended
    plt.plot(year_extended, best_fit2, 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()